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


class DataNode(object):
    def __init__(self, data=None, pre=None, next=None):
        self.data = data
        self.pre = pre
        self.next = next


class LinkedList:
    def __init__(self, seq=[], flag=True):
        """

        :param seq:  初始化可迭代对象
        :param flag: 若可迭代对象是LinkedList, 那么flag=False, 否则此参数为True
        """
        self.__count = 0
        self.pre = self
        self.next = self
        self.extend(seq)
        

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
        self.__count = 0

    def copy(self):  # real signature unknown; restored from __doc__
        """ L.copy() -> list -- a shallow copy of L """
        return LinkedList(self)

    def count(self, value):  # real signature unknown; restored from __doc__
        """ L.count(value) -> integer -- return number of occurrences of value """
        p = self.next
        s = 0
        while p != self:
            s += p.data == value
            p = p.next
        return s

    def extend(self, iterable, flag=True):
        """
        :param iterable:
        :param flag: 若可迭代对象是LinkedList, 那么flag=False, 否则此参数为True
        :return:
        """
        if flag:
            for each in iterable:
                self.append(each, flag)
        else:
            if not isinstance(iterable, LinkedList):
                raise ValueError('iterable must isinstance of LinkedList')
            self.pre = iterable.pre
            iterable.next = self
            self.__count += iterable.__count

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
        assert abs(index) < self.__count
        if index > 0:
            if index > self.__count // 2:
                index = index - self.__count

        if index > 0:
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
        pass

    def print(self):
        p = self.next
        while p != self:
            print(p.data, '->', end='')
            p = p.next
        print("END")

    #
    # def __add__(self, *args, **kwargs):  # real signature unknown
    #     """ Return self+value. """
    #     pass
    #
    # def __contains__(self, *args, **kwargs):  # real signature unknown
    #     """ Return key in self. """
    #     pass
    #
    # def __delitem__(self, *args, **kwargs):  # real signature unknown
    #     """ Delete self[key]. """
    #     pass
    #
    # def __eq__(self, *args, **kwargs):  # real signature unknown
    #     """ Return self==value. """
    #     # TODO: __eq__
    #     pass
    #
    # def __getattribute__(self, *args, **kwargs):  # real signature unknown
    #     """ Return getattr(self, name). """
    #     pass
    #
    # def __getitem__(self, y):  # real signature unknown; restored from __doc__
    #     """ x.__getitem__(y) <==> x[y] """
    #     pass
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
        pass

    def __imul__(self, *args, **kwargs):  # real signature unknown
        """ Implement self*=value. """
        pass

    def __iter__(self, *args, **kwargs):  # real signature unknown
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs):  # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs):  # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs):  # real signature unknown
        """ Return self<value. """
        pass

    def __mul__(self, *args, **kwargs):  # real signature unknown
        """ Return self*value.n """
        pass
