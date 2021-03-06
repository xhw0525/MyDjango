# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
from django.contrib import admin
from myapp.models import *
from myapp.views import custom_page
from django.http.request import HttpRequest

#
# admin.site.site_title = 'MD后台管理系统'
# # # 放在每个管理页面末尾的<title>，默认情况下是“Django站点管理员”
# admin.site.site_header = 'MD后台管理系统'
# # # 放在每个管理页面顶部的<h1>文本，默认情况下是“Django管理”
# admin.site.index_title = 'MD后台产品管理'
#
# # 管理员索引页面顶部的文本，默认情况下是“站点管理”
# # admin.site.site_url = ''
# # 管理页面顶部“查看网站”链接的URL，默认情况下是/，将其设置None将删除链接



# Register your models here.
@admin.register(MyUserModel)
class MyUserModelAdmin(admin.ModelAdmin):
    # 列表要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ['username', 'phone', 'sex', 'signature', 'nickname']

    # 列表点进去后的编辑内容; 还可以多个字段显示在一行。
    fields = ['username', 'phone', ('sex', 'signature')]

    # 列表 直接激活编辑
    list_editable = ['phone', ]
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50

    # 右侧过滤器
    list_filter = ('sex',)
    # 搜索字段
    search_fields = ('username', 'phone',)

    def get_readonly_fields(self, request: HttpRequest, obj=None):
        only_reads: list = []
        if not request.path.endswith('/add/'):  # 非添加时, 禁止修改用户名
            only_reads.append('username')
        return [f.name for f in self.model._meta.fields if (only_reads.__contains__(f.name))]


@admin.register(MyChatModel)
class ZXAutoReplyModelAdmin(admin.ModelAdmin):
    list_display = ['username', ]


@admin.register(CustomPageView)
class FeedbackStatsAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_content=None):
        return custom_page(request)
