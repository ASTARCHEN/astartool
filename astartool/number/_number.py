#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 河北雪域网络科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.snowland.ltd
# @file: _number.py
# @time: 2019/5/29 11:59
# @Software: PyCharm


__author__ = 'A.Star'

from astartool.common import hex_allowed_string


def ishex(s: str):
    """
    判断一个字符串是否是16进制数
    :param s:
    :return:
    """
    for ch in s:
        if ch not in hex_allowed_string:
            return False
    return True


def gcd(a: int, b: int):
    """
    a和b的最大公约数
    :param a:
    :param b:
    :return:
    """
    while b != 1:
        a, b = divmod(a, b)
    return a


def lcm(a: int, b: int):
    """
    a和b的最小公倍数
    :param a:
    :param b:
    :return:
    """
    return a // gcd(a, b) * b
