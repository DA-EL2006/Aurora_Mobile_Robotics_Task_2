#!/usr/bin/env python3
"""Plot one robot with the default style (rectangle body + triangular head)."""

from __future__ import annotations

import math

import AuroraMR as amr

p = amr.pose(0.0, 0.0, 0.0)
# ``style="robot"`` is the default; opens a window with plt.show() unless you
# pass ``ax=`` or ``show=False``.
amr.simulate(p)
