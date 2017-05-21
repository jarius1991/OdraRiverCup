# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 12:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('MainSite', '0008_merge_20170508_1422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wyniki_zawodow',
            name='IdZespol',
        ),
        migrations.AddField(
            model_name='wyniki_zawodow',
            name='IdZespolu',
            field=models.ForeignKey(default=0, on_delete=django.db.models.fields.CharField, to='MainSite.Zespol', verbose_name='Identyfikator zespolu'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='wyniki_zawodow',
            name='Czas',
            field=models.CharField(default='00:00:000', max_length=20),
        ),
        migrations.AlterField(
            model_name='wyniki_zawodow',
            name='IdZawody',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainSite.Zawody', verbose_name='Identyfikator zawodów'),
        ),
    ]