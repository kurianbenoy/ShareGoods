# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-07-29 02:48
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usernames',
            name='aadhar_no',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(999999999999)]),
        ),
    ]