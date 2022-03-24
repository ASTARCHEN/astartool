astartool
=========

toolkit for python.


A.Star私房工具包

唉~ 写了辣么多代码，总觉得过于臃肿。
我把简单的代码能重复利用的摘出来作为工具包，以后就引用他了

目前此代码包含一下几部分:
1. data_structure

keymap: 两端键值的类字典
linked_list: 链表
queue: 链式队列

2. error
错误的包

MethodNotFoundError: 方法错误
ParameterError: 参数错误
ParameterTypeError: 参数类型错误
ParameterValueError: 参数值错误

3. exception

异常的包

4. file

  downloadhelper: 大文件下载
  excelhelper: excel生成
  filehelper: 简单的文件哈希、文件简单操作
  imagehelper: 简单的图片转化,目前对base64转image

5. number

number包包含数论/数字处理的一些基本代码

equals_zero: 与numpy.isclose类似，只不过这个是专门判断0的

equals_zero_any: 只要有一个为0,则返回True, 否则是False

equals_zero_all: 只有全部为0, 返回True, 否则是False

ishex: 判断是否是16进制字符串

gcd: 辗转相处法求最大公约

lcm: 最小公倍数

prime_factorzation: 筛选法求素数

rotate_left: 循环左移

6. project

file_logging/std_logging 日志装饰器

_project: 文档模板生成

_platform: 判断当前运行环境操作系统类型

time_clock: 对time.clock的改良，操作系统导致使用错误

7. random

random 包包含随机数相关的函数

generate_password: 随机密码

random_digit_string: 随机生成n位数字

random_string: 随机生成一个长度为n的字符串

random_hex_string: 随机生成n位16进制字符串

random_ip: 随机生成一个ip地址, 目前只支持IPV4

security_random_hex: 基于国密SM3的KDF

8. setuptool

包含打包相关的函数

_tool: 调用setup方法之前做一些处理

_version: 版本管理

9. string

包含字符串处理相关函数

is_email: 判断是不是邮箱

is_mobile: 判断是否是手机号

generate_number: 生成n位带时间编号

check_number: 检验生成n位带时间编号

to_binary: str转bytes

to_text: bytes转str

password_check 检查口令合法性的小工具

