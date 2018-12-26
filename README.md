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
or
先 python manage.py makemigrations [appname]
再 python manage.py migrate [appname]



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

#   收集静态文件
#   python manage.py collectstatic
#   sudo /etc/init.d/nginx start
#   uwsgi --ini ~/uftp/MyDjango/MyDjango_uwsgi.ini
#   编辑网站站点
#   sudo vim /etc/nginx/sites-enabled/myngnix_site



centos:
启动
[root@localhost ~]# /usr/local/nginx/sbin/nginx
停止/重启
[root@localhost ~]# /usr/local/nginx/sbin/nginx -s stop(quit、reload)
命令帮助
[root@localhost ~]# /usr/local/nginx/sbin/nginx -h
验证配置文件
[root@localhost ~]# /usr/local/nginx/sbin/nginx -t
配置文件
[root@localhost ~]# vim /usr/local/nginx/conf/nginx.conf




pip查询    pip list --format=columns


 python manage.py makemigrations --empty myapp

scp指定端口
sudo scp -P 26897 -r /Users/xhw/Downloads/pip-9.0.1.tar.gz  xhw@176.122.128.5:/home/xhw

Ubuntu 取消 Apache及Nginx等开机自启动
1、   sudo update-rc.d -f nginx remove 删除nginx随机器启动的服务
 　　sudo update-rc.d -f apache2 remove 删除apache2随机器启动的服务

2、 查看/etc/rc2.d/里面的apache和nginx启动脚本，通常都是【一个英文字母 + 两个阿拉伯数字 + 脚本名称】。
    英文字母是S的都是会自动启动的，K则相反。所以只要找到apache和nginx的启动脚本，把S改成K就可以了。


ubuntu安装完Nginx后，文件结构大致为：
　　所有的配置文件都在 /etc/nginx下；
　　启动程序文件在 /usr/sbin/nginx下；
　　日志文件在 /var/log/nginx/下，分别是access.log和error.log；
　　并且在 /etc/init.d下创建了启动脚本nginx
sudo /etc/init.d/nginx start    # 启动
sudo /etc/init.d/nginx stop     # 停止
sudo /etc/init.d/nginx restart  # 重启

uwsgi --ini MyDjango_uwsgi.ini
./reload_uwsgi.sh  #自己脚本  用于重启uwsgi


收集Django静态文件
把Django自带的静态文件收集到同一个static中，不然访问Django的admin页面会找不到静态文件。在django的setting文件中，添加下面一行内容：
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
然后到项目目录下执行:
python manage.py collectstatic
修改配置文件
DEBUG = False
ALLOWED_HOSTS = ['*']
