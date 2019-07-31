# -*- coding: utf-8 -*-
from zchatapp.models import ZUserModel, ZAutoReplyModel
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.forms.models import model_to_dict

from tools.fomats import format_response_json, set_user_params, user_to_dict
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from django.http.response import HttpResponse, JsonResponse
from django.http.request import HttpRequest
from django.db.models.query import QuerySet
from rest_framework.request import Request
from rest_framework.parsers import BaseParser
from rest_framework.decorators import parser_classes
from django.views.decorators.csrf import csrf_exempt  # 不进行csrf验证

from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
import os
import MyDjango.settings as ZSetting
import _md5
from django.views.decorators.csrf import csrf_exempt
import csv
from django.http import HttpResponse
import datetime
import os
import xlwt
from django.http import StreamingHttpResponse
import MyDjango.settings as ZSetting

def index(request):
    return HttpResponse('index')


# admin管理页面的自定义页面demo
def custom_page(request):

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['username', 'nickname', 'phone', 'sex', 'ctime', 'atime', 'is_service',]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = ZUserModel.objects.all().values_list('username', 'nickname', 'phone', 'sex', 'ctime', 'atime', 'is_service')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


@api_view(['post'])
def login(request):
    json_data = request.data
    username = json_data.get('username')
    password = json_data.get('password')
    if username is None:
        return Response(format_response_json(state=2, msg='用户名为空'))

    users: QuerySet = ZUserModel.objects.filter(username=username, password=password)
    if len(users) == 0:
        return Response(format_response_json(state=2, msg='用户或密码错误'))
    else:
        user = users.first()
        return Response(format_response_json(msg='登录成功', data_dic=user_to_dict(model=user)))


@api_view(['post'])
def get_auto_reply(request):
    # json_data = request.data
    models = ZAutoReplyModel.objects.all()
    if len(models) == 0:
        return Response(format_response_json(msg='无', state=1))

    jsons = []

    for msg_model in models:
        if msg_model.msg_text is not None:
            dict_txt = {
                "content": msg_model.msg_text,
                "type": "text"
            }
            jsons.append(dict_txt)
        if msg_model.msg_image.name is not None and len(msg_model.msg_image.name) != 0:
            dict_image = {
                "content": os.path.join('media', msg_model.msg_image.name),
                "type": "image"
            }
            jsons.append(dict_image)

    return Response(format_response_json(data_dic=jsons))
