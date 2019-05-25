# -*- coding: utf-8 -*-

import json
from django.http import HttpResponse
from zxchat.models import ZXUserModel


def adduser(request):
    username = request.GET.get('username', None)
    password = request.GET.get('password', None)
    phone = request.GET.get('phone', None)
    sex = request.GET.get('sex', 1)
    signature = request.GET.get('signature', None)
    nickname = request.GET.get('nickname', None)
    if username is None:
        return HttpResponse(formatResponseJson(state=2, msg='用户名为空'))
    print(username, password, phone, sex, signature, nickname)
    user = None
    users = ZXUserModel.objects.filter(username=username)
    if len(users) > 0:
        return HttpResponse(formatResponseJson(state=2, msg='用户已存在'))
    else:
        user = ZXUserModel()

    user.username = username
    user.password = password
    user.phone = phone
    user.sex = sex
    user.signature = signature
    user.nickname = nickname

    user.save()

    return HttpResponse(formatResponseJson(msg='保存成功'))


def formatResponseJson(msg='success', state=0, data=[]):
    mainDic = {'msg': msg, 'state': state, 'data': data}

    return json.dumps(mainDic, ensure_ascii=False)
