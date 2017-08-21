# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0003_auto_20170812_0639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngo',
            name='link',
            field=models.URLField(blank=True),
        ),
    ]
