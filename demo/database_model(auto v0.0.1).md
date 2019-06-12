# 自动生成数据库模板头

**Version: 0.0.1**
**Auth:    ASTARTOOL ROBOT**
**Date:    2019-06-12 12:47:58.199048**


0. User

字段|字段描述|字段类型|字段信息
:--:|:--:|:--:|:--:|
email|'email address'|邮箱类型|可否为空格:True,是否唯一:True
role|role|变长字符串|最大长度:8,default:'CU',choices:USER_ROLE_CHOICES
QQ|QQ|变长字符串|最大长度:32,default:None,是否唯一:True,可否为空格:True,可否为空:True
telephone|telephone|变长字符串|最大长度:15,是否唯一:True
sex|sex|变长字符串|最大长度:1,default:'F'
realname|realname|变长字符串|最大长度:32,default:None,可否为空:True,可否为空格:True
IDcard|IDcard|变长字符串|最大长度:19,default:None,可否为空:True,可否为空格:True,是否唯一:True
registertime|registertime|时间类型|auto_now_add:True
wechat|wechat|变长字符串|最大长度:32,可否为空:True,可否为空格:True,default:None
school|school|变长字符串|最大长度:128,可否为空:True,可否为空格:True,default:None
alipay|alipay|变长字符串|最大长度:64,可否为空:True,可否为空格:True,default:None
# father|# father|ForeignKey|模型:'self',删除:models.CASCADE,可否为空:True,default:None

1. ProductType

字段|字段描述|字段类型|字段信息
:--:|:--:|:--:|:--:|
name|name|变长字符串|最大长度:32

2. Project

字段|字段描述|字段类型|字段信息
:--:|:--:|:--:|:--:|
project_id|project_id|变长字符串|最大长度:32
product_type_class|product_type_class|ForeignKey|模型:ProductType,删除:models.CASCADE
product_type_item|product_type_item|变长字符串|最大长度:32
project_title|project_title|变长字符串|最大长度:32
deadline||时间类型|
money|money|变长字符串|最大长度:1024
project_description||TextField|
customer|customer|ForeignKey|模型:User,删除:models.DO_NOTHING,related_name:'customer'
poster|poster|ForeignKey|模型:User,删除:models.DO_NOTHING,related_name:'poster'

3. Order

字段|字段描述|字段类型|字段信息
:--:|:--:|:--:|:--:|
order_id|order_id|变长字符串|最大长度:32
project_id|project_id|ForeignKey|模型:Project,删除:models.CASCADE
order_time|order_time|时间类型|是否自动生成:True,是否自动更新:True
programmer|programmer|ForeignKey|模型:User,删除:models.CASCADE
state|'状态'|整型|choices:STATE_CHOICE

4. OrderStateLog

字段|字段描述|字段类型|字段信息
:--:|:--:|:--:|:--:|
order|order|ForeignKey|模型:Order,删除:models.CASCADE
old_state|old_state|整型|choices:STATE_CHOICE,可否为空:True,可否为空格:True
new_state|new_state|整型|choices:STATE_CHOICE
change_time|change_time|时间类型|是否自动更新:True,是否自动生成:True
poster|poster|ForeignKey|模型:User,删除:models.CASCADE

5. QQGroup

字段|字段描述|字段类型|字段信息
:--:|:--:|:--:|:--:|
number|number|变长字符串|最大长度:32

