from django.contrib.auth.models import AbstractUser
from django.db import models
from djangohelper.contrib.auth.apps import AuthConfig


# from djangohelper.contrib.auth.models import User
#
# STATE_CHOICE = (
#     (-1, '无状态'),
#     (0, '交易中'),
#     (1, '已结单'),
#     (2, '部分退款'),
#     (3, '全部退款'),
#     (4, '悔单')
# )
#
# USER_ROLE_CHOICES = (
#     ('SU', 'SuperUser'),
#     ('GA', 'GroupAdmin'),
#     ('PU', 'Programmer'),
#     ('CU', 'Customer'),
#     ('SK', 'StoreKeeper'),
#     ('VU', 'VIPCustomer')
# )


class User(AbstractUser):
    """
    用户表
    """
    email = models.EmailField('email address', blank=True, unique=True)
    role = models.CharField(max_length=8, default='CU', choices=USER_ROLE_CHOICES)
    QQ = models.CharField(max_length=32, default=None, unique=True, blank=True, null=True)
    telephone = models.CharField(max_length=15, unique=True)
    sex = models.CharField(max_length=1, default='F')
    realname = models.CharField(max_length=32, default=None, null=True, blank=True)
    IDcard = models.CharField(max_length=19, default=None, null=True, blank=True, unique=True)
    registertime = models.DateTimeField(auto_now_add=True)
    wechat = models.CharField(max_length=32, null=True, blank=True, default=None)
    school = models.CharField(max_length=128, null=True, blank=True, default=None)
    alipay = models.CharField(max_length=64, null=True, blank=True, default=None)
    # father = models.ForeignKey('self', on_delete=models.CASCADE, null=True, default=None)
    #
    # def __str__(self):
    #     return self.username


class ProductType(models.Model):
    name = models.CharField(max_length=32)


class Project(models.Model):
    project_id = models.CharField(max_length=32)
    product_type_class = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    product_type_item = models.CharField(max_length=32)
    project_title = models.CharField(max_length=32)
    deadline = models.DateTimeField()
    money = models.CharField(max_length=1024)
    project_description = models.TextField()
    customer = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='customer', )
    poster = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='poster')


class Order(models.Model):
    order_id = models.CharField(max_length=32)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    order_time = models.DateTimeField(auto_created=True, auto_now=True)
    programmer = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.IntegerField(verbose_name='状态', choices=STATE_CHOICE)


# models.CharField(verbose_name)
class OrderStateLog(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    old_state = models.IntegerField(choices=STATE_CHOICE, null=True, blank=True)
    new_state = models.IntegerField(choices=STATE_CHOICE)
    change_time = models.DateTimeField(auto_now=True, auto_created=True)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)


class QQGroup(models.Model):
    number = models.CharField(max_length=32)

#
# class WaitingQueue(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     programmer = models.ForeignKey(User, on_delete=models.DO_NOTHING, 'programmer')
#     timestamp = models.DateTimeField()
