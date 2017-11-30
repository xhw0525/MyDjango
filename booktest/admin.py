from django.contrib import admin
from models import *
# Register your models here.

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'jiage', 'shijian']

admin.site.register(BookInfo, BookInfoAdmin)
