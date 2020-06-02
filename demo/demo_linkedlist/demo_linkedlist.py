#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 深圳星河软通科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.astar.ltd
# @file: demo_linkedlist .py
# @time: 2020/5/21 18:10
# @Software: PyCharm

from astartool.data_structure.linked_list import *



if __name__ == '__main__':
    li = LinkedList((1, 2, 3, 4, 5))

    li.append(1)
    li.append(2)
    li.append(3)
    li.append(4)
    li.print()
    li.extend((5, 6, 7, 8, 9, 0))
    li.print()
    print(li.pop())
    li.print()
    print(li.pop(0))
    li.print()
    li.reverse()
    li.print()

