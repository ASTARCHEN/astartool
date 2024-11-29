
# -*- coding: utf-8 -*-


from astar_devopstool.version_announcement import version_release_announcement_template
from astar_devopstool.common import License, LICENSE_SHORT, Language, Plantform

import astartool

version_dict = {
    'project_name': 'astartool',
    'version': astartool.__version__,
    '版本': astartool.__version__,
    '日期': '2024-11-29',
    '授权协议': LICENSE_SHORT[License.APACHE],
    '开发语言': Language.PYTHON.value,
    '操作系统': "跨平台",
    '分类': "运维工具、工具包",
    '开源地址-gitee': '[https://gitee.com/hoops/astartool]'
                  '(https://gitee.com/hoops/astartool)',
    '开源下载-pypi': '[https://pypi.org/project/astartool/]'
                 '(https://pypi.org/project/astartool/)'
}

content = """
### 新增

1. project: 新增对32位系统、64位系统的判断
2. file: excelhelper-支持导出多表格; compresshelper-新增，处理解压; filehelper-支持tar/bz2/gz格式的解压
3. string: is_valid_number-判断是整数/小数/分数中的一种
4. setuptool: get_complete_version-支持小于5位的元祖扩展成5位; python高版本的常量定义

### 修复

1. filehelper-文件计算哈希时异常bug

"""

version_release_announcement_template(version_dict, content=content, file_name="../docs/version_release.md")
