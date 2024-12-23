#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 河北雪域网络科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.snowland.ltd
# @file: common.py
# @time: 2019/5/29 11:41
# @Software: PyCharm


__author__ = 'A.Star'

import datetime
from decimal import Decimal
from enum import Enum
import logging
from astartool.data_structure.keymap import KeyMap

hex_string = '0123456789abcdef'
hex_string_upper = '0123456789ABCDFEF'
alnum_string = '0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
alpha_string = 'qwertyuiopasdfghjklzxcvbnm'
digit_string = '0123456789'
password_allowed_string = '1234567890qwertyuiopasdfghjklzxcvbnm!@#$%^*()'
password_allowed_string_upper = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^*()'
hex_allowed_string = '0123456789ABCDEFabcdef'

BIT_BLOCK_H = [0x00, 0x80, 0xC0, 0xE0, 0xF0, 0xF8, 0xFC, 0xFE, 0xFF]
BIT_BLOCK_L = [0x00, 0x01, 0x03, 0x07, 0x0F, 0x1F, 0x3F, 0x7F, 0xFF]
BIT_EACH = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288,
            1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912,
            1073741824, 2147483648, 4294967296, 8589934592, 17179869184, 34359738368, 68719476736, 137438953472,
            274877906944, 549755813888, 1099511627776, 2199023255552, 4398046511104, 8796093022208, 17592186044416,
            35184372088832, 70368744177664, 140737488355328, 281474976710656, 562949953421312, 1125899906842624,
            2251799813685248, 4503599627370496, 9007199254740992, 18014398509481984, 36028797018963968,
            72057594037927936, 144115188075855872, 288230376151711744, 576460752303423488, 1152921504606846976,
            2305843009213693952, 4611686018427387904, 9223372036854775808, 18446744073709551616, 36893488147419103232,
            73786976294838206464, 147573952589676412928, 295147905179352825856, 590295810358705651712,
            1180591620717411303424, 2361183241434822606848, 4722366482869645213696, 9444732965739290427392,
            18889465931478580854784, 37778931862957161709568, 75557863725914323419136, 151115727451828646838272,
            302231454903657293676544, 604462909807314587353088, 1208925819614629174706176, 2417851639229258349412352,
            4835703278458516698824704, 9671406556917033397649408, 19342813113834066795298816,
            38685626227668133590597632, 77371252455336267181195264, 154742504910672534362390528,
            309485009821345068724781056, 618970019642690137449562112, 1237940039285380274899124224,
            2475880078570760549798248448, 4951760157141521099596496896, 9903520314283042199192993792,
            19807040628566084398385987584, 39614081257132168796771975168, 79228162514264337593543950336,
            158456325028528675187087900672, 316912650057057350374175801344, 633825300114114700748351602688,
            1267650600228229401496703205376, 2535301200456458802993406410752, 5070602400912917605986812821504,
            10141204801825835211973625643008, 20282409603651670423947251286016, 40564819207303340847894502572032,
            81129638414606681695789005144064, 162259276829213363391578010288128, 324518553658426726783156020576256,
            649037107316853453566312041152512, 1298074214633706907132624082305024, 2596148429267413814265248164610048,
            5192296858534827628530496329220096, 10384593717069655257060992658440192,
            20769187434139310514121985316880384, 41538374868278621028243970633760768,
            83076749736557242056487941267521536, 166153499473114484112975882535043072,
            332306998946228968225951765070086144, 664613997892457936451903530140172288,
            1329227995784915872903807060280344576, 2658455991569831745807614120560689152,
            5316911983139663491615228241121378304, 10633823966279326983230456482242756608,
            21267647932558653966460912964485513216, 42535295865117307932921825928971026432,
            85070591730234615865843651857942052864, 170141183460469231731687303715884105728]

