# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-07-14 09:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0022_author_detail_recommendation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_detail',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
