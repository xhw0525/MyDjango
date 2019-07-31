# -*- coding: utf-8 -*-
# coding: utf-8

import threading
import requests as requests
import json
from zchatapp.models import ZAutoReplyModel

or_name = "xhw0525"
app_name = "my123"


# Create your models here.
class ChatManager(object):
    token = ""

    requests = requests

    _instance_lock = threading.Lock()

    @classmethod
    def shareInstance(cls, *args, **kwargs):
        if not hasattr(ChatManager, "_instance"):
            with ChatManager._instance_lock:
                if not hasattr(ChatManager, "_instance"):
                    ChatManager._instance = ChatManager(*args, **kwargs)
        return ChatManager._instance

    def getTokenFromWeb(self):
        url = 'https://a1.easemob.com/%s/%s/token?org_name=%s&app_name=%s' % (or_name, app_name, or_name, app_name)

        headers = {
            'Content-Type': 'application/json',
        }
        data = {
            "grant_type": "client_credentials",
            "client_id": "YXA6vnQ10GbwEeaNUrOwYDD2Pw",
            "client_secret": "YXA6Dj98aySTDg_NXFQj6nShiV-p-ok"
        }

        reqs = self.requests.post(url=url, headers=headers, data=json.dumps(data))
        result = json.loads(reqs.text)
        self.token = result['access_token']

    def sendTextMessage(self, touser, fromuser="admin", content=" ", reopen=False):
        url = 'https://a1.easemob.com/%s/%s/messages' % (or_name, app_name)

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer %s' % (self.token)

        }
        data = {
            "target_type": "users",
            "target": [
                touser
            ],
            "msg": {
                "type": "txt",
                "msg": content
            },
            "from": fromuser
        }

        reqs = self.requests.post(url=url, headers=headers, data=json.dumps(data))
        result = json.loads(reqs.text)
        if reqs.status_code != 200 and not reopen:
            self.getTokenFromWeb()
            self.sendTextMessage(touser=touser, fromuser=fromuser, content=content, reopen=True)

        return result

    def sendImageMessage(self, touser, fromuser="admin", autoReply=None, reopen=False):
        model: ZAutoReplyModel = autoReply;
        url = 'https://a1.easemob.com/%s/%s/messages' % (or_name, app_name)

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer %s' % (self.token)

        }
        data = {
            "target_type": "users",
            "target": [
                touser
            ],
            "msg": {
                "type": "img",
                "url": "https://a1.easemob.com/%s/%s/chatfiles/%s" % (or_name, app_name, model.image_uuid),
                # "filename":model.msg_image.name,
                "secret": model.image_share_secret,
                "size": {"width": 100, "height": 100}

            },
            "from": fromuser
        }

        reqs = self.requests.post(url=url, headers=headers, data=json.dumps(data))
        result = json.loads(reqs.text)
        if reqs.status_code != 200 and not reopen:
            self.getTokenFromWeb()
            self.sendImageMessage(touser=touser, fromuser=fromuser, autoReply=autoReply, reopen=True)

        return result

    def uploadFileToWeb(self, fielurl="", name="123.png", reopen=False):
        url = 'https://a1.easemob.com/%s/%s/chatfiles' % (or_name, app_name)

        headers = {
            'restrict-access': "true",
            'Authorization': 'Bearer %s' % (self.token)

        }

        files = {
            'file': (name, open(fielurl, 'rb'), 'image/png')  # image或者file
        }
        reqs = self.requests.post(url=url, headers=headers, files=files, data={})
        result = json.loads(reqs.text)
        if reqs.status_code != 200 and not reopen:
            self.getTokenFromWeb()
            return self.uploadFileToWeb(fielurl=fielurl, reopen=True)

        return result

    def changeUserPassword(self, username, newpassword="123456", reopen=False):
        url = 'https://a1.easemob.com/%s/%s/users/%s/password' % (or_name, app_name, username)

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer %s' % (self.token)

        }
        data = {
            "newpassword": newpassword,
        }

        reqs = self.requests.post(url=url, headers=headers, data=json.dumps(data))

        print("====>>huanxin_change_password_code:".encode('utf-8'), reqs.status_code, "====>content:".encode('utf-8'), reqs.text)
        if reqs.status_code != 200 and not reopen:
            self.getTokenFromWeb()
            return self.changeUserPassword(username=username, newpassword=newpassword, reopen=True)

        return reqs.status_code == 200 or reqs.status_code == '200'

# manager = ChatManager.shareInstance()
# manager.getTokenFromWeb()
# manager.sendTextMessage(touser='qqqq', content="哈哈123")
