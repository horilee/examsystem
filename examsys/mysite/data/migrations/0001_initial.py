# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num', models.CharField(max_length=15)),
                ('subject', models.CharField(max_length=30)),
                ('diffculty', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('parent', models.ForeignKey(related_name='children', blank=True, to='data.Point', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num', models.CharField(max_length=15)),
                ('style', models.CharField(max_length=10)),
                ('Qmain', models.TextField()),
                ('ans', models.CharField(max_length=20)),
                ('data', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('num', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('sex', models.BooleanField()),
                ('age', models.IntegerField()),
                ('birth', models.DateField()),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('phone', models.CharField(max_length=11, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('num', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('sex', models.BooleanField()),
                ('age', models.IntegerField()),
                ('birth', models.DateField()),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('phone', models.CharField(max_length=11, blank=True)),
                ('subject', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='point',
            name='questions',
            field=models.ForeignKey(blank=True, to='data.Question', null=True),
        ),
        migrations.AddField(
            model_name='exam',
            name='author',
            field=models.ForeignKey(to='data.Teacher'),
        ),
        migrations.AddField(
            model_name='exam',
            name='questions',
            field=models.ManyToManyField(to='data.Question'),
        ),
    ]