list_allow_extension = [
    '.py',
    '.jl',
    '.m',
    '.js',
    '.java',
    '.xml',
    '.html',
    '.htm',
    '.css',
    '.txt',
    '.cs',
    '.cpp',
    '.c',
    '.h',
    '.php'
]
list_ignore = [
    '.git',
    '.gitignore',
    '__pycache__/'
    '*.py[cod]',
    # '*$py.class',
    '*.so',
    '.Python'
    'build/',
    'develop-eggs/',
    'dist/',
    'downloads/',
    'eggs/',
    '.eggs/',
    'lib/',
    'lib64/',
    'parts/',
    'sdist/',
    'var/',
    'wheels/',
    '*.egg-info/',
    '.installed.cfg',
    '*.egg',
    'MANIFEST',
    '*.manifest',
    '*.spec',
    'pip-log.txt',
    'pip-delete-this-directory.txt',
    'htmlcov/',
    '.tox/',
    '.coverage',
    '.coverage.*',
    '.cache',
    'nosetests.xml',
    'coverage.xml',
    '*.cover',
    '.hypothesis/',
    '*.mo',
    '*.pot',
    '*.log',
    '.static_storage/',
    '.media/',
    'local_settings.py',
    'instance/',
    '.webassets-cache',
    '.scrapy',
    'docs/_build/',
    'target/',
    '.ipynb_checkpoints',
    '.python-version',
    'celerybeat-schedule',
    '.env',
    '.venv',
    'env/',
    'venv/',
    'ENV/',
    'env.bak/',
    'venv.bak/',
    '.spyderproject',
    '.spyproject',
    '.ropeproject',
    '/site',
    '.mypy_cache/',
    '.idea/'
]

map_field_to_ = KeyMap({
    'CharField': 'varchar',
    'TextField': 'text',
    'IntegerField': 'int',
    'FloatField': 'float',
    'DateTimeField': 'datetime',
    'DateField': 'date',
    'ForeignKey': '外键',
    # '':
})

item_field = [
    'verbose_name',
]
item_foreignkey = [
    'model', 'related_name', 'on_delete'
]


class ErrorCode(Enum):
    ERROR_CODE_UNKNOWN = -1  # 未知错误
    ERROR_CODE_OPERATION_SUCCESS = 0  # 操作成功
    ERROR_CODE_OPERATION_FAILED = 1  # 操作失败
    ERROR_CODE_PARTNER_ERROR = 2  # 参数有误
    ERROR_CODE_TOKEN_ERROR = 3  # token失效
    ERROR_CODE_DATABASE_ERROR = 4  # 数据库错误
    ERROR_CODE_LOGINED_ERROR = 5  # 该账户已在其他设备登录，已退出
    ERROR_CODE_ACCOUNT_LOCKED_ERROR = 6  # 账户被锁定、禁用|
    ERROR_CODE_IP_TRY_TIME_LIMITED_ERROR = 7  # 同一终端登录失败次数超过限制|
    ERROR_CODE_ACCOUNT_TRY_TIME_LIMITED_ERROR = 8  # 同一账户登录失败次数超过限制
    ERROR_CODE_USER_NOT_FOUND = 9  # 无此用户
    ERROR_CODE_PERMISSION_ERROR = 10  # 无用户权限
    ERROR_CODE_SERVER_ERROR = 99  # 后台处于维护状态|


LOG_LEVEL_STR = ['INFO', 'WARN', 'WARNING', 'ERROR', 'NOTSET', 'DEBUG', 'FATAL', 'CRITICAL']
LOG_LEVEL_INT = [logging.INFO, logging.WARN, logging.WARNING, logging.ERROR, logging.NOTSET, logging.DEBUG,
                 logging.FATAL, logging.CRITICAL]

LOG_LEVEL_MAP_STR2INT = {
    'INFO': logging.INFO,
    'WARN': logging.WARN,
    'WARNING': logging.WARN,
    'ERROR': logging.ERROR,
    'NOTSET': logging.NOTSET,
    'DEBUG': logging.DEBUG,
    'FATAL': logging.FATAL,
    'CRITICAL': logging.CRITICAL
}

LOG_LEVEL_MAP_INT2STR = {
    logging.INFO: 'INFO',
    logging.WARN: 'WARN',
    logging.ERROR: 'ERROR',
    logging.NOTSET: 'NOTSET',
    logging.DEBUG: 'DEBUG',
    logging.FATAL: 'FATAL',
}

_PROTECTED_TYPES = (
    type(None), int, float, Decimal, datetime.datetime, datetime.date, datetime.time,
)
