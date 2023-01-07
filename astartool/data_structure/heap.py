# -*- coding: utf-8 -*-

import heapq


class Heap:
    def __init__(self, seq=[], func=lambda x: x):
        self.func = func
        self.func_seq = [(func(each), each) for each in seq]
        heapq.heapify(self.func_seq)

    def heappop(self):
        item = heapq.heappop(self.func_seq)
        return item[1]

    def nlargest(self, n, key=None):
        largest = heapq.nlargest(n, self.func_seq, key)
        return [l[1] for l in largest]

    def nsmallest(self, n, key=None):
        smallest = heapq.nsmallest(n, self.func_seq, key)
        return [l[1] for l in smallest]

    def heapreplace(self, item):
        return heapq.heapreplace(self.func_seq, (self.func(item), item))

    def heappush(self, item):
        return heapq.heappush(self.func_seq, (self.func(item), item))

    def heappushpop(self, item):
        return heapq.heappushpop(self.func_seq, (self.func(item), item))

    def merge(self, key=None, reverse=False):
        return heapq.merge(self.func_seq, key, reverse)

    def heapify(self, func=lambda x: x):
        self.func = func
        self.func_seq = [(func(each[1]), each[1]) for each in self.func_seq]
        return heapq.heapify(self.func_seq)
