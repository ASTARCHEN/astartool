# -*- coding: utf-8 -*-


import platform


def is_windows():
    return platform.system().lower() == 'windows'


def is_linux():
    return platform.system().lower() == 'linux'

