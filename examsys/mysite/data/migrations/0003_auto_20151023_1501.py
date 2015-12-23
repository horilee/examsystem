# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_question_diffculty'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarkandPos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mark', models.ImageField(upload_to=b'')),
                ('pos', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='StudentQAns',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('studentans', models.CharField(max_length=20)),
                ('correct', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='StuedntEAns',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mark', models.CharField(max_length=100, null=True, blank=True)),
                ('ans', models.ManyToManyField(to='data.StudentQAns')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='college',
            field=models.CharField(max_length=15, blank=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='college',
            field=models.CharField(max_length=15, blank=True),
        ),
        migrations.AlterField(
            model_name='exam',
            name='questions',
            field=models.ManyToManyField(to='data.MarkandPos'),
        ),
        migrations.AlterField(
            model_name='question',
            name='diffculty',
            field=models.CharField(max_length=5),
        ),
        migrations.AddField(
            model_name='stuednteans',
            name='student',
            field=models.ForeignKey(to='data.Student'),
        ),
        migrations.AddField(
            model_name='studentqans',
            name='question',
            field=models.ForeignKey(to='data.Question'),
        ),
        migrations.AddField(
            model_name='studentqans',
            name='student',
            field=models.ForeignKey(to='data.Student'),
        ),
        migrations.AddField(
            model_name='markandpos',
            name='question',
            field=models.ForeignKey(to='data.Question'),
        ),
    ]
