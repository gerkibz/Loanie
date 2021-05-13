# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-15 12:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20170715_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='laon_officer',
            field=models.ForeignKey(blank=True, help_text='Someone who manages the client among your staffs', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='loan_officer', to=settings.AUTH_USER_MODEL),
        ),
    ]
