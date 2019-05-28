# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from myapp.models import MyUserModel
from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.decorators.http import require_http_methods
from django.forms.models import model_to_dict
from tools.siger import check_siger


@require_http_methods(["POST"])
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

    return HttpResponse({'status': 0, "msg": "Hello, %s!" % (request.data.get('username', None)), })
    return HttpResponse('123')


# 其他页面返回的东西
@check_siger
def hello(request):
    users = MyUserModel.objects.filter(username='123')
    data: set = model_to_dict(users.first())
    print('------------->', data)

    return render(request, 'hello.html', {'nihao': '你好啊啊啊' + "aaa"})


# admin管理页面的自定义页面demo
def custom_page(request):
    theads = []
    return render(request, 'custom_page.html', {"theads": theads, "trows": []})
