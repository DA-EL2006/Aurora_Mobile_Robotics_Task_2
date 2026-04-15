import math

import AuroraMR as amr

s = amr.MotionSession.create(
    amr.pose(0, 0, 0),
    amr.KinematicsModel.TWO_WHEEL,
    dt=0.02
)

unicycle = amr.UnicycleParams(
    track_width=0.4,
    max_linear_speed=1.5
)

s.forward(1.0 , speed =0.8) # move 1 m forward at 0.8 m / s

s.turn_left (math.pi /2 , 1.0) # turn 90 deg CCW at 1.0 rad /

s.forward (0.5 , speed =0.8) # move 0.5 m forward

amr.plot_motion (s) # static plot

amr.play_motion(s, interval_ms=25, log=True, log_every_n_frames=12)  # live animation + terminal logs