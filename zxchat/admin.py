# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
from django.contrib import admin
from zxchat.models import *
from zxchat.views import custom_page


# Register your models here.

class ZXUserModelAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ['username', 'phone', 'sex', 'signature', 'nickname', 'type',
                    'status', 'ctime', 'mtime', 'activetime', 'is_service','isok' ]
    # 直接激活
    list_filter = ('is_service', 'status',)

    # 还可以多个字段显示在一行。(比 list_display优先级高)
    fields = ['username', 'phone', ('sex', 'signature'),'isok']

    # 那些字段能直接修改
    list_editable = ['activetime', ]
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50

    # 筛选器
    # list_filter =('username', 'is_service',) #过滤器
    search_fields = ('username', 'signature',)  # 搜索字段

    def get_readonly_fields(self, request, obj=None):
        only_reads = ['username']

        # ...

        return [f.name for f in self.model._meta.fields if (only_reads.__contains__(f.name))]





admin.site.register(ZXUserModel, ZXUserModelAdmin)


# admin.site.site_title='hahah'


@admin.register(ZXAutoReplyModel)
class ZXAutoReplyModelAdmin(admin.ModelAdmin):
    list_display = ['username', 'replyText1', 'replyText2', 'replyImage', ]


@admin.register(CustomPageView)
class FeedbackStatsAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_content=None):
        return custom_page(request)
