#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 河北雪域网络科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.snowland.ltd
# @file: __init__.py.py
# @time: 2019/5/29 11:25
# @Software: PyCharm


__author__ = 'A.Star'

from astartool.setuptool import get_version

version = (0, 0, 8, 'final', 0)
__version__ = get_version(version)
__all__ = [
    'setuptool',
    'random',
    'number',
    'version',
    'common',
    'string',
    'project',
    'file',
    'data_structure'
]
