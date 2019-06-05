#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 河北雪域网络科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.snowland.ltd
# @file: common.py
# @time: 2019/5/29 11:41
# @Software: PyCharm


__author__ = 'A.Star'

hex_string = '0123456789abcdef'
hex_string_upper = '0123456789ABCDFEF'
alnum_string = '0123456789qwertyuiopasdfghjklzxcvbnm'
alpha_string = 'qwertyuiopasdfghjklzxcvbnm'
digit_string = '0123456789'
password_allowed_string = '1234567890qwertyuiopasdfghjklzxcvbnm!@#$%^*()'
password_allowed_string_upper = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^*()'
hex_allowed_string = '0123456789ABCDEFabcdef'

BIT_BLOCK_H = [0x00, 0x80, 0xC0, 0xE0, 0xF0, 0xF8, 0xFC, 0xFE, 0xFF]
BIT_BLOCK_L = [0x00, 0x01, 0x03, 0x07, 0x0F, 0x1F, 0x3F, 0x7F, 0xFF]
BIT_EACH = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144,
            524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456,
            536870912, 1073741824, 2147483648, 4294967296]

