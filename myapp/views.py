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
from rest_framework.schemas import AutoSchema
import coreapi


@api_view(['post'])
@schema(AutoSchema(manual_fields=[
    #location='query'加上后就拼接到了url上   #required=True 文档中当有location时才生效
    coreapi.Field(name="username", type='string', description='*姓名', required=True),
    coreapi.Field(name="age",type='integer', description='年龄'),
]))
# @authentication_classes((SessionAuthentication, BasicAuthentication))
# @permission_classes((IsAuthenticated,))
def hello_world(request):
    """哈哈 这个是方法注释"""

    print('------------->',request.data,request.get_raw_uri())

    return Response({"message": "Hello, world!%s"%(request.data.get('username',None)),})


# 以下为非restframwork内容
# 其他页面返回的东西
def hello(request):
    return render(request, 'hello.html', {'nihao': '你好啊啊啊' + "aaa"})


# admin管理页面的自定义页面demo
def custom_page(request):
    theads = []
    return render(request, 'custom_page.html', {"theads": theads, "trows": []})
