#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 深圳星河软通科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.astar.ltd
# @file: linked_list .py
# @time: 2020/5/21 17:24
# @Software: PyCharm


# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 深圳星河软通科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.astar.ltd
# @file: _data_structure .py
# @time: 2020/5/18 0:15
# @Software: PyCharm

from collections import Iterable, Sized



class DataNode(object):
    def __init__(self, data=None, pre=None, next=None):
        self.data = data
        self.pre = pre
        self.next = next

    def __eq__(self, other):
        if isinstance(other, DataNode):
            return self.data == other.data
        else:
            return self.data == other

    def __str__(self):
        return self.data

    def __del__(self):
        self.pre = self.next = None
        del self.next
        del self.pre
        del self.data


class LinkedList(Iterable, Sized):
    def __init__(self, seq:Iterable=[], flag=True):
        """

        :param seq:  初始化可迭代对象
        :param flag: 若可迭代对象是LinkedList, 那么flag=False, 否则此参数为True
        """
        self.__count = 0
        self.pre = self
        self.next = self
        self.__p = self
        self.extend(seq, flag=flag)

    def append(self, p_object, flag=True):
        """
        追加函数
        :param p_object:
        :param flag: p_object 是DataNode, 那么flag=False, 否则此参数为True
        :return:
        """
        if flag:
            p_object = DataNode(p_object, None, None)
        self.pre.next = p_object
        p_object.pre = self.pre
        self.pre = p_object
        p_object.next = self
        self.__count += 1

    def clear(self):  # real signature unknown; restored from __doc__
        """ L.clear() -> None -- remove all items from L """
        p = self.next
        while p != self:
            t = p.next
            del p
            p = t
        self.pre = self.next = self
        self.__count = 0

    def copy(self):  # real signature unknown; restored from __doc__
        """ L.copy() -> list -- a shallow copy of L """
        return LinkedList(self, flag=True)

    def count(self, value):  # real signature unknown; restored from __doc__
        """ L.count(value) -> integer -- return number of occurrences of value """
        p = self.next
        s = 0
        while p != self:
            s += p.data == value
            p = p.next
        return s

    def extend(self, iterable:Iterable, flag=True):
        """
        :param iterable:
        :param flag: 若可迭代对象是LinkedList, 那么flag=False, 否则此参数为True
        当flag=flase时候，只修改指针，不会新创建DataNode对象.
        flag=True时候，会创建DataNode对象，显然flag=False更快，但是需要注意此方法需要慎用
        :return:
        """
        if flag:
            for each in iterable:
                self.append(each, flag)
        else:
            if not isinstance(iterable, LinkedList):
                raise ValueError('iterable must isinstance of LinkedList')
            self.pre.next = iterable.next
            iterable.next.pre = self.pre
            self.pre = iterable.pre
            iterable.pre.next = self
            self.__count += iterable.__count
            iterable.next = iterable.pre = iterable
            del iterable

    def index(self, value, start=None, stop=None):  # real signature unknown; restored from __doc__
        """
        L.index(value, [start, [stop]]) -> integer -- return first index of value.
        Raises ValueError if the value is not present.
        """
        # TODO: todo start and stop
        p = self.next
        s = 0
        while p != self:
            if p.data == value:
                return s
            s += 1
            p = p.next
        raise ValueError('value is not present')

    def insert(self, index, p_object, flag=True):
        """
        :param index:
        :param p_object:
        :param flag: 若是DataNode类型, 那么flag=False, 否则此参数为True
        :return:
        """
        p = self.next
        s = 0
        # TODO: index大于所有长度//2的时候反向去查
        while p != self:
            if s == index:
                break
            s += 1
            p = p.next
        if flag:
            p_object = DataNode(p_object)
            p_object.next = p.next
            p_object.pre = p
            p.next = p_object
            p_object.next.pre = p_object
        else:
            p_object.next = p.next
            p_object.pre = p
            p.next = p_object
            p_object.next.pre = p_object
        self.__count += 1

    def pop(self, index=-1):
        assert abs(index) <= self.__count
        if index > 0:
            if index > self.__count // 2:
                index = index - self.__count

        if index >= 0:
            p = self.next
            ind = 0
            while ind < index:
                p = p.next
                ind += 1
            p.pre.next = p.next
            p.next.pre = p.pre
            self.__count -= 1
            return p.data
        else:
            p = self.pre
            ind = 0
            while ind < index:
                p = p.pre
                ind -= 1
            p.pre.next = p.next
            p.next.pre = p.pre
            self.__count -= 1
            return p.data

    def remove(self, value):  # real signature unknown; restored from __doc__
        """
        L.remove(value) -> None -- remove first occurrence of value.
        Raises ValueError if the value is not present.
        """
        p = self.next
        while p != self:
            p = p.next
            if p.data == value:
                p.pre.next = p.next
                p.next.pre = p.pre
                return
        raise ValueError('the value is not present.')

    def reverse(self):  # real signature unknown; restored from __doc__
        """ L.reverse() -- reverse *IN PLACE* """
        p = self.next
        while p != self:
            p.next, p.pre = p.pre, p.next
            p = p.pre
        self.next, self.pre = self.pre, self.next

    def sort(self, key=None, reverse=False):  # real signature unknown; restored from __doc__
        """ L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE* """
        raise Exception("method not found")

    def print(self):
        p = self.next
        while p != self:
            print(p.data, '->', end=' ')
            p = p.next
        print("END")

    def __add__(self, *args, **kwargs):  # real signature unknown
        """ Return self+value. """
        value = args[0]
        if isinstance(value, Sized):
            if len(value) != len(self):
                raise ValueError('error in input')
            c = LinkedList(map(lambda a, b: a + b, self, value))
            return c
        else:
            b = LinkedList(map(lambda a: a + value, self))
            return b

    def __eq__(self, *args, **kwargs):  # real signature unknown
        """ Return self==value. """
        value = args[0]
        if isinstance(value, LinkedList):
            if id(value) == id(self):
                return True
        if isinstance(value, Sized):
            if len(value) != len(self):
                return False
            for a, b in zip(value, self):
                if a != b:
                    return False
            return True
        return False

    def __getitem__(self, y):  # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        if isinstance(y, int):
            if y >= len(self) or y < -len(self):
                raise ValueError("list out of range")
            if y > 0:
                if y > len(self) // 2:
                    y = y - len(self)

            if y >= 0:
                p = self.next
                ind = 0
                while ind < y:
                    p = p.next
                    ind += 1

                return p.data
            else:
                    p = self.pre
                    ind = 0
                    while ind < y:
                        p = p.pre
                        ind -= 1
                    return p.data
        elif isinstance(y, slice):
            raise Exception('method not fount')
        else:
            raise Exception('method not fount')
    #
    # def __ge__(self, *args, **kwargs):  # real signature unknown
    #     """ Return self>=value. """
    #     pass
    #
    # def __gt__(self, *args, **kwargs):  # real signature unknown
    #     """ Return self>value. """
    #     pass

    def __iadd__(self, *args, **kwargs):  # real signature unknown
        """ Implement self+=value. """
        raise Exception("method not found")
        pass

    def __imul__(self, *args, **kwargs):  # real signature unknown
        """ Implement self*=value. """
        raise Exception("method not found")
        pass

    def __len__(self, *args, **kwargs):  # real signature unknown
        """ Return len(self). """
        return self.__count

    def __le__(self, *args, **kwargs):  # real signature unknown
        """ Return self<=value. """
        raise Exception("method not found")
        pass

    def __lt__(self, *args, **kwargs):  # real signature unknown
        """ Return self<value. """
        raise Exception("method not found")
        pass

    def __mul__(self, *args, **kwargs):  # real signature unknown
        """ Return self*value.n """
        raise Exception("method not found")
        pass

    def __next__(self):
        self.__p = self.__p.next
        if self.__p == self:
            raise StopIteration
        else:
            return self.__p.data

    def __iter__(self):
        return self

    def __del__(self):
        p = self.next
        while p != self:
            t = p.next
            del p
            p = t
        del p
