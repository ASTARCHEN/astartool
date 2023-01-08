# -*- coding: utf-8 -*-
from typing import List

from astartool.data_structure.union_find import UnionFind


class TimestampSynchronization(UnionFind):
    def __init__(self):
        super(TimestampSynchronization, self).__init__()
        self.timedelta = None

    @classmethod
    def init_by_list(cls, dataset: list):
        disjoint_set = TimestampSynchronization()
        disjoint_set.dataset = {i: each for i, each in enumerate(dataset)}
        disjoint_set.parent = [i for i, each in enumerate(dataset)]
        disjoint_set.rank = [1 for _ in dataset]
        disjoint_set.timedelta = [0.0 for _ in dataset]
        return disjoint_set

    def find(self, x):
        # 查找根结点
        if x == self.parent[x]:
            return x, 0.0
        else:
            self.parent[x], delta_t = self.find(self.parent[x])
            self.timedelta[x] += delta_t
            # 路径压缩， 遍历过程中的所有双亲结点直接指向根结点，减少后续查找次数
        return self.parent[x], self.timedelta[x]

    def merge(self, x, y, delta_t=0.0):
        rx, timedelta_x = self.find(x)  # 查找x的根结点，即x所在集合的代表元素
        ry, timedelta_y = self.find(y)

        if rx != ry:  # 如果不是同一个集合
            dt = timedelta_x + delta_t - timedelta_y
            if dt > 0:
                rx, ry, x, y = ry, rx, y, x  # 这里进行交换是为了保证rx的rank大于ry的rank，方便下面合并
                dt = -dt
            elif self.rank[rx] < self.rank[ry]:  # rank大的集合合并rank小的集合
                rx, ry = ry, rx  # 这里进行交换是为了保证rx的rank大于ry的rank，方便下面合并
                dt = -dt
            self.parent[ry] = rx  # rx 合并 ry
            self.timedelta[ry] = dt
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1


def demo_1():
    li = ["v1", "v2", "v3", "v4", "v5"]
    union_find = TimestampSynchronization.init_by_list(li)
    print(union_find.timedelta)
    union_find.merge(0, 1, 1.0)
    print('-'*10)
    print("timedelta:", union_find.timedelta)
    print("parent:", union_find.parent)
    print("rank:", union_find.rank)

    union_find.merge(2, 4, 7.0)
    print('-'*10)
    print("timedelta:", union_find.timedelta)
    print("parent:", union_find.parent)
    print("rank:", union_find.rank)

    union_find.merge(3, 1, -5.0)
    print('-'*10)
    print("timedelta:", union_find.timedelta)
    print("parent:", union_find.parent)
    print("rank:", union_find.rank)

    union_find.merge(4, 0, -10.0)
    print('-'*10)
    print("timedelta:", union_find.timedelta)
    print("parent:", union_find.parent)
    print("rank:", union_find.rank)

    for i in range(5):
        print(union_find.find(i))

    for i in range(5):
        print(union_find.find(i))


if __name__ == '__main__':
    def distance(p1, p2):
        return abs(p1[0] - p2[0]) ** 2 + abs(p1[1] - p2[1]) ** 2
    li = [(1, 0), (2, 2), (1, 0), (10, 20), (10, 21), (11, 19), (0, 0)]
    unifind = UnionFind.init_by_list(li)

    len_list = len(li)
    klass_set = {0}
    for i, p1 in enumerate(li[1:], start=1):
        for j in klass_set:
            p2 = li[j]
            if distance(p1, p2) < 3 * 3:
                unifind.merge(i, j)
                break
        klass_set.add(unifind.find(i))
    print(unifind.parent)
    print(unifind.find(0))
