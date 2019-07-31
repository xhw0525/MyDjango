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
# from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.authtoken import views as rest_views

import MyDjango.settings as settings
from myapp.views import hello

# import debug_toolbar


urlpatterns = [
    url(r'^api_token$', rest_views.obtain_auth_token),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^admin/', admin.site.urls),
    url(r'^myapp/', include('myapp.urls')),
    url(r'^app/', include('zchatapp.urls')),
    # url(r'^wx/', include('wechat.urls',namespace="wechat")),
    url('^.*', hello, name=''),
    # 这样加静态路径后自带服务器调试时   浏览器可以直接访问静态路径下的资源 仅限(CSS, JavaScript, Images) //建议使用下面+号拼接的方式
    # url(r'^staticroot/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
    # url(r'^staticfiles/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATICFILES_DIRS[0]}),
    # url(r'^static1/(?P<path>.*)$', django.views.static.serve,{'document_root': settings.STATIC_ROOT}),
]

# 1.5之后不用加?
# # 这样加静态路径后自带服务器调试时   浏览器可以直接访问静态路径下的资源 貌似仅限(CSS, JavaScript, Images)
if settings.DEBUG:
    urlpatterns += static(u'static', document_root=settings.STATIC_ROOT)
    urlpatterns += static(u'media', document_root=settings.MEDIA_ROOT)
# else:
#     urlpatterns += static(u'static', document_root=settings.STATIC_ROOT)
#     urlpatterns += static(u'media', document_root=settings.MEDIA_ROOT)


# debug_toolbar配置 04
# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#                       url(r'^__debug__/', include(debug_toolbar.urls)),
#                   ] + urlpatterns