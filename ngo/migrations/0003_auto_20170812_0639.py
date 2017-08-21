# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0002_auto_20170812_0636'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ngocategory',
            old_name='name',
            new_name='domain',
        ),
    ]
