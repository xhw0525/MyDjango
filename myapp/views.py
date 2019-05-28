# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import schema
from rest_framework.decorators import permission_classes
from rest_framework.parsers import JSONParser
from myapp.models import MyUserModel
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action, api_view
from myapp.serializers import MyUserModelSerializer
from rest_framework.views import APIView
from rest_framework.schemas import AutoSchema, ManualSchema

import coreapi


@api_view(['post'])
def hello_world(request):
    """
    @api {POST} /hello_world/ 哈啊 apidoc 自动文档
    @apiGroup LoginModule
    @apiDescription 这里可以描述一下这个函数的具体操作
        这一行也是可以描述的

    @apiParam {String} name 姓名
    @apiParam {String} password 密码

    @apiSuccess {Object} status 状态码
    @apiSuccess {Object} msg 简略描述

    @apiSuccessExample Response-Success:
        {
            'status': 0,
            'msg': 'success'
        }
    @apiErrorExample Response-Fail:
        {
            'status': 1,
            'msg': 'Fail'
        }
    """
    print('------------->', request.data, request.get_raw_uri())

    return Response({'status': 0, "msg": "Hello, %s!" % (request.data.get('username', None)), })


# 以下为非restframwork内容
# 其他页面返回的东西
def hello(request):
    return render(request, 'hello.html', {'nihao': '你好啊啊啊' + "aaa"})


# admin管理页面的自定义页面demo
def custom_page(request):
    theads = []
    return render(request, 'custom_page.html', {"theads": theads, "trows": []})
