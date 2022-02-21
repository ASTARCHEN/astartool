# -*- coding: utf-8 -*-


from astartool.project import get_version



version_tuple = (0, 1, 0, 'alpha', 1)
assert get_version(version_tuple) == '0.1a1'

version_tuple = (0, 1, 1, 'alpha', 1)
assert get_version(version_tuple) == '0.1.1a1'

version_tuple = (0, 1, 0, 'beta', 1)
assert get_version(version_tuple) == '0.1b1'

version_tuple = (0, 1, 3, 'beta', 1)
assert get_version(version_tuple) == '0.1.3b1'

version_tuple = (0, 1, 0, 'rc', 0)
assert get_version(version_tuple) == '0.1rc0'

version_tuple = (0, 1, 4, 'rc', 0)
assert get_version(version_tuple) == '0.1.4rc0'

version_tuple = (0, 1, 0, 'rc', 1)
assert get_version(version_tuple) == '0.1rc1'

version_tuple = (0, 1, 0, 'final', 0)
assert get_version(version_tuple) == '0.1'

version_tuple = (0, 1, 0, 'final', 1)
assert get_version(version_tuple) == '0.1'

version_tuple = (0, 1, 0, 'post', 0)
assert get_version(version_tuple) == '0.1post0'

version_tuple = (0, 1, 0, 'post', 1)
assert get_version(version_tuple) == '0.1post1'

version_tuple = (0, 1, 4, 'post', 0)
assert get_version(version_tuple) == '0.1.4post0'

version_tuple = (0, 1, 5, 'post', 1)
assert get_version(version_tuple) == '0.1.5post1'
