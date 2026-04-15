from __future__ import annotations

import io

import pytest

from amr.kinematics.params import KinematicsModel, UnicycleParams
from amr.motion import MotionSession
from amr.playback_log import (
    PlaybackLogOptions,
    effective_interval_ms,
    format_kinematics_params,
    log_session_start,
)
from amr.pose import pose


def test_effective_interval_ms():
    assert effective_interval_ms(100.0, 2.0) == 50.0
    assert effective_interval_ms(100.0, 0.5) == 200.0
    with pytest.raises(ValueError):
        effective_interval_ms(100.0, 0.0)


def test_format_kinematics_params():
    s = MotionSession.create(
        pose(0, 0, 0),
        KinematicsModel.TWO_WHEEL,
        dt=0.02,
        unicycle=UnicycleParams(track_width=0.5),
    )
    text = format_kinematics_params(s)
    assert "two_wheel" in text.lower()
    assert "0.02" in text


def test_log_session_start_runs():
    buf = io.StringIO()
    s = MotionSession.create(pose(0, 0, 0), KinematicsModel.TWO_WHEEL, dt=0.02)
    log_session_start(s, title="Test", interval_ms=25.0, playback_speed=2.0, file=buf)
    out = buf.getvalue()
    assert "Test" in out
    assert "50" in out or "25" in out
