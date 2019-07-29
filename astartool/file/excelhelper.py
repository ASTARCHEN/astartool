#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 河北雪域网络科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.snowland.ltd
# @file: excelhelper.py
# @time: 2019/6/13 17:33
# @Software: PyCharm


__author__ = 'A.Star'

import xlwt


def to_excel(data, filename: str, sheetname: str="Sheet1", fields: list = None, *,
             output_fields: list = None, encoding='utf-8'):
    workbook = xlwt.Workbook(encoding=encoding)
    booksheet = workbook.add_sheet(sheetname, cell_overwrite_ok=True)
    if output_fields is None:
        output_fields = fields
    start = 0
    if output_fields:
        [booksheet.write(0, i, field) for i, field in enumerate(output_fields)]
        start += 1
    if isinstance(data[0], dict):
        [[booksheet.write(j, i, objects[field]) for i, field in enumerate(fields)] for j, objects in
         enumerate(data, start)]
    else:
        [[booksheet.write(j, i, rowdata[i]) for i, cell in enumerate(rowdata)] for j, rowdata in enumerate(data, start)]
    workbook.save(filename)
