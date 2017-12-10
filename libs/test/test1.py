# -*- coding: utf-8 -*-
from selenium import webdriver
import time
print(time.time())

if True:
    service_args=[]
    # service_args.append('--load-images=no')  ##关闭图片加载
    # service_args.append('--disk-cache=yes')  ##开启缓存
    # service_args.append('--ignore-ssl-errors=true') ##忽略https错误

    service_args.append('--proxy=127.0.0.1:8888') #代理
    service_args.append('--proxy-type=http') #代理
    browser = webdriver.PhantomJS('/Users/xhw/PythonU/phantomjs-2.1.1-macosx/bin/phantomjs', service_args=service_args)

else:
    ## 哈哈 浏览器也可以 无界面
    option = webdriver.FirefoxOptions()
    option.add_argument("--headless")
    browser = webdriver.Firefox(options=option)

browser.set_window_size(1000, 800)
browser.set_page_load_timeout(10)  ##设置超时时间


browser.get("http://devdoc.xiaoyouapp.cn/publics/apiList")


browser.save_screenshot('123.png')
print(time.time())


browser.quit()    #quit退出浏览器
