# -*- coding: utf-8 -*-

from astartool.setuptool import load_install_requires


if __name__ == '__main__':
    print(load_install_requires(r"..\requirements.txt"))
    print(load_install_requires(r"..\requirements-doc.txt"))
