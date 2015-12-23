# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_auto_20151023_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='markandpos',
            name='mark',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='markandpos',
            name='pos',
            field=models.CharField(max_length=10, blank=True),
        ),
    ]
