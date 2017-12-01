# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinfo',
            name='jiage',
            field=models.CharField(default='2', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='shijian',
            field=models.CharField(default='1', max_length=50),
            preserve_default=False,
        ),
    ]
