#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 深圳星河软通科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.astar.ltd
# @file: demo_linkedlist .py
# @time: 2020/5/21 18:10
# @Software: PyCharm

from astartool.data_structure.linked_list import *



a = LinkedList((1,2))
# print(a == [1,2,3])
# print(a == (1,2,3))
# print(a[0])
# print(a[1])
# print(a[2])
# b = (a + 3)
# b.print()
# for each in b:
#     print(each)


c = a.copy()
c.print()
a.extend([4,5,6,7])
a.print()
a.reverse()
a.print()
a.clear()
print("clear")
a.print()
a.append([1,2,3,4,5,6,7])
a.append((2,3,4))
a.print()