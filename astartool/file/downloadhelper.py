#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 河北雪域网络科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.snowland.ltd
# @file: downloadhelper.py
# @time: 2019/6/13 17:33
# @Software: PyCharm

def big_file_download(file_name):
    # do something...

    def file_iterator(file_name, chunk_size=16 * 2 ** 10):
        with open(file_name, 'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    try:
        return file_iterator(file_name)
    except BaseException as e:
        # 没有对应的文件
        print(str(FileNotFoundError))
    return None
