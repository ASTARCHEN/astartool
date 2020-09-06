#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 河北雪域网络科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.snowland.ltd
# @file: downloadhelper.py
# @time: 2019/6/13 17:33
# @Software: PyCharm


def big_file_download(file_name, file, chunk_size=16 * 2 ** 10):
    """
    从文件里面下载到file_name路径下
    :param file_name: 文件路径
    :param file: uploadfile对象（django对象）
    :param chunk_size: 文件每次处理大小
    :return:
    """

    def file_iterator(file_name, file, chunk_size=chunk_size):
        with open(file_name, 'wb') as f:
            while True:
                c = file.read(chunk_size)
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
