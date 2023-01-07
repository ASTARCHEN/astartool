# -*- coding: utf-8 -*-


from astartool.data_structure.heap import Heap


class Student:
    def __init__(self, no, c1, c2, c3):
        self.no = no
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3

    @property
    def sum(self):
        return self.c1 + self.c2 + self.c3

    def __lt__(self, other):
        return self.no < other.no

    def __str__(self):
        return "Student<{}>".format(self.no)

    def __repr__(self):
        return "Student<{}>".format(self.no)


heap = Heap()

heap.heappush(Student(1, 80, 85, 90))
heap.heappush(Student(2, 76, 90, 75))
heap.heappush(Student(3, 70, 88, 97))
heap.heappush(Student(4, 73, 92, 75))

print("students:", heap.func_seq)
heap.heapify(lambda x: x.sum)
print("new heap:", heap.func_seq)

s = heap.heappop()

print("type:", isinstance(s, Student))
print(s)
