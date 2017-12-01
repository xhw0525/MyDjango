# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0002_auto_20171028_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinfo',
            name='shijian',
            field=models.TimeField(),
            preserve_default=True,
        ),
    ]
