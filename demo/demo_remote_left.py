#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 河北雪域网络科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.snowland.ltd
# @file: demo_remote_left.py
# @time: 2019/6/2 23:45
# @Software: PyCharm


__author__ = 'A.Star'

from astartool.number import rotate_left as rotate_left_2
from astartool.common import BIT_EACH
import time
import random


def rotate_left(a, k, mod=32):
    k %= mod
    return ((a << k) & (BIT_EACH[mod]-1)) | ((a & (BIT_EACH[mod]-1)) >> (mod - k))


if __name__ == '__main__':
    itor_number = 100
    count = 0
    for itor in range(itor_number):
        init = time.clock()
        n = 100000
        a = [random.randint(0, 1 << 32) for i in range(n)]
        k = [random.randint(0, 32) for i in range(n)]
        t1, t2 = [], []
        start1 = time.clock()
        for i in range(n):
            t1.append(rotate_left(a[i], k[i]))
        end1 = time.clock()
        start2 = time.clock()
        for i in range(n):
            t2.append(rotate_left_2(a[i], k[i]))
        end2 = time.clock()
        assert t1 == t2
        time1 = end1 - start1
        time2 = end2 - start2
        print("time 1:", time1)
        print("time 2:", time2)
        if time2 < time1:
            count += 1

    print("快速左移比较快的次数是:", count)
    print("快速左移比较快的概率是:", count/itor_number)

