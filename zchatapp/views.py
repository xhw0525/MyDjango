# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from zchatapp.models import ZUserModel
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.forms.models import model_to_dict
from tools.siger import check_siger
from tools.fomats import format_response_json
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response


@api_view(http_method_names=['post'])
def adduser(request):
    """
    @api {POST} /hello_world/ 哈啊 apidoc 自动文档
    @apiGroup LoginModule
    @apiDescription 这里可以描述一下这个函数的具体操作
        这一行也是可以描述的

    @apiParam {String} name 姓名
    @apiParam {String} password 密码

    @apiSuccess {integer} status 状态码
    @apiSuccess {String} msg 简略描述
    @apiSuccess {Object} data 附加信息

    @apiSuccessExample Response-Success:
        {
            'status': 0,
            'msg': 'success'
            'data': '附加信息'
        }
    @apiErrorExample Response-Fail:
        {
            'status': 1,
            'msg': 'Fail'
            'data': '附加信息'
        }
    """

    json_data = request.data
    username = json_data.get('username')
    password = json_data.get('password')
    phone = json_data.get('phone')
    sex = json_data.get('sex')
    signature = json_data.get('signature')
    nickname = json_data.get('nickname')
    if username is None:
        return Response(format_response_json(state=2, msg='用户名为空'))

    users = ZUserModel.objects.filter(username=username)
    if len(users) > 0:
        return Response(format_response_json(state=2, msg='用户已存在'))
    else:
        user = ZUserModel()
        user.username = username
        user.password = password
        user.phone = phone
        user.sex = sex
        user.signature = signature
        user.nickname = nickname
        user.save()
        return Response(format_response_json(msg='保存成功'))



# admin管理页面的自定义页面demo
def custom_page(request):
    theads = []
    return render(request, 'custom_page.html', {"theads": theads, "trows": []})