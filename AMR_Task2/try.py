import math #This imports the math toolkit or library having extra math features like square roots etc

import AuroraMR as amr #This imports the AuroraMR library and gives us access to call functions from the library.


pose = amr.pose(0, 0, 0) #pose function, defines the position (x, y) and the angle (theta)


s = amr.MotionSession.create(amr.pose(0, 0, 0), amr.KinematicsModel.TWO_WHEEL, dt=0.02)
s.forward(0.8, 0.5)
s.turn_left(math.pi / 3, 0.9)
s.forward(0.4, 0.5)
s.forward(0.8, 0.5)
s.turn_left(math.pi / 3, 0.9)
s.forward(0.4, 0.5)
s.forward(0.8, 0.5)
s.turn_left(math.pi / 3, 0.9)
s.forward(0.4, 0.5)
s.forward(0.8, 0.5)
s.turn_left(math.pi / 3, 0.9)
s.forward(0.4, 0.5)
s.forward(0.8, 0.5)
s.turn_left(math.pi / 3, 0.9)
s.forward(0.4, 0.5)
s.forward(0.8, 0.5)
s.turn_left(math.pi / 3, 0.9)
s.forward(0.4, 0.5)


# Set MPLBACKEND if you have no display, or use show=False to skip the window
# and still get logs printed to the terminal
amr.play_motion(s, interval_ms=30, log=True, log_every_n_frames=10, show=True)