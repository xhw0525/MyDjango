# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import method
print(time.time())


#----------------------------------------------------------------------------

dc = webdriver.DesiredCapabilities.PHANTOMJS
dc["phantomjs.page.settings.userAgent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0.1 Safari/604.3.5"
dc["phantomjs.page.settings.accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
dc["phantomjs.page.customHeaders.Cookie"] ='io=uQ3YyzbLDHeSeL0dRmG4; app_id=1582738981259327; Hm_lpvt_faf40d1dd41f0d73bf8a504980865f5c=1512741821; Hm_lvt_faf40d1dd41f0d73bf8a504980865f5c=1512351327,1512523919,1512725477,1512734929; access_token=AJINIKVjFfMTU3NTA2MzY3MzM3ODUzNF9NVGs0TWpjd01ESTFNa0J4Y1M1amIyMD1fMTIwMmJjMjgyZjJhMWI4MDdlMWU1NjIzYjlhODMwNWJfMTUxNTMzMTM5MQ%3D%3D; user_id=1575063673378534; gr_user_id=51f8976c-c270-4c44-b291-f91be40842d7'

browser = webdriver.PhantomJS('/Users/xhw/PythonU/phantomjs-2.1.1-macosx/bin/phantomjs', desired_capabilities=dc, service_log_path='./log/geckodriver.log')
# browser = webdriver.Safari()
browser.set_window_size(1000, 800)
browser.implicitly_wait(30) #隐式等待
browser.set_page_load_timeout(60)  ##超时时间

# method.get_detail(browser,id='1585492539749572')
'1529581119996976' #缘分吧
'1582738981259327' #小友

method.get_Main(browser, id=u'1529581119996976', load_pages=1, load_all=True, load_user=True,max_tags=2, detay_rand=0)
