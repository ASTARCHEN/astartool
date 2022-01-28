# astartool

[![version](https://img.shields.io/pypi/v/astartool.svg)](https://pypi.python.org/pypi/astartool)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FASTARCHEN%2Fastartool.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2FASTARCHEN%2Fastartool?ref=badge_shield)
[![gitee](https://gitee.com/hoops/astartool/badge/star.svg)](https://gitee.com/hoops/astartool/stargazers)
[![github](https://img.shields.io/github/stars/ASTARCHEN/astartool)](https://img.shields.io/github/stars/ASTARCHEN/astartool)
[![download](https://img.shields.io/pypi/dm/astartool.svg)](https://pypi.org/project/astartool)
[![wheel](https://img.shields.io/pypi/wheel/astartool.svg)](https://pypi.python.org/pypi/astartool)
[![CodeFactor](https://www.codefactor.io/repository/github/astarchen/astartool/badge/main)](https://www.codefactor.io/repository/github/astarchen/astartool/overview/main)
![status](https://img.shields.io/pypi/status/astartool.svg)

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

3. exception

异常的包

4. file

  downloadhelper: 大文件下载
  excelhelper: excel生成
  filehelper: 简单的文件哈希、文件简单操作

5. number

number包包含数论的一些基本代码

ishex: 判断是否是16进制字符串

gcd: 辗转相处法求最大公约

lcm: 最小公倍数

6. project

file_logging/std_logging 日志装饰器
_project: 文档模板生成

7. random

random 包包含随机数相关的函数

random_string: 随机生成一个长度为n的字符串

random_hex_string: 随机生成n位16进制字符串

random_digit_string: 随机生成n位数字

generate_password: 随机生成密码

security_random_hex: 基于国密SM3的KDF

random_ip: 随机生成一个ip地址, 目前只支持IPV4

8. setuptool

包含打包相关的函数

9. string

包含字符串处理相关函数

is_email: 判断是不是邮箱

is_mobile: 判断是否是手机号

generate_number: 生成n位带时间编号

check_number: 检验生成n位带时间编号
 


## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FASTARCHEN%2Fastartool.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FASTARCHEN%2Fastartool?ref=badge_large)

