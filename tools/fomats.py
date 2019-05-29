# -*- coding: utf-8 -*-

import json
from django.forms.models import model_to_dict
from django.http.response import JsonResponse
from django.http.request import HttpRequest


def format_response_json(msg='success', state=0, data_dic=''):
    json_dic = {'state': state, 'msg': msg, 'data': data_dic}

    return json_dic
