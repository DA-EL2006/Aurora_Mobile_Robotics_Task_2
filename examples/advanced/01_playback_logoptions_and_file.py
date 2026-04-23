"""Advanced: ``PlaybackLogOptions`` (detailed blocks, tire samples) + tee logs to a file.

Run:  PYTHONPATH=. python examples/advanced/01_playback_logoptions_and_file.py

Inspect ``adv_playback.log`` in this folder and watch stdout for the same lines.
"""

from __future__ import annotations

import math
import os
import sys
import warnings
from pathlib import Path

import matplotlib.pyplot as plt

import AuroraMR as amr

# Headless: FuncAnimation is not shown; Matplotlib may warn on teardown (harmless here).
warnings.filterwarnings(
    "ignore",
    message="Animation was deleted without rendering",
    category=UserWarning,
    module="matplotlib.animation",
)

os.environ.setdefault("MPLBACKEND", "Agg")

here = Path(__file__).resolve().parent
log_path = here / "adv_playback.log"


class _Tee:
    """Write to several streams (same pattern as live_ackermann_session)."""

    def __init__(self, *streams: object) -> None:
        self.streams = streams

    def write(self, data: str) -> object:
        for s in self.streams:
            s.write(data)
            s.flush()
        return len(data)

    def flush(self) -> None:
        for s in self.streams:
            s.flush()


def main() -> None:
    s = amr.MotionSession.create(amr.pose(0, 0, 0), amr.KinematicsModel.TWO_WHEEL, dt=0.02)
    s.forward(0.6, 0.5)
    s.turn_left(math.pi / 3, 0.9)
    s.forward(0.3, 0.45)

    with open(log_path, "w", encoding="utf-8") as f:
        tee = _Tee(sys.stdout, f)
        opts = amr.PlaybackLogOptions(
            enabled=True,
            every_n_frames=8,
            detailed_block=True,
            include_velocity=True,
            include_tire_sample=True,
            file=tee,  # type: ignore[arg-type]
        )
        anim = amr.play_motion(
            s,
            interval_ms=20,
            playback_speed=1.5,
            title="TWO_WHEEL (logged)",
            show=False,
            log_options=opts,
        )
        del anim
        plt.close("all")

    print(f"\nAlso wrote full log to: {log_path}")


if __name__ == "__main__":
    main()
