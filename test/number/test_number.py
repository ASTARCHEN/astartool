import unittest

from astartool.number import gcd


class TestNumber(unittest.TestCase):
    def test_gcd(self):
        assert gcd(151200, 362880) == 30240
