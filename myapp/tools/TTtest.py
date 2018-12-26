# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def creat_phantomjs(show_img=True):
    service_args = []
    if not show_img:
        service_args.append('--load-images=no')     # 关闭图片加载

    desire = DesiredCapabilities.PHANTOMJS.copy()
    headers = {'Accept': '*/*',
               'Accept-Language': 'en-US,en;q=0.8',
               'Cache-Control': 'max-age=0',
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
               'Connection': 'keep-alive',
               }
    for key, value in headers.iteritems():
        desire['phantomjs.page.customHeaders.{}'.format(key)] = value
    service_args.append('--ignore-ssl-errors=true')     # 忽略https错误
    browser = webdriver.PhantomJS('/Users/xhw/PythonV/phantomjs-2.1.1-macosx/bin/phantomjs',desired_capabilities=desire,
                                      service_args=service_args)
    # browser = webdriver.Safari()
    return browser


browser = creat_phantomjs()
browser.delete_all_cookies()
browser.get('https://sso.toutiao.com')
browser.get_cookies()

phone1 = browser.find_element_by_xpath('//*[@id="mobile"]')  # 手机号
ActionChains(browser).click(phone1).perform()
phone1.send_keys('12345678901')

msg1 = browser.find_element_by_xpath('//*[@id="captcha1"]')  # 验证码
ActionChains(browser).click(msg1).perform()
msg1.send_keys('123')



getyzm = browser.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div/form/div[3]/span')


ActionChains(browser).click(getyzm).perform()
time.sleep(0.5)
ActionChains(browser).click(getyzm).perform()


browser.save_screenshot('haha.png')
browser.quit()