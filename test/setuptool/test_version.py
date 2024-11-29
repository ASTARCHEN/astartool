import unittest

from astartool.setuptool import get_version, get_complete_version


class TestGetVersion(unittest.TestCase):
    def test_010a1(self):
        version_tuple = (0, 1, 0, 'alpha', 1)
        self.assertEqual('0.1a1', get_version(version_tuple))

    def test_011a1(self):
        version_tuple = (0, 1, 1, 'alpha', 1)
        self.assertEqual('0.1.1a1', get_version(version_tuple))

    def test_01b1(self):
        version_tuple = (0, 1, 0, 'beta', 1)
        self.assertEqual('0.1b1', get_version(version_tuple))

    def test_013b1(self):
        version_tuple = (0, 1, 3, 'beta', 1)
        self.assertEqual('0.1.3b1', get_version(version_tuple))

    def test_010rc0(self):
        version_tuple = (0, 1, 0, 'rc', 0)
        self.assertEqual('0.1rc0', get_version(version_tuple))

    def test_014rc0(self):
        version_tuple = (0, 1, 4, 'rc', 0)
        self.assertEqual('0.1.4rc0', get_version(version_tuple))

    def test_010rc1(self):
        version_tuple = (0, 1, 0, 'rc', 1)
        self.assertEqual('0.1rc1', get_version(version_tuple))

    def test_01_0(self):
        version_tuple = (0, 1, 0, 'final', 0)
        self.assertEqual('0.1', get_version(version_tuple))

    def test_01_1(self):
        version_tuple = (0, 1, 0, 'final', 1)
        self.assertEqual('0.1', get_version(version_tuple))

    def test_10(self):
        version_tuple = (1, 0, 0, 'final', 0)
        self.assertEqual('1.0', get_version(version_tuple))

    def test01post0(self):
        version_tuple = (0, 1, 0, 'post', 0)
        self.assertEqual('0.1post0', get_version(version_tuple))

    def test01post1(self):
        version_tuple = (0, 1, 0, 'post', 1)
        self.assertEqual('0.1post1', get_version(version_tuple))

    def test01dev0(self):
        version_tuple = (0, 1, 0, 'dev', 0)
        self.assertEqual('0.1dev0', get_version(version_tuple))

    def test01dev1(self):
        version_tuple = (0, 1, 0, 'dev', 1)
        self.assertEqual('0.1dev1', get_version(version_tuple))


class TestGetCompleteVersion(unittest.TestCase):
    def test_01(self):
        version_tuple = (0, 1, 0, 'final', 0)
        short_version_tuple = (0, 1)
        self.assertEqual(version_tuple, get_complete_version(short_version_tuple))

    def test_10(self):
        version_tuple = (1, 0, 0, 'alpha', 1)
        short_version_tuple = (1, 0, 'alpha', 1)
        self.assertEqual(version_tuple, get_complete_version(short_version_tuple))
