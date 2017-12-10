# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.common.proxy import Proxy,ProxyType
print(time.time())

service_args=[]
# service_args.append('--load-images=no')  ##关闭图片加载
# service_args.append('--disk-cache=yes')  ##开启缓存
# service_args.append('--ignore-ssl-errors=true') ##忽略https错误
# service_args.append('--proxy=127.0.0.1:9999')  # 代理
# service_args.append('--proxy-type=http')  # 代理
browser = webdriver.PhantomJS('/Users/xhw/PythonU/phantomjs-2.1.1-macosx/bin/phantomjs', service_args=service_args)
browser.set_window_size(1000, 800)
browser.set_page_load_timeout(10)  ##设置超时时间

# 利用DesiredCapabilities(代理设置)参数值，重新打开一个sessionId，我看意思就相当于浏览器清空缓存后，加上代理重新访问一次url
proxy=Proxy()
proxy.proxy_type=ProxyType.MANUAL
proxy.http_proxy='119.5.37.182:808'
# 将代理设置添加到webdriver.DesiredCapabilities.PHANTOMJS中
proxy.add_to_capabilities(webdriver.DesiredCapabilities.PHANTOMJS)
browser.start_session(webdriver.DesiredCapabilities.PHANTOMJS)

browser.get("http://devdoc.xiaoyouapp.cn/publics/apiList")
print(browser.session_id)
browser.save_screenshot('使用代理访问的.png')
print(time.time())
browser.quit()    #quit退出浏览器
