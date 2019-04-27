# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-07-11 16:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0015_author_detail_show_on_main_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='want_to_join',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('mobile', models.CharField(max_length=15)),
                ('message', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
