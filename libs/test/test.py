# -*- coding: utf-8 -*-
from selenium import webdriver
import time
print(time.time())
service_args=[]
# service_args.append('--load-images=no')  ##关闭图片加载
# service_args.append('--disk-cache=yes')  ##开启缓存
# service_args.append('--ignore-ssl-errors=true') ##忽略https错误

# browser = webdriver.PhantomJS('/Users/xhw/PythonU/phantomjs-2.1.1-macosx/bin/phantomjs', service_args=service_args)
browser = webdriver.PhantomJS('/Users/xhw/PythonU/phantomjs-2.1.1-macosx/bin/phantomjs')

browser.set_page_load_timeout(0.1)  ##设置超时时间
browser.set_window_size(1920, 1080) ##设置窗口大小

try:
    browser.get('https://work.bugtags.com/login.html')
except Exception, e:
    print('error--->', e)

print('error_handler--->', browser.error_handler)

print('page--->',browser.page_source)
# 模拟登陆
# user_name = browser.find_element_by_id('login_email')
# user_name.send_keys('1982700252@qq.com')
# user_id = browser.find_element_by_id('login_pwd')
# user_id.send_keys('Zx.666555')
# btn = browser.find_element_by_id('btn_login')
# btn.click()

#整个网页滑动
# js="var q=document.documentElement.scrollTop += document.body.scrollHeight"
# browser.execute_script(js)
#指定元素滑动
# js="var q=document.getElementById('mainbody').scrollTop = document.getElementById('mainbody').scrollHeight"
# browser.execute_script(js)

time.sleep(1)

#打印源码
# print(browser.page_source)
#截图
# browser.save_screenshot('hahahaha.png')


browser.get('about:blank') #爬坑: 一次请求完 重置状态
print(time.time())

browser.close()     #close关闭当前页面

browser.quit()    #quit退出浏览器