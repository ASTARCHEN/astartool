
# -*- coding: utf-8 -*-


from astar_devopstool.version_announcement import version_release_announcement_template
from astar_devopstool.common import License, LICENSE_SHORT, Language, Plantform

import astartool

version_dict = {
    'project_name': 'astartool',
    'version': astartool.__version__,
    '版本': astartool.__version__,
    '日期': '2022-5-2',
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

1. 惰性字典
2. 合并字典

### 修复

1. gcd代码异常
2. 高版本python（3.10+）下collections工具包异常

"""

version_release_announcement_template(version_dict, content=content, file_name="../docs/version_release.md")
