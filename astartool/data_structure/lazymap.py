
from astartool.setuptool import PY310
if PY310:
    from collections.abc import MutableMapping
else:
    from collections import MutableMapping

from threading import RLock
import inspect
from copy import copy

from astartool.error.lazydict_error import ConstantRedefinitionError, CircularReferenceError

CONSTANT = frozenset(['evaluating', 'evaluated', 'error'])


# see also https://github.com/janrain/lazydict


class LazyMap(MutableMapping):
    def __init__(self, values={}):
        self.lock = RLock()
        self.values = copy(values)
        self.states = {}
        for key in self.values:
            self.states[key] = 'defined'

    def __len__(self):
        return len(self.values)

    def __iter__(self):
        return iter(self.values)

    def __getitem__(self, key):
        with self.lock:
            if key in self.states:
                if self.states[key] == 'evaluating':
                    raise CircularReferenceError('value of "%s" depends on itself' % key)
                elif self.states[key] == 'error':
                    raise self.values[key]
                elif self.states[key] == 'defined':
                    value = self.values[key]
                    if callable(value):
                        try:
                            full_arg_spec = inspect.getfullargspec(value)
                            args = full_arg_spec[0]
                        except:
                            args, _, _, _ = inspect.getargspec(value)

                        if len(args) == 0:
                            self.states[key] = 'evaluating'
                            try:
                                self.values[key] = value()
                            except Exception as ex:
                                self.values[key] = ex
                                self.states[key] = 'error'
                                raise ex
                        elif len(args) == 1:
                            self.states[key] = 'evaluating'
                            try:
                                self.values[key] = value(self)
                            except Exception as ex:
                                self.values[key] = ex
                                self.states[key] = 'error'
                                raise ex
                    self.states[key] = 'evaluated'
            return self.values[key]

    def __contains__(self, key):
        return key in self.values

    def __setitem__(self, key, value):
        with self.lock:
            if self.states.get(key) in CONSTANT:
                raise ConstantRedefinitionError('"%s" is immutable' % key)
            self.values[key] = value
            self.states[key] = 'defined'

    def __delitem__(self, key):
        with self.lock:
            if self.states.get(key) in CONSTANT:
                raise ConstantRedefinitionError('"%s" is immutable' % key)
            del self.values[key]
            del self.states[key]

    def __str__(self):
        return str(self.values)

    def __repr__(self):
        return "LazyMap({0})".format(repr(self.values))


class MutableLazyMap(LazyMap):
    def __setitem__(self, key, value):
        with self.lock:
            self.values[key] = value
            self.states[key] = 'defined'

    def __delitem__(self, key):
        with self.lock:
            del self.values[key]
            del self.states[key]
