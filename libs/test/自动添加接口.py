# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
print(time.time())


p_name = u'小友整体优化'

lists = [(u'自动添加脚本测试', u'http://zidong.com1'),
         (u'自动添加脚本测试1a', u'http://zidong.com2aa.c'),
         ]


#----------------------------------------------------------------------------------------------------

browser = webdriver.Firefox(log_path='./log/geckodriver.log')
browser.set_window_size(1000, 800)
browser.set_page_load_timeout(10)  ##超时时间

browser.get("http://devdoc.xiaoyouapp.cn/publics/login")
time.sleep(1)

user = browser.find_element_by_name('userName')
user.send_keys('admin')
pwd = browser.find_element_by_name('password')
pwd.send_keys('juxin1205')

yz = browser.find_element_by_xpath('/html/body/div[1]/div/form/input[3]')
while len(yz.get_attribute('value')) < 4:
    time.sleep(1)

btn = browser.find_element_by_class_name('btn-primary')
btn.click()
time.sleep(1)


addlink = browser.find_element_by_xpath('//a[@href="/index/api"]')
addlink.click()
time.sleep(1)

for namestr, urlstr in lists:
    browser.find_element_by_id('add_api_btn').click()

    slt = browser.find_element_by_xpath('//form/div/div/div/select')
    Select(slt).select_by_visible_text(p_name)

    name = browser.find_element_by_xpath('//form/div[1]/div[2]/div/input')
    name.send_keys(namestr)

    url = browser.find_element_by_xpath('//form/div[1]/div[3]/div/textarea')
    url.send_keys(urlstr)
    browser.find_element_by_id('add_api_send').click()
    time.sleep(1)

    al = browser.switch_to_alert()
    al.accept()
    time.sleep(1)
    print '已添加-->name:', namestr, ' url:', urlstr

# browser.save_screenshot('结果截图.png')
print(time.time())
browser.quit()    #quit退出浏览器
