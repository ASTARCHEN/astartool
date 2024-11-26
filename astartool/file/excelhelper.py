#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 河北雪域网络科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.snowland.ltd
# @file: excelhelper.py
# @time: 2019/6/13 17:33
# @Software: PyCharm


__author__ = 'A.Star'

from typing import Union, List, Iterable, Tuple

import xlwt
import xlrd


def to_excel(data,
             filename: str,
             sheetname: Union[str, Union[List[str], Tuple]] = "Sheet1",
             fields: Union[Iterable[str], Iterable[List[str]]] = None, *,
             output_fields: Union[Iterable[str], Iterable[List[str]]] = None, encoding='utf-8'):
    """
    把数据转化到excel中
    :param data:
    :param filename:
    :param sheetname: 表名
    :param fields:
    :param output_fields: 输出的标签名
    :param encoding: 字符编码方式
    :return:
    """
    if isinstance(sheetname, str):
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
    else:
        workbook = xlwt.Workbook(encoding=encoding)
        if fields is None:
            fields = [None] * len(sheetname)
        if output_fields is None:
            output_fields = fields

        for sheet_number, (it_sheetname, it_data, it_fields, it_output_fields) in enumerate(zip(sheetname, data, fields, output_fields)):
            booksheet = workbook.add_sheet(it_sheetname, cell_overwrite_ok=True)
            start = 0
            if it_output_fields:
                [booksheet.write(0, i, field) for i, field in enumerate(it_output_fields)]
                start += 1
            if isinstance(it_data[0], dict):
                [[booksheet.write(j, i, objects[field]) for i, field in enumerate(it_fields)] for j, objects in
                 enumerate(it_data, start)]
            else:
                [[booksheet.write(j, i, rowdata[i]) for i, cell in enumerate(rowdata)] for j, rowdata in enumerate(it_data, start)]
        workbook.save(filename)
