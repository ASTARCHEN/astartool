# -*- coding: utf-8 -*-

from astartool.project import is_windows
import time


time_clock = time.time if is_windows() else time.clock
