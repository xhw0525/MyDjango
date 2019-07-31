# -*- coding: utf-8 -*-
# coding: utf-8
from zchatapp.models import ZUserModel, ZBeiZhuModel, ZAutoReplyModel
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.forms.models import model_to_dict

from akuozhan.chat_manager import ChatManager
from tools.fomats import format_response_json, set_user_params, user_to_dict
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from django.http.response import HttpResponse, JsonResponse
from django.http.request import HttpRequest
from django.db.models.query import QuerySet, Q
from django.http import QueryDict
from akuozhan.smss_manager import SMSSManager
import time

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
import json
import datetime


@api_view(['post'])
def add_user(request):
    """
    @api {POST} /adduser/ 添加用户
    @apiGroup UserModule
    @apiDescription 这里可以描述一下这个函数的具体操作

    @apiParam {String} name 账号
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

    json_data = request.POST
    username = json_data.get('username')
    if username is None:
        return Response(format_response_json(state=2, msg='用户名为空'))

    users = ZUserModel.objects.filter(username=username)
    if len(users) > 0:
        return Response(format_response_json(state=2, msg='用户已存在'))
    else:
        user: ZUserModel = ZUserModel()
        set_user_params(json_dic=json_data, model=user)
        # 添加时间
        user.ctime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user.save()
        return Response(format_response_json(msg='保存成功', data_dic=user_to_dict(user)))


@api_view(['post'])
def save_beizhu(request):
    json_data = request.POST
    youname = json_data.get('youname')
    friendName = json_data.get('friendName')
    friendBeizhu = json_data.get('friendBeizhu')

    if youname is not None and friendName is not None and friendBeizhu is not None:
        # 好友备注信息
        beizhus: QuerySet = ZBeiZhuModel.objects.filter(user_name=youname, friend_name=friendName)
        beizhu = None;
        if (len(beizhus) > 0):
            beizhu: ZBeiZhuModel = beizhus.first()

        if beizhu is None:
            beizhu = ZBeiZhuModel()

        beizhu.beizhu_name = friendBeizhu
        beizhu.user_name = youname
        beizhu.friend_name = friendName
        beizhu.save()
        return Response(format_response_json(msg='保存成功'))
    else:
        return Response(format_response_json(msg='参数异常', state=1))


@api_view(['post'])
def get_user(request):
    json_data = request.data
    youname = json_data.get('youname')
    username = json_data.get('username')
    if username is None:
        return Response(format_response_json(state=2, msg='用户名为空'))

    users: QuerySet = ZUserModel.objects.filter(username=username)
    if len(users) == 0:
        return Response(format_response_json(state=2, msg='用户不存在'))
    else:
        user = users.first()
        # 好友备注信息
        beizhus: QuerySet = ZBeiZhuModel.objects.filter(user_name=youname, friend_name=user.username)
        if (len(beizhus) > 0):
            beizhu: ZBeiZhuModel = beizhus.first()
            user.beizhu = beizhu.beizhu_name

        return Response(format_response_json(data_dic=user_to_dict(user)))


@api_view(['post'])
def get_users(request):
    json_data: QueryDict = request.data
    youname = json_data.get('youname')
    user_names_str: str = json_data.get('usernames')
    user_names = None
    if type(user_names_str) is list:
        user_names = user_names_str
    else:
        user_names: list = json.loads(user_names_str)

    if user_names is None:
        return Response(format_response_json(state=2, msg='用户名s为空'))
    users_l: list = []

    users: QuerySet = ZUserModel.objects.filter(username__in=user_names)

    for user in users:
        # 好友备注信息
        beizhus: QuerySet = ZBeiZhuModel.objects.filter(user_name=youname, friend_name=user.username)
        if (len(beizhus) > 0):
            beizhu: ZBeiZhuModel = beizhus.first()
            user.beizhu = beizhu.beizhu_name

        users_l.append(user_to_dict(user))

    return Response(format_response_json(data_dic=users_l))


@api_view(['post'])
def update_user(request):
    json_data = request.data
    username = json_data.get('username')
    if username is None:
        return Response(format_response_json(state=2, msg='用户名为空'))

    users: QuerySet = ZUserModel.objects.filter(username=username)
    if len(users) == 0:
        return Response(format_response_json(state=2, msg='用户不存在'))
    else:
        user = users.first()
        set_user_params(json_dic=json_data, model=user)
        user.save()
        return Response(format_response_json(msg='保存成功'))


@api_view(['post'])
def forget_password(request):
    json_data = request.POST
    username = json_data.get('username')
    phone = json_data.get('phone')
    smsscode = json_data.get('smsscode')
    password = json_data.get('password')
    if username is None or phone is None or smsscode is None or password is None:
        return Response(format_response_json(state=2, msg='参数不全'))

    users = ZUserModel.objects.filter(username=username, phone=phone)
    if len(users) == 0:
        return Response(format_response_json(state=2, msg='账号不存在'))
    else:
        user: ZUserModel = users.first()
        smssresult: bool = SMSSManager.shareInstance().checkSMSSFromWeb(phone=phone, zone=86, code=smsscode)

        if smssresult:

            chatresult: bool = ChatManager.shareInstance().changeUserPassword(username=username, newpassword=password)
            if chatresult:
                user.password = password
                user.save()
                return Response(format_response_json(msg='密码重置成功'))
            else:
                return Response(format_response_json(state=2, msg='密码重置失败'))

        else:
            return Response(format_response_json(state=2, msg='验证码无效,请稍后重试'))


@api_view(['post'])
# @authentication_classes((SessionAuthentication, ))
# @permission_classes((IsAuthenticated,))
def get_kefu(request):
    """
    @api {POST} /xxx/ 获取用户信息

    """
    json_data = request.data
    username = json_data.get('username')
    sendAutoReply: str = json_data.get('sendAutoReply')

    # 获取客服
    users = ZUserModel.objects.filter(is_service=1)
    if len(users) == 0:
        return Response(format_response_json(msg='未获取到客服', state=1))

    kefu: ZUserModel = users.first()
    if sendAutoReply == "1":
        thre = DoAutoReply()
        thre.setReply(touser=username, fromuser=kefu.username)
        thre.start()
        # doAutoReplyForHuanXin(touser=username,fromuser=kefu.username)

    result: dict = format_response_json(data_dic=user_to_dict(kefu))
    return Response(result)


@api_view(['post'])
def upload_image(request: HttpRequest):
    """
    @api {POST} /xxx/ 上传图片

    """
    username = request.data.get('username')
    if not username:
        return JsonResponse(format_response_json(msg='用户名为空', state=1))

    users = ZUserModel.objects.filter(username=username)
    if len(users) == 0:
        return JsonResponse(format_response_json(msg='用户不存在', state=1))

    headimage = request.FILES.get('file')
    if not headimage:
        return JsonResponse(format_response_json(msg='未获取到文件', state=1))

    imagename = 'chat_' + username + '_' + str(time.time()) + '.png'
    path = os.path.join('media', imagename)

    user: ZUserModel = users.first()
    user.head = imagename
    user.save()
    rpath = os.path.join(ZSetting.BASE_DIR, 'public', path)

    with open(rpath, 'wb') as f:
        for line in headimage.chunks():
            f.write(line)

    return JsonResponse(format_response_json(msg='保存成功', data_dic=imagename))


@api_view(['post'])
def update_lasttime(request: HttpRequest):
    username = request.data.get('username')
    # lasttime = request.data.get('lasttime')
    dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ZUserModel.objects.filter(username=username).update(last_time=dt)

    return JsonResponse(format_response_json(msg='更新成功'))








# def doAutoReplyForHuanXin(touser, fromuser):
#     models = ZAutoReplyModel.objects.all()
#     if len(models) != 0:
#         for msg_model in models:
#             if msg_model.msg_text is not None:
#                 ChatManager.shareInstance().sendTextMessage(touser=touser, fromuser=fromuser,
#                                                             content=msg_model.msg_text)
#             if msg_model.msg_image.name is not None and len(msg_model.msg_image.name) != 0:
#                 if msg_model.image_uuid is not None and len(msg_model.image_uuid) > 0:
#
#                     time.sleep(0.1)
#                     ChatManager.shareInstance().sendImageMessage(touser=touser, fromuser=fromuser,
#                                                                  autoReply=msg_model)
#                 else:
#                     path = os.path.join('media', msg_model.msg_image.name)
#                     rpath = os.path.join(ZSetting.BASE_DIR, 'public', path)
#
#                     upload_result = ChatManager.shareInstance().uploadFileToWeb(fielurl=rpath,
#                                                                                 name=msg_model.msg_image.name)
#                     entities: dict = upload_result['entities'][0]
#
#                     msg_model.image_uuid = entities['uuid']
#                     msg_model.image_type = entities['type']
#                     msg_model.image_share_secret = entities['share-secret']
#                     msg_model.save()
#                     time.sleep(0.1)
#                     ChatManager.shareInstance().sendImageMessage(touser=touser, fromuser=fromuser,autoReply=msg_model)


##通过thread 实现django中
import threading
import time


class DoAutoReply(threading.Thread):
    touser = ""
    fromuser = ""

    def setReply(self, touser, fromuser):
        self.touser = touser
        self.fromuser = fromuser

    def run(self):
        time.sleep(0.5)
        # 获取自动回复内容
        models = ZAutoReplyModel.objects.all()
        if len(models) != 0:
            for msg_model in models:
                if msg_model.msg_text is not None:
                    ChatManager.shareInstance().sendTextMessage(touser=self.touser, fromuser=self.fromuser,
                                                                content=msg_model.msg_text)
                if msg_model.msg_image.name is not None and len(msg_model.msg_image.name) != 0:
                    if msg_model.image_uuid is not None and len(msg_model.image_uuid) > 0 and msg_model.msg_image_for_huanxin.name == msg_model.msg_image.name:

                        time.sleep(1)
                        ChatManager.shareInstance().sendImageMessage(touser=self.touser, fromuser=self.fromuser,
                                                                     autoReply=msg_model)
                    else:
                        path = os.path.join('media', msg_model.msg_image.name)
                        rpath = os.path.join(ZSetting.BASE_DIR, 'public', path)

                        upload_result = ChatManager.shareInstance().uploadFileToWeb(fielurl=rpath,
                                                                                    name=msg_model.msg_image.name)
                        entities: dict = upload_result['entities'][0]

                        msg_model.image_uuid = entities['uuid']
                        msg_model.image_type = entities['type']
                        msg_model.image_share_secret = entities['share-secret']
                        msg_model.msg_image_for_huanxin = msg_model.msg_image
                        msg_model.save()
                        time.sleep(0.1)
                        ChatManager.shareInstance().sendImageMessage(touser=self.touser, fromuser=self.fromuser,
                                                                     autoReply=msg_model)
