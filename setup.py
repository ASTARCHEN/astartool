#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : 河北雪域网络科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.snowland.ltd
# @file: setup.py
# @time: 2018/9/8 1:31
# @Software: PyCharm
import os
from setuptools import find_packages
from astartool import version
from astartool.setuptool import load_install_requires, get_version, setup, read_file

osp = os.path


# def read_file(file_name='README.md', encoding='utf-8'):
#     """
#     读取本地文件
#     :param file_name: 文件名
#     :param encoding: 文件编码，默认utf-8
#     :return:
#     """
#     return open(osp.join(osp.dirname(__file__), file_name), 'r', encoding=encoding).read()


setup(
    name='astartool',
    version=get_version(version),
    description=(
        'toolkit for python'
    ),
    long_description=read_file('description.rst', encoding='utf-8'),
    author='A.Star',
    author_email='astar@snowland.ltd',
    maintainer='A.Star',
    maintainer_email='astar@snowland.ltd',
    license='Apache v2.0',
    packages=find_packages(),
    platforms=["all"],
    url='https://gitee.com/hoops/astartool',
    classifiers=[
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries'
    ],
    install_requires=load_install_requires()
)
