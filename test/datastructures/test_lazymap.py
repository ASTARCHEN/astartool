from unittest import TestCase
from astartool.data_structure.lazymap import LazyMap
from astartool.error.lazydict_error import CircularReferenceError, ConstantRedefinitionError


class TestLazyDictionary(TestCase):

    def test_circular_reference_error(self):
        d = LazyMap()
        d['foo'] = lambda s: s['foo']
        self.assertRaises(CircularReferenceError, d.__getitem__, 'foo')

    def test_constant_redefinition_error(self):
        d = LazyMap()
        d['a'] = 1
        d['b'] = 2
        d['sum'] = lambda s: s['a'] + s['b']
        x = d['sum']
        self.assertRaises(ConstantRedefinitionError, d.__setitem__, 'a', 'hotdog')
        self.assertRaises(ConstantRedefinitionError, d.__delitem__, 'a')

    def test_lazy_evaluation(self):
        d = LazyMap()
        d['sum'] = lambda s: s['a'] + s['b']
        d['a'] = 1
        d['b'] = 2
        self.assertEqual(d['sum'], 3)

    def test_str(self):
        d = LazyMap({'a': {'b': 1}})
        self.assertEqual(str(d), "{'a': {'b': 1}}")

    def test_repr(self):
        d = LazyMap({'a': {'b': 1}})
        self.assertEqual(repr(d), "LazyDictionary({'a': {'b': 1}})")

    def test_atomic_evaluation(self):
        d = LazyMap()
        d['division'] = lambda: 1 / 0
        self.assertEqual(d.states['division'], 'defined')
        self.assertRaises(ZeroDivisionError, d.__getitem__, 'division')
        # second call checks lazydict.CircularReferenceError is not raised.
        self.assertRaises(ZeroDivisionError, d.__getitem__, 'division')
        self.assertEqual(d.states['division'], 'error')
