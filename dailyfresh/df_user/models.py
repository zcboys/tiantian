# coding=utf-8
from django.db import models

# Create your models here.


class UserInfo(models.Model):
    # 用户名
    uname = models.CharField(max_length=20)
    # 密码
    upwd = models.CharField(max_length=40)
    # 收货地址
    uaddress = models.CharField(max_length=100)
    # 手机号
    uphone = models.CharField(max_length=11)
    # 邮编
    uyoubian = models.CharField(max_length=6)
    # 邮箱
    uemail = models.CharField(max_length=40)