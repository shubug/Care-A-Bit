# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='donorprofile',
            name='date_joined',
            field=models.DateTimeField(default=datetime.date(2017, 8, 13), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='donorprofile',
            name='is_active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='donorprofile',
            name='total_donation',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='donorprofile',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
            preserve_default=True,
        ),
    ]
