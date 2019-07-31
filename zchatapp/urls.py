# -*- coding: utf-8 -*-
"""MyDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from zchatapp.views import view_main, view_user
from django.conf.urls import url, include

# 使用自动化URL路由，转配我们的API.
# 如有额外需要, 我也为可视化API添加了登陆URLs.
urlpatterns = [
    url(r'^add_user$', view_user.add_user, name='add_user'),
    url(r'^save_beizhu$', view_user.save_beizhu, name='save_beizhu'),
    url(r'^get_user$', view_user.get_user, name='get_user'),
    url(r'^get_users$', view_user.get_users, name='get_users'),
    url(r'^update_user$', view_user.update_user, name='update_user'),
    url(r'^upload_image$', view_user.upload_image, name='upload_image'),
    url(r'^update_lasttime$', view_user.update_lasttime, name='update_lasttime'),
    url(r'^forget_password$', view_user.forget_password, name='forget_password'),
    url(r'^get_kefu$', view_user.get_kefu, name='get_kefu'),
    url(r'^login$', view_main.login, name='login'),
    url(r'^get_auto_reply$', view_main.get_auto_reply, name='get_auto_reply'),

    url(r'^custom_page$', view_main.custom_page, name='custom_page'),

]
