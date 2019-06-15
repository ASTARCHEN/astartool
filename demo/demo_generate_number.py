#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 河北雪域网络科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.snowland.ltd
# @file: demo_generate_number.py
# @time: 2019/6/4 1:55
# @Software: PyCharm


__author__ = 'A.Star'

from astartool.string import generate_number, check_number
from astartool.random import generate_password, random_string
from astartool.common import password_allowed_string_upper, alnum_string

number = generate_number(k=20)
print(number)
print(check_number(number))
print(generate_password(allow_chars=password_allowed_string_upper))  # v)70d!)n6$(j%)b@^)9ga!@ot@3a!6k(
print(random_string(16, alnum_string))  # kXoGcoOA5iLXCBeI
