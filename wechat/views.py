# -*- coding: utf-8 -*-

import hashlib
import json
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import time
import xml.etree.ElementTree as ET
import urllib3


TOKEN = "xhw" #微信token


#django默认开启csrf防护，这里使用@csrf_exempt去掉防护
@csrf_exempt
def weixin_main(request):
    if request.method == "GET":
        #接收微信服务器get请求发过来的参数
        signature = request.GET.get('signature', None)
        timestamp = request.GET.get('timestamp', None)
        nonce = request.GET.get('nonce', None)
        echostr = request.GET.get('echostr', None)

        #把参数放到list中排序后合成一个字符串，再用sha1加密得到新的字符串与微信发来的signature对比，如果相同就返回echostr给服务器，校验通过
        hashlist = [TOKEN, timestamp, nonce]
        hashlist.sort()
        hashstr = ''.join([s for s in hashlist])
        hashstr = hashlib.sha1(hashstr).hexdigest()
        if hashstr == signature:
          return HttpResponse(echostr)
        else:
          return HttpResponse("field")
    else:
        othercontent = autoreply(request)
        return HttpResponse(othercontent)

#微信服务器推送消息是xml的，根据利用ElementTree来解析出的不同xml内容返回不同的回复信息，就实现了基本的自动回复功能了，也可以按照需求用其他的XML解析方法

def autoreply(request):
    try:
        webData = request.body
        xmlData = ET.fromstring(webData)

        msg_type = xmlData.find('MsgType').text
        ToUserName = xmlData.find('ToUserName').text
        FromUserName = xmlData.find('FromUserName').text
        CreateTime = xmlData.find('CreateTime').text
        requestContent = xmlData.find('Content').text
        MsgId = xmlData.find('MsgId').text
        print  ('接收消息成功了---->>>>',requestContent)

        toUser = FromUserName
        fromUser = ToUserName
        if msg_type == 'text':
            if requestContent.startswith('#'):
                responseContent = getMsgFromTuLing(requestContent.replace('#','',1),msg_type)
            else:
                responseContent = "消息已收到,谢谢"
            print ('回复消息---->>>>',responseContent)
            replyMsg = TextMsg(toUser, fromUser, responseContent)
            print (replyMsg)
            return replyMsg.send()

        elif msg_type == 'image':
            responseContent = "图片已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, responseContent)
            return replyMsg.send()
        elif msg_type == 'voice':
            responseContent = "语音已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, responseContent)
            return replyMsg.send()
        elif msg_type == 'video':
            responseContent = "视频已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, responseContent)
            return replyMsg.send()
        elif msg_type == 'shortvideo':
            responseContent = "小视频已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, responseContent)
            return replyMsg.send()
        elif msg_type == 'location':
            responseContent = "位置已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, responseContent)
            return replyMsg.send()
        else:
            msg_type == 'link'
            responseContent = "链接已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, responseContent)
            return replyMsg.send()

    except Exception as Argment:
        return Argment

def getMsgFromTuLing(content,msg_type):
    try:
        urlStr = "http://openapi.tuling123.com/openapi/api/v2"
        jsonDic = {}
        jsonDic['reqType'] = 0
        jsonDic['perception'] = {'inputText':{'text':content}}
        jsonDic['userInfo'] = {'apiKey':'343d2e8e1fae46de9f7964618085dd54','userId':'xhw0525'}
        jsonstr = json.dumps(jsonDic)
        req = urllib3.Request(urlStr,jsonstr,{'Content-Type':'application/json'})
        f = urllib3.urlopen(req).read()
        resultDic = json.loads(f)
        try:
            string = ''
            for res in resultDic[u'results']:
                if res[u'resultType'] == u'text':
                    string+=res[u'values'][u'text'].encode('utf-8')
                if res[u'resultType'] == u'image':
                    pass
            return string
        except:
            return '图灵转码失败'
    except:
        return '图灵获取失败'
        pass


class Msg(object):
    def __init__(self, xmlData):
        self.ToUserName = xmlData.find('ToUserName').text
        self.FromUserName = xmlData.find('FromUserName').text
        self.CreateTime = xmlData.find('CreateTime').text
        self.MsgType = xmlData.find('MsgType').text
        self.MsgId = xmlData.find('MsgId').text


class TextMsg(Msg):
    def __init__(self, toUserName, fromUserName, content):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['Content'] = content

    def send(self):
        XmlForm = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[{Content}]]></Content>
        </xml>
        """
        return XmlForm.format(**self.__dict)