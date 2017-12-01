#coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MyDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('booktest.urls')),
    #这样加静态路径后自带服务器调试时   浏览器可以直接访问静态路径下的资源 仅限(CSS, JavaScript, Images)
    # url(r'^staticroot/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
    # url(r'^staticfiles/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATICFILES_DIRS[0]}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT}),

)
