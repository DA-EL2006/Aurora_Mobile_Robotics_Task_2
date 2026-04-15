#!/usr/bin/env python3
"""Ackermann motion built in code, then played live at 0.5× speed with logging.

Shows the same parameters as :func:`amr.play_motion_by_kind` but with a custom path.

Run::

    PYTHONPATH=. python examples/live_ackermann_session.py

Optional: append logs to a file by setting ``LOG_PATH`` below.
"""

from __future__ import annotations

import math
import sys

import AuroraMR as amr

# Set to a path string to tee logs to a file, or None for stdout only
LOG_PATH: str | None = None


def main() -> None:
    params = amr.AckermannParams(
        wheelbase=0.55,
        track_width=0.36,
        max_steering_angle=0.5,
        max_speed=1.0,
    )
    session = amr.MotionSession.create(
        amr.pose(0.0, 0.0, 0.0),
        amr.KinematicsModel.ACKERMANN,
        dt=0.02,
        ackermann=params,
    )
    session.forward(1.8, 0.5)
    session.turn_left(math.radians(45), 0.75)
    session.forward(1.2, 0.45)

    log_stream = open(LOG_PATH, "w", encoding="utf-8") if LOG_PATH else None
    try:

        class Tee:
            def __init__(self, *streams: object) -> None:
                self.streams = streams

            def write(self, data: str) -> None:
                for s in self.streams:
                    s.write(data)
                    s.flush()

            def flush(self) -> None:
                for s in self.streams:
                    s.flush()

        out: object = Tee(sys.stdout, log_stream) if log_stream else sys.stdout

        opts = amr.PlaybackLogOptions(
            enabled=True,
            every_n_frames=8,
            detailed_block=True,
            include_velocity=True,
            file=out,  # type: ignore[arg-type]
        )

        amr.play_motion(
            session,
            interval_ms=30,
            playback_speed=0.5,
            title="Ackermann (custom path)",
            show=True,
            log_options=opts,
        )
    finally:
        if log_stream is not None:
            log_stream.close()


if __name__ == "__main__":
    main()
