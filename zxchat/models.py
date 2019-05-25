# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Create your models here.

# noinspection PyInterpreter
class ZXChatModel(models.Model):
    username = models.CharField(max_length=50)

    def __str__(self):
        return self.username.encode("utf-8")



class ZXUserModel(models.Model):
    username = models.CharField(max_length=50)

    def __str__(self):
        return self.username.encode("utf-8")