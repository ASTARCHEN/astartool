#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 深圳星河软通科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.astar.ltd
# @file: linked_list .py
# @time: 2020/5/21 17:24
# @Software: PyCharm


from collections import Iterable, Sized
from astartool.error import MethodNotFoundError, ParameterValueError


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
    def __init__(self, seq: Iterable = [], flag=True):
        """

        :param seq:  初始化可迭代对象
        :param flag: 若可迭代对象是LinkedList, 那么flag=False, 否则此参数为True
        """
        self.__count = 0
        self.pre = self
        self.next = self
        self.__p = Pointer(self)
        self.extend(seq, flag=flag)
        self.__p = Pointer(self)

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
        p = Pointer(self)
        s = 0
        while p.has_next():
            s += (p.data == value)
            p.next()
        return s

    def extend(self, iterable: Iterable, flag=True):
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
                for each in iterable:
                    self.append(each, flag)
                return
            self.pre.next = iterable.next
            iterable.next.pre = self.pre
            self.pre = iterable.pre
            iterable.pre.next = self
            self.__count += iterable.__count
            iterable.next = iterable.pre = iterable
            del iterable
        self.__p = Pointer(self)

    def index(self, value, start=None, stop=None):  # real signature unknown; restored from __doc__
        """
        L.index(value, [start, [stop]]) -> integer -- return first index of value.
        Raises ValueError if the value is not present.
        """
        # TODO: todo start and stop
        p = Pointer(self)
        s = 0
        while not p.is_last():
            if p.data == value:
                return s
            s += 1
            p.next()
        raise ValueError('value is not present')

    def insert(self, index, p_object, flag=True):
        """
        :param index:
        :param p_object:
        :param flag: 若是DataNode类型, 那么flag=False, 否则此参数为True
        :return:
        """
        p = Pointer(self)
        p.next()
        s = 0
        # TODO: index大于所有长度//2的时候反向去查
        while p.is_last():
            if s == index:
                break
            s += 1
            p.next()
        if flag:
            p_object = DataNode(p_object)
            p_object.next = p.datanode.next
            p_object.pre = p.datanode
            p.datanode.next = p_object
            p_object.next.pre = p_object
        else:
            p_object.next = p.datanode.next
            p_object.pre = p.datanode
            p.datanode.next = p_object
            p_object.next.pre = p_object
        self.__count += 1

    def pop(self, index=-1):
        if abs(index) <= self.__count:
            pass
        else:
            raise IndexError('index not found')
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
        raise MethodNotFoundError("method not found")

    def print(self):
        self.__p.next()
        while not self.__p.is_last():
            print(self.__p.data, '->', end=' ')
            self.__p.next()
        print("END")
        self.__p = Pointer(self)

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
                raise ParameterValueError("list out of range")
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
            step = 1 if y.step is None else y.step
            if step > 0:
                if y.start is None:
                    start = 0
                elif y.start < 0:
                    start = len(self) + y.start
                else:
                    start = y.start

                if y.stop is None:
                    stop = len(self)
                elif y.stop < 0:
                    stop = len(self) + y.stop
                else:
                    stop = y.stop
            else:
                if y.start is None:
                    start = len(self) - 1
                elif y.start < 0:
                    # TODO: check it
                    start = len(self) + y.start
                else:
                    start = y.start

                if y.stop is None:
                    stop = -1
                elif y.stop < 0:
                    # TODO: check it
                    stop = len(self) + y.stop
                else:
                    stop = y.stop
            p = Pointer(self) + start + 1
            li = LinkedList()
            for i in range(start, stop, step):
                li.append(p.datanode.data)
                p += step
                if p.is_last():
                    break
            return li
        else:
            raise MethodNotFoundError('method not fount')

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
        raise MethodNotFoundError("method not found")

    def __imul__(self, *args, **kwargs):  # real signature unknown
        """ Implement self*=value. """
        raise MethodNotFoundError("method not found")

    def __len__(self, *args, **kwargs):  # real signature unknown
        """ Return len(self). """
        return self.__count

    def __le__(self, *args, **kwargs):  # real signature unknown
        """ Return self<=value. """
        raise MethodNotFoundError("method not found")

    def __lt__(self, *args, **kwargs):  # real signature unknown
        """ Return self<value. """
        raise MethodNotFoundError("method not found")

    def __mul__(self, *args, **kwargs):  # real signature unknown
        """ Return self*value.n """
        raise MethodNotFoundError("method not found")

    def __next__(self):
        self.__p.next()
        if self.__p.is_last():
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


class Pointer:
    def __init__(self, data_node: (DataNode, LinkedList)):
        self.__p = data_node

    def __add__(self, other):
        p = self
        if isinstance(other, int) and other > 0:
            for _ in range(other):
                if p.has_next():
                    p.next()
                else:
                    # warnings.warn('has no next')
                    p.next()
                    break
            return p
        elif other < 0:
            return self + (-other)
        else:
            return p

    def __sub__(self, other):
        p = self
        if other > 0:
            for _ in range(other):
                if p.has_pre():
                    p.pre()
                else:
                    # warnings.warn('has no next')
                    p.pre()
                    break
            return p
        elif other < 0:
            return self + (-other)
        else:
            return p

    def __iadd__(self, other):
        if isinstance(other, int):
            if other > 0:
                for _ in range(other):
                    if self.has_next():
                        self.next()
                    else:
                        # warnings.warn('has no next')
                        self.next()
                        break
                return self
            else:
                return self.__isub__(-other)
        raise ValueError("other must > 0")

    def __isub__(self, other):
        if isinstance(other, int):
            if other > 0:
                for _ in range(other):
                    if self.has_pre():
                        self.pre()
                    else:
                        # warnings.warn('has no pre')
                        self.pre()
                        break
                return self
            else:
                return self.__iadd__(-other)
        raise ValueError("other must > 0")

    def has_next(self):
        return isinstance(self.__p.next, DataNode)

    def has_pre(self):
        return isinstance(self.__p.pre, DataNode)

    def is_last(self):
        return isinstance(self.__p, LinkedList)

    def next(self):
        self.__p = self.__p.next

    def pre(self):
        self.__p = self.__p.pre

    @property
    def data(self):
        try:
            return self.__p.data
        except:
            raise ValueError('LinkedList has no data')

    @property
    def datanode(self):
        return self.__p
