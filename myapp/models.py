# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Create your models here.

# noinspection PyInterpreter
class MyChatModel(models.Model):
    username = models.CharField(max_length=50)

    def __str__(self):
        return self.username.encode("utf-8")


class MyUserModel(models.Model):
    class Meta:
        verbose_name = '聊天App用户'
        verbose_name_plural = verbose_name

    username = models.CharField('姓名', max_length=50, blank=True)  # string	用户名
    phone = models.CharField('手机号', max_length=50, null=True, blank=True)  # string	手机号
    sex = models.IntegerField('性别(1男2女)', null=True, blank=True)  # int	1保密,2男,3女
    signature = models.CharField('签名', max_length=50, null=True, blank=True)  # string	个性签名
    year = models.IntegerField('年龄', null=True, blank=True)  # int	年龄
    head = models.CharField('头像', max_length=50, null=True, blank=True)  # string	头像
    nickname = models.CharField('昵称', max_length=50, null=True, blank=True)  # string	昵称
    type = models.IntegerField('1普通用户,2会员', null=True, blank=True)  # int	1普通用户,2会员
    status = models.IntegerField('1正常,2禁用', null=True, blank=True)  # int	1正常,2禁用
    activetime = models.DateField('账号使用有效期', null=True, blank=True)
    ctime = models.DateTimeField('添加时间', null=True, blank=True)  # string	添加时间
    mtime = models.DateTimeField('最后一次登录/修改时间', null=True, blank=True)  # string	最后一次登录/修改时间
    stature = models.CharField('身高', max_length=50, null=True, blank=True)  # string	身高
    birthday = models.DateField('生日', null=True, blank=True)  # string	生日
    industry = models.CharField('行业', max_length=50, null=True, blank=True)  # string	行业
    education = models.CharField('学历', max_length=50, null=True, blank=True)  # string	学历
    is_service = models.IntegerField('是否客服', default=0)  # int	是否客服 1是 0不是

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
