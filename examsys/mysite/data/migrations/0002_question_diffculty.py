# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='diffculty',
            field=models.CharField(max_length=5, null=True, blank=True),
        ),
    ]
