# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20151023_1648'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='author',
        ),
        migrations.AlterField(
            model_name='exam',
            name='questions',
            field=models.ManyToManyField(to='data.MarkandPos', blank=True),
        ),
    ]
