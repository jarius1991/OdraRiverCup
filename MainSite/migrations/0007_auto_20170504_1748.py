# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-04 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainSite', '0006_auto_20170504_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galeria',
            name='Zdjecie',
            field=models.ImageField(upload_to='galeria'),
        ),
    ]
