# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from myapp.models import MyUserModel
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.forms.models import model_to_dict
from tools.siger import check_siger
from tools.fomats import format_response_json
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
# from dwebsocket import require_websocket,accept_websocket
# import dwebsocket

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
    if username is None:
        return Response(format_response_json(state=2, msg='用户名为空'))

    users = MyUserModel.objects.filter(username=username)
    if len(users) > 0:
        return Response(format_response_json(state=2, msg='用户已存在'))
    else:
        user = MyUserModel()
        set_params_to_model(json_dic=json_data, model=user)
        user.save()
        return Response(format_response_json(msg='保存成功'))


# 其他页面返回的东西
@check_siger
def hello(request):
    users = MyUserModel.objects.filter(username='123')
    if len(users) > 0:
        data: set = model_to_dict(users.first())
        print('------------->', data)

    return render(request, 'hello.html', {'nihao': '你好啊啊啊' + "aaa"})


# admin管理页面的自定义页面demo
def custom_page(request):
    theads = []
    return render(request, 'custom_page.html', {"theads": theads, "trows": []})






# from dwebsocket import require_websocket,accept_websocket
# import dwebsocket
#
# from django.http.response import HttpResponse
# from django.shortcuts import render
# import json
#
# import redis
# rc = redis.StrictRedis(host='redis_host', port=6379, db=8, decode_responses=True)
#
# @require_websocket  # 只接受websocket请求，不接受http请求，这是调用了dwebsocket的装饰器
# def websocket_test(request):
#     message = request.websocket.wait()
#     request.websocket.send(message)
#
#
# @accept_websocket   # 既能接受http也能接受websocket请求
# def echo(request):
#     if not request.is_websocket():
#         try:
#             print('---- request.GET 数据：--->>',request.GET)
#             message = request.GET['message']
#             return HttpResponse(message)
#
#         except Exception as e:
#             print('---- 报错: e--->>',e)
#             return render(request,'test_websocket/user2.html')
#
#     else:
#         redis_my_key = ''
#         while True:
#             # print(dir(request.websocket))
#             # print('request.websocket.count_messages() -->', request.websocket.count_messages())
#             if request.websocket.count_messages() > 0:
#                 for message in request.websocket:
#
#                     print('request.websocket._get_new_messages() -->', request.websocket._get_new_messages())
#                     if request.websocket.is_closed():
#                         print('连接关闭')
#                         return HttpResponse('连接断开')
#                     else:
#
#                         # print('request.websocket.is_closed() -->', request.websocket.is_closed())
#                         print('--- request.is_websocket() 数据:  --->>',message)
#
#                         # 将数据写入数据库   {"my_uuid":"1","your_uuid":"2","message":"Hello, World!"}
#                         data = json.loads(message.decode())
#                         conn_type = data.get('type')
#                         my_uuid = data.get('my_uuid')
#                         your_uuid = data.get('your_uuid')
#                         msg = data.get('message')
#                         redis_my_key = 'message_{uuid}'.format(uuid=my_uuid)
#                         redis_you_key = 'message_{uuid}'.format(uuid=your_uuid)
#
#                         if conn_type == 'register':
#                             if my_uuid and your_uuid:
#                                 request.websocket.send("注册成功".encode('utf-8'))
#                             else:
#                                 request.websocket.send("uuid为空，链接断开".encode('utf-8'))
#                                 # request.websocket.close()
#                                 return HttpResponse('uuid为空，连接断开')
#                         elif conn_type == 'sendMsg':
#                             rc.lpush(redis_my_key, msg)
#                             rc.lpush(redis_you_key, msg)
#
#                         break
#             elif redis_my_key:
#                 data = rc.rpop(redis_my_key)
#                 if data:
#                     print('收到消息，立马发送data -->', data)
#                     request.websocket.send(data.encode('utf-8'))
#
#                 # print(dir(request.websocket))
#                 # request.websocket.send(message + '这是您发来的 @@@ '.encode('utf-8'))