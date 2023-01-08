# -*- coding: utf-8 -*-
from typing import List, Dict


class UnionFind:
    """
    并查集
    """

    def __init__(self, parent=None, rank=None, dataset=None):
        # 所有根结点相同的结点位于同一个集合中
        self.parent: List[int] = parent if parent else []  # 双亲结点数组，记录该结点的双亲结点，用于查找该结点的根结点
        self.rank: list = rank if rank else []  # 秩数组，记录以该结点为根结点的树的深度，主要用于优化，在合并两个集合的时候，rank大的集合合并rank小的集合
        self.dataset = {i: i for i, _ in enumerate(self.parent)} if dataset is None else dataset

    @classmethod
    def init_by_list(cls, dataset: list):
        disjoint_set = UnionFind()
        disjoint_set.dataset = {i: each for i, each in enumerate(dataset)}
        disjoint_set.parent = [i for i, each in enumerate(dataset)]
        disjoint_set.rank = [1 for _ in dataset]
        return disjoint_set

    def find(self, x):
        """查找根结点"""
        if x == self.parent[x]:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])  # 路径压缩， 遍历过程中的所有双亲结点直接指向根结点，减少后续查找次数
        return self.parent[x]

    def merge(self, x, y):
        """合并节点"""
        rx = self.find(x)  # 查找x的根结点，即x所在集合的代表元素
        ry = self.find(y)

        if rx != ry:  # 如果不是同一个集合
            if self.rank[rx] < self.rank[ry]:  # rank大的集合合并rank小的集合
                rx, ry = ry, rx  # 这里进行交换是为了保证rx的rank大于ry的rank，方便下面合并
        self.parent[ry] = rx  # rx 合并 ry
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1

    @property
    def classes(self):
        """
        获得当前的所有类号
        """
        return set(i for i, each in enumerate(self.parent) if each == i)

    def get_groups(self) -> Dict[int, List]:
        """
        获得类字典, 键代表类号， 值为列表
        """
        classes = self.classes
        groups = {klass: [] for klass in classes}
        for i, each in self.dataset.items():
            groups[self.find(i)].append(each)
        return groups

    def get_group(self, x) -> List:
        """
        获取与x编号相同的所有元素
        """
        root = self.find(x)
        return [v for k, v in self.dataset.items() if self.find(k) == root]
