#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 深圳星河软通科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.astar.ltd
# @file: _decorators.py
# @time: 2019/11/13 16:26
# @Software: PyCharm


import wrapt
import logging
from astartool.common import LOG_LEVEL_MAP_INT2STR, LOG_LEVEL_MAP_STR2INT, LOG_LEVEL_STR, LOG_LEVEL_INT


def std_logging(level=logging.INFO):
    """
    日志记录
    :param level:
    :return:
    """
    int_flag = level in LOG_LEVEL_INT
    assert int_flag or level in LOG_LEVEL_STR
    if int_flag:
        level = LOG_LEVEL_MAP_INT2STR[level]

    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        print("[{}]: enter {}()".format(level, wrapped.__name__))
        f = wrapped(*args, **kwargs)
        print("[{}]: exit {}()".format(level, wrapped.__name__))
        return f

    return wrapper


def file_logging(level=logging.INFO):
    """
    日志记录
    :param level:
    :return:
    """
    str_flag = level in LOG_LEVEL_STR
    assert str_flag or level in LOG_LEVEL_INT
    if str_flag:
        level = LOG_LEVEL_MAP_STR2INT[level]

    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        logging.log(level, "enter {}()".format(wrapped.__name__))
        f = wrapped(*args, **kwargs)
        logging.log(level, "exit {}()".format(wrapped.__name__))
        return f

    return wrapper
