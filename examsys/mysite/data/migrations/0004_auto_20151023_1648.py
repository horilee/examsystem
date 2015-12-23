# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20151023_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='point',
            name='questions',
        ),
        migrations.AddField(
            model_name='point',
            name='questions',
            field=models.ManyToManyField(to='data.Question', null=True, blank=True),
        ),
    ]
