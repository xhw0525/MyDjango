# -*- coding: utf-8 -*-
# coding: utf-8
import json
from django.forms.models import model_to_dict
from django.http.response import JsonResponse
from django.http.request import HttpRequest
from zchatapp.models import ZUserModel


def format_response_json(msg='success', state=0, data_dic=''):
    json_dic = {'state': state, 'msg': msg, 'data': data_dic}

    return json_dic


def set_user_params(json_dic={}, model: ZUserModel = None):
    user_fields = [
        'username',
        'password',
        'phone',
        'sex',
        'signature',
        'nickname',
    ]
    for parm in json_dic:
        if user_fields.__contains__(parm):
            setattr(model, parm, json_dic[parm])


def user_to_dict(model: ZUserModel = None):
    exclude = ['password', 'is_service', 'head']
    dic = model_to_dict(model, exclude=exclude)
    dic['head'] = model.head.name
    return dic
