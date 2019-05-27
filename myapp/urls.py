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
import myapp.views as views
from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet) #集合视图使用这种路由

# 使用自动化URL路由，转配我们的API.
# 如有额外需要, 我也为可视化API添加了登陆URLs.
urlpatterns = [
    # url(r'^adduser$', views.adduser, name='adduser'),
    # url(r'^updateuser$', views.updateuser, name='updateuser'),
    # url(r'^getuser$', views.getuser, name='getuser'),
    url(r'^', include(router.urls)),

    url(r'^ApiViewDemo$', views.ApiViewDemo.as_view()),
    url(r'^hello_world$', views.hello_world, name='hello_world'),

    url(r'^docs/', include_docs_urls(title="myapp")),
    url('^.*', views.hello, name=''),

]

