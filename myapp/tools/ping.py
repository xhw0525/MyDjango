# -*- coding: utf-8 -*-
import threading,subprocess
from time import ctime,sleep,time
import Queue
queue=Queue.Queue()
for i in range(2,254):
    host = '172.16.1.'+str(i)
    ret = subprocess.call('ping -c 1 -W 0.1 ' + host, shell=True, stdout=open('/dev/null', 'w'))
    if ret:
        print "%s is down" % host
    else:
        print "%s is up" % host
