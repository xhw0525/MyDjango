# -*- coding: utf-8 -*-
import method
import sqlite3
import json
def sava_db_main(jsons):

    if jsons is None or len(jsons) == 0:
        return
    ids = []
    # print(jsonp)
    conn = sqlite3.connect('../../result/db.sqlite3')
    sqlstr = """replace into bugtags_main (
    id,
app_id,
code,
description,
updated_at,
created_at) VALUES (?,?,?,?,?,?)"""

    for i in range(0, len(jsons)):
        param = (
            jsons[i]['id'],
            jsons[i]['app_id'],
            jsons[i]['code'],
            jsons[i]['description'],
            jsons[i]['updated_at'],
            jsons[i]['created_at'],)
        cursor = conn.cursor()
        cursor.execute(sqlstr, param)
        conn.commit()

        #保存tags

        if 'tags' in jsons[i].keys():
            sava_db_tags(jsons[i]['tags'])
        #保存截图信息
        if 'snapshots' in jsons[i].keys():
            sava_db_snapshots(jsons[i]['snapshots'])

        ids.append(jsons[i]['id'])
    conn.close()
    return ids


def sava_db_tags(jsons):
    user_datas = []
    if jsons is None or len(jsons) == 0:
        return
    conn = sqlite3.connect('../../result/db.sqlite3')
    sqlstr = """replace into bugtags_main_tags (
    id ,
app_id,
issue_id,
code,
snapshot_id, 
description,
updated_at,
created_at,
version_name,
version_code,
issue_code
    ) VALUES (?,?,?,?,?,?,?,?,?,?,?)"""

    for i in range(0, len(jsons)):
        if 'code' in jsons[i].keys():
            code = jsons[i]['code']
        else:
            code = 0

        if 'description' in jsons[i].keys():
            description = jsons[i]['description']
        else:
            description = None

        if 'updated_at' in jsons[i].keys():
            updated_at = jsons[i]['updated_at']
        else:
            updated_at = None

        if 'issue_code' in jsons[i].keys():
            issue_code = jsons[i]['issue_code']
        else:
            issue_code = 0
        param = (
            jsons[i]['id'],
            jsons[i]['app_id'],
            jsons[i]['issue_id'],
            code,
            jsons[i]['snapshot_id'],
            description,
            updated_at,
            jsons[i]['created_at'],
            jsons[i]['version_name'],
            jsons[i]['version_code'],
            issue_code,
        )
        cursor = conn.cursor()
        cursor.execute(sqlstr, param)
        conn.commit()
        if 'occurrence_info' in jsons[i].keys():
            occurrence_info = jsons[i]['occurrence_info']
            occurrence_info['tagid'] = jsons[i]['id']
            users = sava_db_occurrence_infos([occurrence_info])
            user_datas += users
        if 'snapshot' in jsons[i].keys() and len(jsons[i]['snapshot']) > 0:
            sava_db_snapshots([jsons[i]['snapshot'],])

    conn.close()
    return user_datas



def sava_db_snapshots(jsons):

    if jsons is None or len(jsons) == 0:
        return
    conn = sqlite3.connect('../../result/db.sqlite3')
    sqlstr = """replace into bugtags_main_snapshots (
id,
app_id,
issue_id,
url,
created_at,
has_snapshot
    ) VALUES (?,?,?,?,?,?)"""

    for i in range(0, len(jsons)):
        if 'id' in jsons[i].keys():
            pass
        else:
            continue

        if 'has_snapshot' in jsons[i].keys():
            has_snapshot = jsons[i]['has_snapshot']
        else:
            has_snapshot = False

        param = (
            jsons[i]['id'],
            jsons[i]['app_id'],
            jsons[i]['issue_id'],
            jsons[i]['url'],
            jsons[i]['created_at'],
            has_snapshot,
        )
        cursor = conn.cursor()
        cursor.execute(sqlstr, param)
        conn.commit()
    conn.close()


def sava_db_occurrence_infos(jsons):
    users = []
    if jsons is None or len(jsons) ==0:
        return
    conn = sqlite3.connect('../../result/db.sqlite3')
    sqlstr = """replace into bugtags_main_tags_occurrence_info (
tagid, 
version_name,
version_code,
release_state,
model,
time,
time_fmt,
user_steps,
user_data,
console_log,
crash_log
    ) VALUES (?,?,?,?,?,?,?,?,?,?,?)"""

    for i in range(0, len(jsons)):
        param = (
            jsons[i]['tagid'],
            jsons[i]['version_name'],
            jsons[i]['version_code'],
            jsons[i]['release_state'],
            jsons[i]['model'],
            jsons[i]['time'],
            jsons[i]['time_fmt'],
            jsons[i]['user_steps'],
            jsons[i]['user_data'],
            jsons[i]['console_log'],
            jsons[i]['crash_log'],
        )
        cursor = conn.cursor()
        cursor.execute(sqlstr, param)
        conn.commit()
        users.append((jsons[i]['tagid'], jsons[i]['user_data']))
    conn.close()
    return users


def sava_db_user_data(json):
    if json is None or len(json) == 0:
        return
    conn = sqlite3.connect('../../result/db.sqlite3')
    sqlstr = """replace into bugtags_main_user_data (
tagid,
app_code,
name,
s_uid,
uid,
s_sid,
appname
    ) VALUES (?,?,?,?,?,?,?)"""
    s_uid = s_sid = AppName = app_code = 0
    if 's_uid' in json.keys():
        s_uid = json['s_uid']
    if 's_sid' in json.keys():
        s_sid = json['s_sid']
    if 'AppName' in json.keys():
        AppName = json['AppName']
    if u'\u5f53\u524d\u7248\u672c\u53f7' in json.keys():
        app_code = -1

    param = (
        json['tagid'],
        app_code,
        json['name'],
        s_uid,
        json['uid'],
        s_sid,
        AppName,
    )
    cursor = conn.cursor()
    cursor.execute(sqlstr, param)
    conn.commit()
    conn.close()
