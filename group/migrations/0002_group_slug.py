# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-29 12:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='slug',
            field=models.SlugField(allow_unicode=True, default=1212, unique=True),
            preserve_default=False,
        ),
    ]
