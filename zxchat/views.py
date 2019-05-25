# -*- coding: utf-8 -*-

import json
from django.http import HttpResponse
import time
from zxchat.models import ZXUserModel



def adduser(request):
    username = request.GET.get('name', '')
    print(username)
    users = ZXUserModel.objects.filter(username="22222")
    print(len(users))
    # if user is None:
    #     user = ZXUserModel()
    #     user.id = '123'
    #     user.username = request.GET.get('name', None)
    # else:
    #     user.username = user.username+'更新'
    # user.save()

    return HttpResponse("返回点啥")

