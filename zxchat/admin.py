# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
from django.contrib import admin
from zxchat.models import *
from zxchat.views import custom_page


# Register your models here.

class ZXUserModelAdmin(admin.ModelAdmin):
    list_display = ['username', 'phone', 'sex', 'signature', 'year', 'head', 'nickname', 'type',
                    'status', 'ctime', 'mtime', 'stature', 'birthday', 'industry', 'education', 'is_service', ]


admin.site.register(ZXUserModel, ZXUserModelAdmin)
# admin.site.site_title='hahah'


@admin.register(CustomPageView)
class FeedbackStatsAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_content=None):
        return custom_page(request)
