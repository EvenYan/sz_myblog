# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-12-06 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_created_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('boy_num', models.PositiveIntegerField(default=40)),
                ('girl_num', models.PositiveIntegerField(default=50)),
            ],
        ),
    ]