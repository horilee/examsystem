# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0019_auto_20151121_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='college',
            field=models.CharField(blank=True, max_length=20, null=True, choices=[(b'sc', b'\xe8\xae\xa1\xe7\xae\x97\xe6\x9c\xba\xe5\xad\xa6\xe9\x99\xa2'), (b'sw', b'\xe8\xbd\xaf\xe4\xbb\xb6\xe5\xad\xa6\xe9\x99\xa2')]),
        ),
    ]
