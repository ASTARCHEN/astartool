#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 河北雪域网络科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.snowland.ltd
# @file: _random.py
# @time: 2019/5/29 11:39
# @Software: PyCharm


__author__ = 'A.Star'

from random import choices, randint
from astartool.common import *
from astartool.number import ishex
from pysmx.SM3 import KDF


def random_string(n: int = 32, allow_chars=alnum_string):
    """
    生成随机字符串
    :param n: n位数
    :param allow_chars: 允许的字符串
    :return:
    """
    return ''.join(choices(allow_chars, k=n))


def random_hex_string(n: int = 32, upper=False):
    """
    生成随机16进制数
    :param n:
    :param upper:
    :return:
    """
    return ''.join(choices(hex_string_upper, k=n)) if upper else ''.join(choices(hex_string, k=n))


def random_digit_string(n: int = 32) -> str:
    """
    生成随机n位数字
    :param n:
    :return:
    """
    return random_string(n, digit_string)


def generate_password(n: int = 32, allow_chars=password_allowed_string):
    """
    生成随机密码
    :param n:
    :param allow_chars:
    :return:
    """
    return random_string(n, allow_chars)


def security_random_hex(seed: (str, bytes), k: int, encoding='utf8') -> str:
    """
    生成随机16进制数
    :param seed:
    :param k:
    :param encoding:
    :return:
    """
    if isinstance(seed, bytes):
        z = seed.hex()
    elif isinstance(seed, str):
        if ishex(seed):
            z = seed
        else:
            z = seed.encode(encoding).hex()
    return KDF(z, k)


def random_ip():
    return '.'.join([str(randint(0, 255)) for _ in range(4)])
