# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from myapp.tools import TTtest
from django.http import HttpResponse
import time
from selenium.webdriver.common.action_chains import ActionChains

# Create your views here.
browser = None
def hello(request):

    return render(request, 'hello.html',{'nihao':'你好啊啊啊'})


def login(request):
    global browser
    if not browser:
        browser = TTtest.creat_phantomjs()
        browser.delete_all_cookies()

    if request.method == 'GET':
        browser.get('https://sso.toutiao.com/')
        srcimg = browser.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div/form/div[2]/div/img').get_attribute('src')
        return render(request, 'login.html', {'imgsrc': srcimg})

    # 已经登录
    print browser.current_url
    if browser.current_url != 'https://sso.toutiao.com/':
        return render(request, 'hello.html', {'nihao': '123'})

    if request.method == 'POST':
        phone1 = browser.find_element_by_xpath('//*[@id="mobile"]')  # 手机号
        ActionChains(browser).click(phone1).perform()
        phone1.send_keys(request.POST['phone'])

        msg1 = browser.find_element_by_xpath('//*[@id="captcha1"]')  # 验证码
        ActionChains(browser).click(msg1).perform()
        msg1.send_keys(request.POST['msg1'])

        if request.POST['msg2']:
            msg2 = browser.find_element_by_xpath('//*[@id="code"]')
            ActionChains(browser).click(msg2).perform()
            msg1.send_keys(request.POST['msg2'])
            # 登录
            loginbtn = browser.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div/form/input')
            ActionChains(browser).click(loginbtn).perform()
            time.sleep(0.5)
            ActionChains(browser).click(loginbtn).perform()
            time.sleep(2)
            browser.save_screenshot('haha.png')

        else: # 获取验证码
            msg2 = browser.find_element_by_xpath('//*[@id="code"]')
            ActionChains(browser).click(msg2).perform()

            getyzm = browser.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div/form/div[3]/span')
            ActionChains(browser).click(getyzm).perform()
            time.sleep(0.5)
            ActionChains(browser).click(getyzm).perform()
            browser.save_screenshot('haha.png')

        return HttpResponse('请刷新页面');


