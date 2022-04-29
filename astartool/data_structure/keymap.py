#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 深圳星河软通科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.astar.ltd
# @file: keymap .py
# @time: 2020/9/5 19:06
# @Software: PyCharm


from collections import Iterable, Sized


class KeyMap(Iterable, Sized):
    def __init__(self, seq: Iterable = [], *args, **kwargs):
        self._map = dict()
        if isinstance(seq, dict):
            self._map = seq
        else:
            self._map = dict(seq)
        self._rev_map = {v: k for k, v in self._map.items()}

    def __len__(self):
        return len(self._map)

    def __iter__(self):
        return iter(self._map)

    def __contains__(self, item):
        return item in self._map or item in self._rev_map

    def __getitem__(self, y):
        if y in self._map:
            return self._map[y]
        if y in self._rev_map:
            return self._rev_map[y]
        raise ValueError('y not in _map or _rev_map')

    def map_to_list(self):
        return [(k, v) for k, v in self._map.items()]

    def reverse_map_to_list(self):
        return [(k, v) for k, v in self._rev_map.items()]

    def get(self, k, default=None):
        if k in self._map:
            return self._map[k]
        if k in self._rev_map:
            return self._rev_map[k]
        return default