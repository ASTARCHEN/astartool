from astartool.setuptool import PY310

if PY310:
    from collections.abc import MutableMapping
else:
    from collections import MutableMapping
from functools import reduce

from astartool.data_structure.lazymap import LazyMap, MutableLazyMap


class MergeMap(MutableMapping):
    def __init__(self, values={}):
        super().__init__()
        self.__inner = MutableLazyMap(values)
        self.maps = []
        self.__keys = set()

    def __len__(self):
        return len(self.__inner)

    def __iter__(self):
        return iter(self.__inner.values)

    def __getitem__(self, key):
        return self.__inner.get(key)

    def __contains__(self, key):
        return key in self.__keys

    def __setitem__(self, key, value):
        return self.__inner.__setitem__(key, value)

    def __delitem__(self, key):
        return self.__inner.__delitem__(key)

    def __str__(self):
        return str(self.__inner.values)

    def __repr__(self):
        return "MergeMap({0})".format(repr(self.values))

    def merge(self, *args, **kwargs):
        new_keys = set()
        new_items = []
        for each in args:
            assert isinstance(each, MutableMapping)
            new_items.extend(each.items())
            new_keys.update(each.keys())

        new_items.extend(kwargs.items())
        new_keys.update(kwargs.keys())
        intersection = new_keys.intersection(self.__inner.keys())
        new_items.extend((k, self.__inner[k]) for k in intersection)
        self.maps.extend(new_items)
        self.__keys.update(new_keys)
        for k in new_keys:
            self.__inner[k] = lambda s: reduce(self.add, filter(lambda x: x[0] == k, self.maps))

    def add(self, a, b):
        return a[1] + b[1]
