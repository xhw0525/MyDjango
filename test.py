# -*- coding: utf-8 -*-

import hashlib
import json
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import time
import xml.etree.ElementTree as ET
import urllib2

def haha():
    try:
        content = '你叫啥'
        urlStr = "http://openapi.tuling123.com/openapi/api/v2"
        jsonDic = {}
        jsonDic['reqType'] = 0
        jsonDic['perception'] = {'inputText':{'text':content}}
        jsonDic['userInfo'] = {'apiKey':'343d2e8e1fae46de9f7964618085dd54','userId':'xhw0525'}
        jsonstr = json.dumps(jsonDic)
        req = urllib2.Request(urlStr,jsonstr,{'Content-Type':'application/json'})
        f = urllib2.urlopen(req).read()
        resultDic = json.loads(f)

        print resultDic[u'results'][0][u'values'][u'text']

    except:
        return '服务器错误001'
        pass

haha()