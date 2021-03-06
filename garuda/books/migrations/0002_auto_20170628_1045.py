# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-28 10:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author_detail',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author_detail',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
