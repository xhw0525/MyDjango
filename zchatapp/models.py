# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
class ZUserModel(models.Model):
    class Meta:
        verbose_name = '聊天App用户'
        verbose_name_plural = verbose_name

    username = models.CharField('账号', max_length=50, blank=True)
    password = models.CharField('密码', max_length=50, null=True, blank=True)
    phone = models.CharField('手机号', max_length=50, null=True, blank=True)
    sex = models.IntegerField('性别(1男2女)', null=True, blank=True)
    signature = models.CharField('签名', max_length=50, null=True, blank=True)
    head = models.ImageField('头像',  null=True, blank=True)
    nickname = models.CharField('昵称', max_length=50, null=True, blank=True)
    type = models.IntegerField('1普通用户,2会员', null=True, blank=True)
    status = models.IntegerField('1正常,2禁用,3删除', null=True, blank=True)
    ctime = models.DateTimeField('添加时间', null=True, blank=True)
    atime = models.DateField('有效时间', null=True, blank=True)
    stature = models.CharField('身高', max_length=50, null=True, blank=True)
    birthday = models.DateField('生日', null=True, blank=True)
    industry = models.CharField('行业', max_length=50, null=True, blank=True)
    education = models.CharField('学历', max_length=50, null=True, blank=True)
    is_service = models.BooleanField('是否客服', default=False)

    mtime = models.DateField('最后一次登录/修改时间', null=True, blank=True)
    last_time = models.DateTimeField('最后在线时间', null=True, blank=True)

    year = models.IntegerField('年龄', null=True, blank=True)
    beizhu = models.CharField('备注(取好友信息时计算,对好友的备注)', max_length=50, null=True, blank=True)

# def isok(self):  # 普通方法可以在admin里当作字段展示
#
#     return 'ok'
#
# def __str__(self):
#     return self.username.encode("utf-8")
class ZBeiZhuModel(models.Model):
    class Meta:
        verbose_name = '备注'
        verbose_name_plural = verbose_name
    user_name = models.CharField('使用备注者', max_length=50, blank=True)
    friend_name = models.CharField('被备注者', max_length=50, blank=True)
    beizhu_name = models.CharField('备注名', max_length=50, blank=True)
    status = models.IntegerField('状态', null=True, blank=True)



class ZAutoReplyModel(models.Model):
    class Meta:
        verbose_name = '自动回复内容'
        verbose_name_plural = verbose_name

    msg_text = models.TextField('文本消息内容', null=False, blank=False)
    msg_image = models.ImageField('图片消息内容', null=True, blank=True)
    msg_image_for_huanxin = models.ImageField('环信平台的图片消息内容', null=True, blank=True)
    image_uuid = models.TextField('图片上传环信后的uuid', null=True, blank=True)
    image_type = models.TextField('图片上传环信后的type', null=True, blank=True)
    image_share_secret = models.TextField('图片上传环信后的share_secret', null=True, blank=True)

    # def isok(self):  # 普通方法可以在admin里当作字段展示
    #
    #     return 'ok'
    #

# class CustomPageView(models.Model):  # 无用模型 只是为了admin中跳转到自定义界面
#     class Meta:
#         verbose_name = '导出所有用户数据'
#         verbose_name_plural = verbose_name
#
#     # name = models.CharField('名称', max_length=50, blank=True)  # string	用户名
#
#     pass
