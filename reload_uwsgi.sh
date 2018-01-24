#!/bin/sh
NAME="MyDjango_uwsgi"
if [ ! -n "$NAME" ];then
    echo "no arguments"
    exit;
fi

echo $NAME
ID=`ps -ef | grep "$NAME" | grep -v "$0" | grep -v "grep" | awk '{print $2}'`
echo $ID
echo "此处是不是该输出点什么"
for id in $ID
do
kill -9 $id
echo "kill $id"
done
echo  "此处是不是该输出点什么"
uwsgi --ini /home/uxhw/MyDjango/MyDjango_uwsgi.ini