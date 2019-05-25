# -*- coding: utf-8 -*-

import json
from django.http import HttpResponse
from zxchat.models import ZXUserModel
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def adduser(request):
    json_data = formatRequestJson(request)
    
    username = json_data.get('username')
    password = json_data.get('password')
    phone = json_data.get('phone')
    sex = json_data.get('sex')
    signature = json_data.get('signature')
    nickname = json_data.get('nickname')
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


@csrf_exempt
def updateuser(request):
    json_data = formatRequestJson(request)

    username = json_data['username']

    if username is None:
        return HttpResponse(formatResponseJson(state=2, msg='用户名为空'))

    users = ZXUserModel.objects.filter(username=username)

    if len(users) == 0:
        return HttpResponse(formatResponseJson(state=2, msg='用户不存在'))

    user: ZXUserModel = users.first()

    for parm in json_data:
        setattr(user, parm, json_data[parm])

    user.save()

    return HttpResponse(formatResponseJson(msg='保存成功'))


def formatResponseJson(msg='success', state=0, data=''):
    mainDic = {'msg': msg, 'state': state, 'data': data}

    return json.dumps(mainDic, ensure_ascii=False)


def formatRequestJson(request):
    json_data = {}
    if request.method == 'POST':
        # 得到的是一个二进制数据
        json_str = request.body
        # print(json_str)  # b'{\n    "f":200,\n    "d":300\n    \n}'\
        # 对二进制数据进行解码,解码得到json数据
        json_str = json_str.decode()
        # print(json_str)  # {"f":200,"d":300}
        # 将json数据转化成字典形式
        json_data = json.loads(json_str)
        # print(json_data)

    return json_data
