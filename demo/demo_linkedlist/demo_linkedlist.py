#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 深圳星河软通科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.astar.ltd
# @file: demo_linkedlist .py
# @time: 2020/5/21 18:10
# @Software: PyCharm

from astartool.data_structure.linked_list import *

# a = LinkedList((1, 2))
# print(a == [1,2,3])
# print(a == (1,2,3))
# print(a[0])
# print(a[1])
# print(a[2])
# b = (a + 3)
# b.print()
# for each in b:
#     print(each)


# c = a.copy()
# c.print()
# assert c == [1, 2]
# a.extend([4, 5, 6, 7])
# assert a == [1, 2, 4, 5, 6, 7]
# a.print()
# a.reverse()
# a.print()
# assert a == [7, 6, 5, 4, 2, 1]
# a.clear()
# print("clear")
# a.print()
# a.append([1, 2, 3, 4, 5, 6, 7])
# a.append((2, 3, 4))
# a.print()
a = LinkedList(list(range(100)))
a.print()
b = a[:10]
b.print()
assert b == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
c = a[-2:]
c.print()
assert c == [98, 99]
d = a[::-1]
a.reverse()
d.print()
a.print()
assert d == a
a.reverse()
e = a[:20:10]
e.print()
assert e == [0, 10]
f = a[1:10:2]
assert f == [1, 3, 5, 7, 9]
