# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0005_auto_20170813_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngocategory',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
