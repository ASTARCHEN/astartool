#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 深圳星河软通科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.astar.ltd
# @file: queue .py
# @time: 2020/6/11 3:39
# @Software: PyCharm


from queue import Queue
from astartool.data_structure.linked_list import LinkedList

class LinkedQueue(Queue):
    """
    链式结构实现的队列
    """
    def __init__(self, maxsize=0):
        super(LinkedQueue, self).__init__(maxsize)

    def _init(self, maxsize):
        self.queue = LinkedList()

    def _get(self):
        return self.queue.pop(0)

    def clear(self):
        with self.mutex:
            self.queue.clear()
