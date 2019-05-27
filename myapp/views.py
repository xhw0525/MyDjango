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


class UserViewSet(viewsets.ModelViewSet):
    """API端：允许查看和编辑用户"""
    queryset = MyUserModel.objects.all().order_by('-ctime')
    serializer_class = MyUserModelSerializer
    parser_classes = (JSONParser,)

    def get_permissions(self):
        if self.action in ('create',):
            self.permission_classes = [IsAuthenticated]
        return [permission() for permission in self.permission_classes]

    def list(self, request, **kwargs):
        users = MyUserModel.objects.all()
        serializer = MyUserModelSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @permission_classes(IsAuthenticated, )
    def create(self, request, **kwargs):
        name = request.data.get('username')
        users = MyUserModel.objects.create(name=name)
        serializer = MyUserModelSerializer(users)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post', ], )
    def getforusername(self, request, pk=None):
        name = request.data.get('name', None)
        if name:
            users = MyUserModel.objects.filter(username=name).first()
        return Response(users, status=status.HTTP_200_OK)


class ApiViewDemo(APIView):
    schema = AutoSchema(manual_fields=[
        coreapi.Field(name="username", required=False, location="query", description="介绍出不来啊"),
        coreapi.Field(name="phone", required=False, location="query", description="介绍出不来啊"),
    ])

    @action(detail=False, )
    def get(self, request, *args, **kwargs):
        """
        发送信息到指定人员邮箱\r\n
        参数列表：\r\n
            from_email： 发件人邮箱\r\n
            to_email: 收件人，多个收件人请使用英文逗号分隔隔开\r\n
            subject: 邮件主题\r\n
            message: 邮件正文\r\n
        """
        return Response('get请求')


@api_view(['post'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field(name="phone", ),
    coreapi.Field(name="gwae", ),
]))
def hello_world(request):
    """
    发送信息到指定人员邮箱\r\n
    参数列表：\r\n
        from_email： 发件人邮箱\r\n
        to_email: 收件人，多个收件人请使用英文逗号分隔隔开\r\n
        subject: 邮件主题\r\n
        message: 邮件正文\r\n
    """
    return Response({"message": "Hello, world!"})


# 以下为非restframwork内容
# 其他页面返回的东西
def hello(request):
    return render(request, 'hello.html', {'nihao': '你好啊啊啊' + "aaa"})


# admin管理页面的自定义页面demo
def custom_page(request):
    theads = []
    return render(request, 'custom_page.html', {"theads": theads, "trows": []})
