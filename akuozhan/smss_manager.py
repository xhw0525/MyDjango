# -*- coding: utf-8 -*-

import threading
import requests as requests
import json


class SMSSManager(object):
    appkey = "2ba5e2d5dedcc"
    requests = requests

    _instance_lock = threading.Lock()

    @classmethod
    def shareInstance(cls, *args, **kwargs):
        if not hasattr(SMSSManager, "_instance"):
            with SMSSManager._instance_lock:
                if not hasattr(SMSSManager, "_instance"):
                    SMSSManager._instance = SMSSManager(*args, **kwargs)
        return SMSSManager._instance

    def checkSMSSFromWeb(self, phone, zone, code):
        url = 'https://webapi.sms.mob.com/sms/verify'

        headers = {
            'Content-Type': 'application/json',
        }
        data = {
            "appkey": self.appkey,
            "phone": phone,
            "zone": zone,
            "code": code,
        }

        reqs = self.requests.post(url=url, headers=headers, data=data)
        result = json.loads(reqs.text)
        print("====>>smss_result:", result, "success:", result['status'] == 200)
        return result['status'] == 200


if __name__ == '__main__':
    manager = SMSSManager()
    manager.checkSMSSFromWeb(phone='18660806096', zone=86, code='2645')
