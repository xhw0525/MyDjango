# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from myapp.models import BugTag

# Create your views here.
browser = None


def hello(request):
    # tags =BugTag(name='你好bug')
    # tags.save()
    names = BugTag.objects.get(id =1)
    name = names.name

    return render(request, 'hello.html', {'nihao': '你好啊啊啊' + name})


