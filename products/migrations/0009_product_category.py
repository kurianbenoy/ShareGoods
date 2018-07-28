# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-07-28 17:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20180728_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.Category'),
            preserve_default=False,
        ),
    ]