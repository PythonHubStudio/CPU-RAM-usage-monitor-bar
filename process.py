
# Copyright (c) 2020 Tukas Oleksandr. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
# This file is part of the "CPU-RAM usage monitor bar"

"""
The module reads the load indicators of the CPU and RAM.
If psutil is not installed, enter the command at the command line:
pip install psutil
"""

import psutil as pt


class CpuBar():
    """Read CPU and RAM usage."""

    def __init__(self):
        """The number of physical and logical CPU cores."""
        self.cpu_count = pt.cpu_count(logical=False)
        self.cpu_count_logical = pt.cpu_count()

    def cpu_percent_return(self):
        """Reads the load of the CPU cores."""
        return pt.cpu_percent(percpu=True)

    def cpu_one_return(self):
        """Reads the total CPU usage."""
        return pt.cpu_percent()

    def ram_usage(self):
        """Reads the load of RAM."""
        return pt.virtual_memory()
