#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 河北雪域网络科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.snowland.ltd
# @file: _tool.py
# @time: 2019/5/29 11:27
# @Software: PyCharm


__author__ = 'A.Star'

import os
import sys

from setuptools import setup as _setup

from astartool.project import alert_dialog


def load_install_requires(filepath='requirements.txt', encoding='utf-8'):
    """
    通过filepath生成setup.py的install_requires
    :param filepath:
    :param encoding:
    :return:
    """
    with open(filepath, 'r', encoding=encoding) as f:
        lines = f.readlines()
    return [line.strip() for line in lines if not line.strip().startswith('#')]


def read_file(file_name, encoding='utf-8'):
    """
    读取本地文件
    :param file_name: 文件名
    :param encoding: 文件编码，默认utf-8
    :return:
    """
    osp = os.path
    return open(osp.join(osp.dirname(__file__), file_name), 'r', encoding=encoding).read()


def __alart_setup():
    print("Version is not final, do you really wants to setup it?")
    print("[Y] yes.")
    print("[N] no.")


def setup(**attrs):
    version = attrs['version']
    if isinstance(version, tuple):
        if len(version) > 3:
            if version[3] not in ['F', 'f', 'final', 'Final']:
                show_text = "Version is not final, do you really wants to setup it?\n[Y] yes.\n[N] no."
                ok_flag = lambda inp: inp[0] in ['Y', 'y']
                yes_callback = None
                no_callback = lambda: sys.exit()
                alert_dialog(ok_flag,
                             cancel_flag=True,
                             show_text=show_text,
                             okay_callback=yes_callback,
                             cancel_callback=no_callback)

    return _setup(**attrs)
