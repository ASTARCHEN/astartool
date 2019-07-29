import os
import zipfile

import rarfile
from pysmx.crypto import hashlib


def CalcSha1(filepath, encoding='utf-8'):
    """
    计算文件SHA1
    :param filepath:
    :param encoding:
    :return:
    """
    with open(filepath, 'rb', encoding=encoding) as f:
        sha1obj = hashlib.sha1()
        sha1obj.update(f.read())
        hash = sha1obj.hexdigest()
        return hash


def CalcMD5(filepath, encoding='utf-8'):
    """
    计算文件MD5
    :param filepath:
    :return:
    """
    with open(filepath, 'rb', encoding=encoding) as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash = md5obj.hexdigest()
        return hash


def CalcSM3(filepath, encoding='utf-8'):
    with open(filepath, 'rb', encoding=encoding) as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash = md5obj.hexdigest()
        return hash


alg_map = {
    "md5": CalcMD5,
    "sm3": CalcSM3,
    "sha1": CalcSha1
}


def CalcHash(filepath, algorithm='md5', encoding='utf-8'):
    return alg_map[algorithm.lower()](filepath, encoding=encoding)


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


def rename(filepath, method='sha1', encoding='utf-8'):
    """
    通过加sha的方式重新命名文件
    :param filepath:
    :return:
    """
    splitext = os.path.splitext(filepath)
    f = alg_map.get(method.lower(), CalcSha1)
    hash = f(filepath, encoding=encoding)
    new_name = method + '_' + str(splitext[0]) + '_' + hash + splitext[-1]
    return new_name
