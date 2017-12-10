#-*-coding:utf-8 -*-
import urllib2,codecs,urllib,socket
from bs4 import BeautifulSoup
import threadpool

def get_proxys(url = '', file_path = ''):
    User_Agent = 'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10'
    header = {}
    header['User-Agent'] = User_Agent

    req = urllib2.Request(url,headers=header)
    res = urllib2.urlopen(req).read()

    soup = BeautifulSoup(res)
    ips = soup.findAll('tr')
    f = codecs.open(file_path,"w", 'utf-8')

    for x in range(1, len(ips)):
        ip = ips[x]
        tds = ip.findAll("td")
        ip_temp = tds[1].contents[0]+"\t"+tds[2].contents[0]+"\n"
        f.write(ip_temp)
    f.close()


def check_proxys(file_path = ''):
    socket.setdefaulttimeout(2)
    f = open(file_path)
    fd_proxy = codecs.open("../result/可用代理.txt", "a+", 'utf-8')
    oklines = fd_proxy.readlines()
    lines = f.readlines()
    proxys = []
    for i in range(0, len(lines)):
        ip = lines[i].strip("\n").split("\t")
        #去重
        if [line.find(ip[0]) for line in oklines if line.find(ip[0])]:
            continue
        proxy_host = "http://" + ip[0] + ":" + ip[1]
        proxy_temp = {"http":proxy_host}
        proxys.append(proxy_temp)
    url = "http://ip.chinaz.com/getip.aspx"
    for proxy in proxys:
        try:
            res = urllib.urlopen(url, proxies=proxy).read()
            fd_proxy.write(proxy["http"]+"\n")
            fd_proxy.flush()
            print 'success->', res
        except Exception, e:
            print proxy
            print e
            continue
    f.close()
    fd_proxy.close()


def start_run(url, file_path):
    print('url  ', url, 'file_path  ',file_path)
    # get_proxys(url, file_path)
    check_proxys(file_path)

parms = []
for i in range(1,100):
    file_path = "../result/所有代理"+str(i)+".txt"
    url = 'http://www.xicidaili.com/nn/'+ str(i)
    parm = (None, {'url': url,'file_path': file_path})
    parms.append(parm)




pool = threadpool.ThreadPool(10)
requests = threadpool.makeRequests(start_run, parms)
[pool.putRequest(req) for req in requests]
pool.wait()

