# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class MyInfo(models.Model):
    name = models.CharField(max_length=50)
    jiage = models.CharField(max_length=50)
    shijian = models.TimeField()

    def __str__(self):
        return self.name.encode("utf-8")

class BugTag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name.encode("utf-8")