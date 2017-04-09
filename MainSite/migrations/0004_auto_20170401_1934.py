# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-01 17:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainSite', '0003_auto_20170401_1913'),
    ]

    operations = [
        migrations.CreateModel(
            name='Harmonogram_Zespol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IdZ_0', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainSite.Harmonogram_Startow')),
                ('IdZawody', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainSite.Zespol')),
            ],
        ),
        migrations.RemoveField(
            model_name='zespol_zawody',
            name='Wyniki',
        ),
        migrations.AlterField(
            model_name='zespol_zawody',
            name='IdZ_0',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainSite.Zespol'),
        ),
        migrations.AlterField(
            model_name='zespol_zawody',
            name='IdZawody',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainSite.Zawody'),
        ),
    ]
