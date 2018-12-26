#!/bin/sh
NAME="uwsgi_centos"
if [ ! -n "$NAME" ];then
    echo "no arguments"
    exit;
fi

echo $NAME
ID=`ps -ef | grep "$NAME" | grep -v "$0" | grep -v "grep" | awk '{print $2}'`
echo $ID
echo "MyDjango uwsgi 重启中..."
for id in $ID
do
kill -9 $id
echo "kill $id"
done
echo  "3秒后启动."
sleep 3
uwsgi --ini /home/xhw/MyDjango/uwsgi_centos.ini