#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 河北雪域网络科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.snowland.ltd
# @file: demo_model_to_doc.py
# @time: 2019/6/12 12:45
# @Software: PyCharm


__author__ = 'A.Star'

from astartool.project import model_to_doc, model_to_dict

if __name__ == '__main__':
    d = model_to_dict('models.py')
    print(d)
    model_to_doc('models.py')
