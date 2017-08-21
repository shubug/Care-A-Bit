# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0004_auto_20170813_0701'),
    ]

    operations = [
        migrations.AddField(
            model_name='ngo',
            name='slug',
            field=models.SlugField(default=b'xxxngoxxx'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ngocategory',
            name='slug',
            field=models.SlugField(default=b'xxxngocatxxx'),
            preserve_default=True,
        ),
    ]
