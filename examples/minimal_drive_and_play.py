import math

import AuroraMR as amr

s = amr.MotionSession.create(amr.pose(0, 0, 0), amr.KinematicsModel.TWO_WHEEL, dt=0.02)
s.forward(1.0, 0.5)
s.turn_left(math.pi / 4, 1.0)
s.forward(0.5, 0.5)
s.turn_right(math.pi / 6, 1.0)
s.forward(0.5, 0.5)
s.turn_left(math.pi, 1.0)
s.forward(1.0, 0.5)

amr.play_motion(s, playback_speed=2.0, log=True, show=True)
