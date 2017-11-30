#coding=utf-8
from django.db import models

# Create your models here.

class BookInfo(models.Model):
    name = models.CharField(max_length=50)
    jiage = models.CharField(max_length=50)
    shijian = models.TimeField()

    def __str__(self):
        return self.name.encode("utf-8")
