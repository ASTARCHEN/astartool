#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 深圳星河软通科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.astar.ltd
# @file: demo_project.py
# @time: 2019/11/13 17:15
# @Software: PyCharm


from astartool.project._decorators import std_logging, file_logging

@std_logging()
def fun(a, b):
    return a+b

@file_logging()
def fun2(a, b):
    return a*b

print(fun(2,4))
print(fun2(2,4))
