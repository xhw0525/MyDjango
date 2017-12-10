# -*- coding: utf-8 -*-

import db_my
import json
import random
import time
import urllib2
page = 1
page_i = 1

def get_Main(browser, id, load_pages = 5, load_all=False,max_tags = 5, load_user=False, detay_rand = 0.2):
    global page
    global page_i

    while True:
        url = 'https://work.bugtags.com/api/apps/'+str(id)+'/issues/?page=' + str(page)
        print '---url--get_Main', url
        browser.get(url)

        time.sleep(random.random() * detay_rand)
        # time.sleep(20)
        jsonp = json.loads(browser.find_element_by_css_selector('body').text)
        print '---json--->', jsonp
        try:
            jsons = jsonp['data']['list']
            print '---page', page, '----len', len(jsons)
        except:
            print '---page', page, '----失败'
            break
        page += 1
        ids = db_my.sava_db_main(jsons)
        page_i = 1
        if load_all or load_user:
            for child_id in ids:
                get_tags(browser,pid=id, id=child_id, load_user=load_user,max_tags = max_tags)
                page_i += 1
        # if not jsonp['data']['has_more']:
        #     break
        if len(jsons) < 20 or page > load_pages: #取前5页
            break





def get_tags(browser,pid,id,load_user=False,max_tags=5, detay_rand = 0.2):
    global page_i

    for i in range(0, max_tags):
        url = 'https://work.bugtags.com/api/apps/'+str(pid)+'/issues/'+str(id)+'/crashes/?page=' + str(i+1)
        print '---url--get_tags', url
        browser.get(url)

        time.sleep(random.random() * detay_rand)
        # time.sleep(20)
        jsonp = json.loads(browser.find_element_by_css_selector('body').text)
        print '---json--->', jsonp
        try:
            jsons = jsonp['data']['list']
            print '---page', page-1, '--page-i', page_i, '---page_tags', i+1, '----len', len(jsons), '---id', id
        except:
            print '---page', page-1, '--page-i', page_i, '---page_tags', i+1, '----失败'
            continue

        user_datas =db_my.sava_db_tags(jsons)

        if load_user:
            get_user_datas(browser, user_datas,max_tags)

        if not jsonp['data']['has_more']:
            break



def get_user_datas(browser, user_datas,max_tags, detay_rand = 0.2):
    if user_datas is None or len(user_datas) == 0:
        return
    for i in range(0, len(user_datas)):
        tagid, user_url = user_datas[i]
        print '---url--get_user_data', user_url
        f = urllib2.urlopen(user_url, timeout=30)

        data = f.read()

        time.sleep(random.random() * detay_rand)
        jsonp = json.loads(data)
        if not len(jsonp):
            print '---json--->', '[]'
            continue
        print '---json--->', jsonp
        jsonp['tagid'] = str(tagid)
        db_my.sava_db_user_data(jsonp)

        if i > max_tags:
            break
