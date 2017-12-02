# MyDjango

# 新建app
# python manage.py startapp app_name

#   开启服务
#   python manage.py runserver 8000
#   python manage.py runserver 0.0.0.0:8000

#   清空数据库
#   python manage.py flush

#   1.创建更改的文件 2.将生成的更改的文件应用到数据库
#   python manage.py makemigrations
#   python manage.py migrate

#   创建超级管理员
#   python manage.py createsuperuser

#   数据库命令行
#   python manage.py dbshell

#   Django 项目环境终端python manage.py shell
#

#   导出数据 导入数据
#   python manage.py dumpdata appname > appname.json
#   python manage.py loaddata appname.json


#   python manage.py collectstatic



命令行
    sudo /etc/init.d/nginx start

    uwsgi --ini ~/uftp/MyDjango/MyDjango_uwsgi.ini

    sudo vim /etc/nginx/sites-enabled/MyDjango



    Ubuntu Python 2.7.9  django 1.7.6