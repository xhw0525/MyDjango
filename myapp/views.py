# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from myapp.models import BugTag

# Create your views here.
browser = None


def hello(request):
    # tags =BugTag(name='你好bug')
    # tags.save()
    names = BugTag.objects.get(id =1)
    name = names.name

    return render(request, 'hello.html', {'nihao': '你好啊啊啊' + name})

# def login(request):
#     global browser
#     if not browser:
#         browser = creat_phantomjs()
#         browser.delete_all_cookies()
#
#     if request.method == 'GET':
#         browser.get('https://sso.toutiao.com/')
#         srcimg = browser.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div/form/div[2]/div/img').get_attribute('src')
#         return render(request, 'login.html', {'imgsrc': srcimg})
#
#     # 已经登录
#     print browser.current_url
#     if browser.current_url != 'https://sso.toutiao.com/':
#         return render(request, 'hello.html', {'nihao': '123'})
#
#     if request.method == 'POST':
#         phone1 = browser.find_element_by_xpath('//*[@id="mobile"]')  # 手机号
#         ActionChains(browser).click(phone1).perform()
#         phone1.send_keys(request.POST['phone'])
#
#         msg1 = browser.find_element_by_xpath('//*[@id="captcha1"]')  # 验证码
#         ActionChains(browser).click(msg1).perform()
#         msg1.send_keys(request.POST['msg1'])
#
#         if request.POST['msg2']:
#             msg2 = browser.find_element_by_xpath('//*[@id="code"]')
#             ActionChains(browser).click(msg2).perform()
#             msg1.send_keys(request.POST['msg2'])
#             # 登录
#             loginbtn = browser.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div/form/input')
#             ActionChains(browser).click(loginbtn).perform()
#             time.sleep(0.5)
#             ActionChains(browser).click(loginbtn).perform()
#             time.sleep(2)
#             browser.save_screenshot('haha.png')
#
#         else: # 获取验证码
#             msg2 = browser.find_element_by_xpath('//*[@id="code"]')
#             ActionChains(browser).click(msg2).perform()
#
#             getyzm = browser.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div/form/div[3]/span')
#             ActionChains(browser).click(getyzm).perform()
#             time.sleep(0.5)
#             ActionChains(browser).click(getyzm).perform()
#             browser.save_screenshot('haha.png')
#
#         return HttpResponse('请刷新页面');
#
#
# def creat_phantomjs(show_img=True):
#     service_args = []
#     if not show_img:
#         service_args.append('--load-images=no')     # 关闭图片加载
#
#     desire = DesiredCapabilities.PHANTOMJS.copy()
#     headers = {'Accept': '*/*',
#                'Accept-Language': 'en-US,en;q=0.8',
#                'Cache-Control': 'max-age=0',
#                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
#                'Connection': 'keep-alive',
#                }
#     for key, value in headers.iteritems():
#         desire['phantomjs.page.customHeaders.{}'.format(key)] = value
#     service_args.append('--ignore-ssl-errors=true')     # 忽略https错误
#     browser = webdriver.PhantomJS('/Users/xhw/PythonV/phantomjs-2.1.1-macosx/bin/phantomjs',desired_capabilities=desire,
#                                   service_args=service_args)
#     # browser = webdriver.Safari()
#     return browser
