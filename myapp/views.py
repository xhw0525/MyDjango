# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from myapp.models import MyUserModel
from tools.siger import check_siger
from django.db.models.query import QuerySet

# 其他页面返回的东西
@check_siger
def hello(request):
    users:QuerySet = MyUserModel.objects.filter(username='123')
    # if len(users) > 0:
    print('------------->',users.count())

    return render(request, 'hello.html', {'nihao': '你好啊啊啊' + "aaa"})


# admin管理页面的自定义页面demo
def custom_page(request):
    theads = []
    return render(request, 'custom_page.html', {"theads": theads, "trows": []})






