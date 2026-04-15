#!/usr/bin/env python3
"""Let :func:`amr.simulate` create the figure (no ``ax=``), but skip ``plt.show()``.

Use this when you want the default layout but only save to a file (no GUI).
"""

from __future__ import annotations

import os

import matplotlib.pyplot as plt

import AuroraMR as amr

os.environ.setdefault("MPLBACKEND", "Agg")

p = amr.pose(0.0, 0.0, 0.0)
amr.simulate(p, show=False)

out = os.path.join(os.path.dirname(__file__), "headless_default_figure.png")
plt.savefig(out, dpi=150)
print("Wrote", out)
plt.close()
