# -*- coding: utf-8 -*-
import bisect as sys_bisect
import time
from random import randrange

from astartool.data_structure import bisect as this_bisect


class Student:
    def __init__(self, no):
        self.no = no


class Student2:
    def __init__(self, no):
        self.no = no

    def __lt__(self, other):
        return self.no < other.no


students = [Student(i) for i in range(10000)]
students2 = [Student2(i) for i in range(10000)]

k = 10000
keys = [randrange(-1, 100001) for i in range(k)]
students_keys = [Student(each) for each in keys]
students2_keys = [Student2(each) for each in keys]


def sys_bisect_func(a, x, lo=0, hi=None, func=None, resort=False):
    if hi is None:
        hi = len(a)
    if func is None:
        return bisect.bisect(a, x, lo, hi)
    a_new = [func(e) for e in a]
    if resort:
        a_new = sorted(a_new)
    return bisect.bisect(a_new, func(x), lo, hi)


t1 = time.time()
ind_sys_1 = [sys_bisect_func(students, k, func=lambda x: x.no) for k in students_keys]  # ERROR
t2 = time.time()
ind_sys_2 = [sys_bisect.bisect(students2, key) for key in students2_keys]
t3 = time.time()
ind_this_1 = [this_bisect.bisect(students, key, func=lambda x: x.no) for key in students_keys]
t4 = time.time()
ind_this_2 = [this_bisect.bisect(students2, key) for key in students2_keys]
t5 = time.time()

assert ind_this_1 == ind_this_2
assert ind_this_2 == ind_sys_2

print("sys 1:", t2 - t1)
print("sys 2:", t3 - t2)
print("this 1:", t4 - t3)
print("this 2:", t5 - t4)
