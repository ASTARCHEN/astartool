# -*- coding: utf-8 -*-

import cProfile
import pstats
import os
import wrapt


def do_cprofile(filename):
    """
    性能分析装饰器定义
    params filename: 导出文件文件名
    """
    @wrapt.decorator
    def profiled_func(func, instance, args, kwargs):
        # Flag for do profiling or not.
        DO_PROF = os.getenv("PROFILING")
        if DO_PROF:
            profile = cProfile.Profile()
            profile.enable()
            result = func(*args, **kwargs)
            profile.disable()
            # Sort stat by internal time.
            sortby = "tottime"
            ps = pstats.Stats(profile).sort_stats(sortby)
            ps.dump_stats(filename)
        else:
            result = func(*args, **kwargs)
        return result

    return profiled_func

