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

scp指定端口
sudo scp -P 29152 -r /Users/xhw/Downloads/pip-9.0.1.tar.gz  xhw@176.122.128.5:/home/xhw


ubuntu安装完Nginx后，文件结构大致为：
　　所有的配置文件都在 /etc/nginx下；
　　启动程序文件在 /usr/sbin/nginx下；
　　日志文件在 /var/log/nginx/下，分别是access.log和error.log；
　　并且在 /etc/init.d下创建了启动脚本nginx
sudo /etc/init.d/nginx start    # 启动
sudo /etc/init.d/nginx stop     # 停止
sudo /etc/init.d/nginx restart  # 重启

uwsgi --ini MyDjango_uwsgi.ini
uwsgi --ini uwsgi.ini             # 启动
uwsgi --reload uwsgi.pid          # 重启
uwsgi --stop uwsgi.pid            # 关闭


收集Django静态文件
把Django自带的静态文件收集到同一个static中，不然访问Django的admin页面会找不到静态文件。在django的setting文件中，添加下面一行内容：
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
然后到项目目录下执行:
python manage.py collectstatic
修改配置文件
DEBUG = False
ALLOWED_HOSTS = ['*']
