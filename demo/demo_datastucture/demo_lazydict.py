# -*- coding: utf-8 -*-
from typing import List
from collections import Counter
from astartool.data_structure.mergemap import MergeMap

a = {
    1: [1],
    2: [2, 3],
    3: [4, 5, 6]
}

b = {
    1: [1],
    2: [2, 3],
    3: [4, 5, 6]
}

counter_a = Counter(a)
counter_b = Counter(b)

print("counter_a:", counter_a)
print("counter_b:", counter_b)

merge_map = MergeMap(counter_a)

merge_map.merge(counter_b)

print("merge_map:", merge_map)
print(max(merge_map.values()))
