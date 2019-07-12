import hashlib
import os
import zipfile

import rarfile
from pysmx.SM3 import Hash_sm3


def CalcSha1(filepath):
    """
    计算文件SHA1
    :param filepath:
    :return:
    """
    with open(filepath, 'rb') as f:
        sha1obj = hashlib.sha1()
        sha1obj.update(f.read())
        hash = sha1obj.hexdigest()
        return hash


def CalcMD5(filepath):
    """
    计算文件MD5
    :param filepath:
    :return:
    """
    with open(filepath, 'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash = md5obj.hexdigest()
        return hash


def CalcSM3(filepath):
    with open(filepath, 'rb') as f:
        hash = Hash_sm3(f.read())
    return hash


alg_map = {
    "md5": CalcMD5,
    "sm3": CalcSM3,
    "sha1": CalcSha1
}


def CalcHash(filepath, algorithm='md5'):
    return alg_map[algorithm.lower()](filepath)


def file_extension(path):
    """
    文件扩展名
    :param path:
    :return:
    """
    return os.path.splitext(path)[1]


def namelist(filepath):
    """
    zip/rar文件名列表
    :param filepath:
    :return:
    """
    extension = file_extension(filepath)
    if extension.lower() == '.zip':
        z = zipfile.ZipFile(filepath, "r")
        # 打印zip文件中的文件列表
        return z.namelist()
    elif extension.lower() == '.rar':
        z = rarfile.RarFile(filepath, "r")
        # 打印zip文件中的文件列表
        return z.namelist()
    else:
        filepath, tempfilename = os.path.split(filepath)
        return [tempfilename]


def get_file_name(filepath):
    """
    通过文件路径获得文件名(无论路径是否真正存在对应的文件)
    :param filepath:
    :return:
    """
    strsplit = str(filepath).split('/')
    filename = strsplit[-1]
    return filename


def rename(filepath, method='sha1'):
    """
    通过加sha的方式重新命名文件
    :param filepath:
    :return:
    """
    splitext = os.path.splitext(filepath)
    f = alg_map.get(method.lower(), CalcSha1)
    hash = f(filepath)
    new_name = method + '_' + str(splitext[0]) + '_' + hash + splitext[-1]
    return new_name


if __name__ == '__main__':
    s = 'E:\\cxl\\codes\\python\\astardownload\\astardownload\\util\\filehelper.py'
    import time

    a = time.clock()
    print(CalcMD5(s))
    b = time.clock()
    print(CalcSM3(s))
    c = time.clock()
    print(CalcSha1(s))
    d = time.clock()
    print(b - a)
    print(c - b)
    print(d - c)
