from __future__ import annotations

import math

import pytest

from amr.kinematics.integration import (
    ackermann_front_steering_angles,
    differential_to_twist,
    integrate_unicycle,
    mecanum_twist,
    wrap_pi,
    wheel_contacts_world,
)
from amr.kinematics.params import KinematicsModel, MecanumParams, UnicycleParams
from amr.motion import MotionSession
from amr.pose import pose


def test_wrap_pi():
    assert abs(abs(wrap_pi(3 * math.pi)) - math.pi) < 1e-9
    assert abs(wrap_pi(-math.pi / 2) + math.pi / 2) < 1e-9


def test_two_wheel_legacy_unicycle_alias():
    assert KinematicsModel.UNICYCLE is KinematicsModel.TWO_WHEEL
    assert KinematicsModel.UNICYCLE.value == "two_wheel"


def test_unicycle_forward_north():
    p0 = pose(0.0, 0.0, 0.0)
    p1 = integrate_unicycle(p0, 1.0, 0.0, 0.1)
    assert p1.y > p0.y + 0.09
    assert abs(p1.x) < 1e-6


def test_differential_twist_straight():
    v, w = differential_to_twist(1.0, 1.0, 0.4)
    assert abs(v - 1.0) < 1e-9
    assert abs(w) < 1e-9


def test_differential_twist_turn():
    v, w = differential_to_twist(0.0, 1.0, 0.4)
    assert abs(v - 0.5) < 1e-9
    assert abs(w - 2.5) < 1e-9


def test_wheel_contacts_symmetric():
    l, r = wheel_contacts_world((0.0, 0.0), 0.0, 0.4)
    assert abs(l[0] - (-0.2)) < 1e-9
    assert abs(r[0] - 0.2) < 1e-9


def test_ackermann_front_angles_left_turn():
    d_l, d_r = ackermann_front_steering_angles(0.35, 0.55, 0.35)
    assert d_l > d_r > 0


def test_mecanum_twist_forward():
    lx, ly = 0.25, 0.2
    vx, vy, om = mecanum_twist(1.0, 1.0, 1.0, 1.0, lx, ly)
    assert abs(vy - 1.0) < 1e-9
    assert abs(vx) < 1e-9
    assert abs(om) < 1e-9


def test_mecanum_twist_strafe():
    lx, ly = 0.25, 0.2
    vx, vy, om = mecanum_twist(-1.0, 1.0, 1.0, -1.0, lx, ly)
    assert abs(vy) < 1e-9
    assert abs(vx - 1.0) < 1e-9
    assert abs(om) < 1e-9


def test_motion_session_forward_unicycle():
    s = MotionSession.create(
        pose(0, 0, 0),
        KinematicsModel.TWO_WHEEL,
        dt=0.01,
        unicycle=UnicycleParams(max_linear_speed=2.0),
    )
    s.forward(1.0, 1.0)
    assert s.pose.y > 0.99
    assert len(s.trace_left) == len(s.trace_right) == len(s.poses)


def test_motion_turn_left_increases_theta_ccw():
    s = MotionSession.create(pose(0, 0, 0), KinematicsModel.TWO_WHEEL, dt=0.01)
    t0 = s.pose.theta
    s.turn_left(math.pi / 2, 1.0)
    assert wrap_pi(s.pose.theta - t0) > math.pi / 2 - 0.1


def test_drive_to_pose():
    s = MotionSession.create(pose(0, 0, 0), KinematicsModel.TWO_WHEEL, dt=0.02)
    goal = pose(2.0, 1.0, math.pi / 4)
    s.drive_to_pose(goal, linear_speed=0.8, angular_speed=1.0, position_tol=0.08, angle_tol=0.08)
    assert math.hypot(s.pose.x - goal.x, s.pose.y - goal.y) < 0.1


def test_ackermann_drive_to_pose_raises():
    s = MotionSession.create(pose(0, 0, 0), KinematicsModel.ACKERMANN, dt=0.02)
    with pytest.raises(NotImplementedError):
        s.drive_to_pose(pose(1, 1, 0), linear_speed=0.5, angular_speed=0.5)


def test_bicycle_legacy_maps_to_ackermann():
    from amr.kinematics.params import BicycleParams

    s = MotionSession.create(
        pose(0, 0, 0),
        KinematicsModel.BICYCLE,
        dt=0.02,
        bicycle=BicycleParams(rear_track_width=0.4),
    )
    assert s.ackermann is not None
    assert abs(s.ackermann.track_width - 0.4) < 1e-9
    assert len(s.trace_front_left) == len(s.poses)


def test_differential_forward_wheels():
    from amr.kinematics.params import DifferentialParams

    s = MotionSession.create(
        pose(0, 0, 0),
        KinematicsModel.DIFFERENTIAL,
        dt=0.01,
        differential=DifferentialParams(track_width=0.4, max_wheel_speed=2.0),
    )
    s.forward_wheels(1.0, 1.0)
    assert s.pose.y > 0.99


def test_mecanum_strafe_and_rotate():
    s = MotionSession.create(
        pose(0, 0, 0),
        KinematicsModel.MECANUM,
        dt=0.01,
        mecanum=MecanumParams(half_length_y=0.25, half_width_x=0.2, max_wheel_speed=3.0),
    )
    s.strafe_right(0.5, 0.8)
    assert abs(s.pose.x) > 0.2
    s.turn_left(math.pi / 4, 1.0)
    assert abs(wrap_pi(s.pose.theta) - math.pi / 4) < 0.15
