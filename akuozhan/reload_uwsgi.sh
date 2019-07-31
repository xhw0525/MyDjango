#!/bin/sh
NAME="uwsgi_ubuntu"
if [ ! -n "$NAME" ];then
    echo "no arguments"
    exit;
fi

echo $NAME
ID=`ps -ef | grep "$NAME" | grep -v "$0" | grep -v "grep" | awk '{print $2}'`
echo $ID
echo "MyDjango uwsgi restart..."
for id in $ID
do
kill -9 $id
echo "kill $id"
done
echo  "sleep 3s"
sleep 3
uwsgi --ini ~/works/ZChatProject/akuozhan/uwsgi_ubuntu.ini