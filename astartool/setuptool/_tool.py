#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 河北雪域网络科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.snowland.ltd
# @file: _tool.py
# @time: 2019/5/29 11:27
# @Software: PyCharm


__author__ = 'A.Star'

from setuptools import setup as _setup
import sys


def load_install_requires(filepath='requirements.txt', encoding='utf-8'):
    """
    通过filepath生成setup.py的install_requires
    :param filepath:
    :param encoding:
    :return:
    """
    with open(filepath, 'r', encoding=encoding) as f:
        lines = f.readlines()
    return [line.strip() for line in lines if not line.startswith('#')]


def __alart_setup():
    print("Version is not final, do you really wants to setup it?")
    print("[Y] yes.")
    print("[N] no.")


def setup(**attrs):
    version = attrs['version']
    if isinstance(version, tuple):
        if len(version) > 3:
            if version[3] not in ['F', 'f', 'final', 'Final']:
                __alart_setup()
                inp = input()
                if inp in ['Y', 'y', 'yes', 'Yes', 'YES']:
                    return _setup(**attrs)
            else:
                sys.exit()
    return _setup(**attrs)
