from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MyDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^staticroot/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
    url(r'^staticfiles/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATICFILES_DIRS[0]}),
    url(r'^', include('booktest.urls')),
)
