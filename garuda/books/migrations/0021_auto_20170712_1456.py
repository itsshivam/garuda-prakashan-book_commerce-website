# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-07-12 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0020_auto_20170712_0841'),
    ]

    operations = [
        migrations.AddField(
            model_name='author_detail',
            name='author_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book_detail',
            name='book_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
