# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
from django.contrib import admin
from zxchat.models import *
from zxchat.views import custom_page


# Register your models here.
class ZXUserModelAdmin(admin.ModelAdmin):
    # 列表要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ['username', 'phone', 'sex', 'signature', 'nickname', 'type',
                    'status', 'ctime', 'mtime', 'activetime', 'is_service', 'isok']

    # 列表点进去后的编辑内容; 还可以多个字段显示在一行。
    fields = ['username', 'phone', ('sex', 'signature'), ]

    # 列表 直接激活编辑
    list_editable = ['activetime', ]
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50

    # 右侧过滤器
    list_filter = ('is_service', 'status',)
    # 搜索字段
    search_fields = ('username', 'signature',)

    def get_readonly_fields(self, request, obj=None):
        only_reads = ['username']

        # ...

        return [f.name for f in self.model._meta.fields if (only_reads.__contains__(f.name))]


admin.site.register(ZXUserModel, ZXUserModelAdmin)



@admin.register(ZXAutoReplyModel)
class ZXAutoReplyModelAdmin(admin.ModelAdmin):
    list_display = ['username', 'replyText1', 'replyText2', 'replyImage', ]


@admin.register(CustomPageView)
class FeedbackStatsAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_content=None):
        return custom_page(request)
