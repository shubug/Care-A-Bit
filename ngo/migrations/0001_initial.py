# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ngo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('link', models.URLField()),
                ('total_contrib', models.IntegerField(default=0)),
                ('last_contrib', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Ngo',
                'verbose_name_plural': 'Ngos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NgoCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('num_of_contrib', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Ngocategory',
                'verbose_name_plural': 'NgoCategories',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='ngo',
            name='category',
            field=models.ForeignKey(blank=True, to='ngo.NgoCategory', null=True),
            preserve_default=True,
        ),
    ]
