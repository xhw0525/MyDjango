# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Create your models here.
class MyChatModel(models.Model):
    username = models.CharField(max_length=50)

    def __str__(self):
        return self.username.encode("utf-8")

class MyUserModel(models.Model):
    class Meta:
        verbose_name = '聊天App用户'
        verbose_name_plural = verbose_name

    username = models.CharField('姓名', max_length=50, blank=True)
    password = models.CharField('密码', max_length=50, null=True, blank=True)
    phone = models.CharField('手机号', max_length=50, null=True, blank=True)
    sex = models.IntegerField('性别(1男2女)', null=True, blank=True)
    signature = models.CharField('个性签名', max_length=50, null=True, blank=True)
    age = models.IntegerField('年龄', null=True, blank=True)
    headimage = models.CharField('头像', max_length=50, null=True, blank=True)
    nickname = models.CharField('昵称', max_length=50, null=True, blank=True)

    def isok(self):  # 普通方法可以在admin里当作字段展示

        return 'ok'
    # def __str__(self):
    #     return self.username.encode("utf-8")


class CustomPageView(models.Model):  # 无用模型 只是为了admin中跳转到自定义界面
    class Meta:
        verbose_name = 'admin中跳转自定义的xx'
        verbose_name_plural = verbose_name

    name = models.CharField('名称', max_length=50, blank=True)  # string	用户名

    pass
