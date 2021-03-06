# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-07-09 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_auto_20170709_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_detail',
            name='show_on_main_page',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=5),
        ),
        migrations.AlterField(
            model_name='book_detail',
            name='competitive_exam',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=5),
        ),
        migrations.AlterField(
            model_name='book_detail',
            name='new_release',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=5),
        ),
        migrations.AlterField(
            model_name='book_detail',
            name='upcoming_book',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=5),
        ),
    ]
