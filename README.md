# MyDjango

# 新建项目
# python manage.py startproject project_name

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



命令行 ngnix uwsgi django组合
#   python manage.py collectstatic
#   sudo /etc/init.d/nginx start
#   uwsgi --ini ~/uftp/MyDjango/MyDjango_uwsgi.ini
#   编辑网站站点
#   sudo vim /etc/nginx/sites-enabled/myngnix_site


pip查询    pip list --format=columns


 python manage.py makemigrations --empty myapp
