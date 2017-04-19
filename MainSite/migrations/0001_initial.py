# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-19 15:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Adres',
            fields=[
                ('IdAdres', models.AutoField(primary_key=True, serialize=False)),
                ('Ulica', models.CharField(max_length=255)),
                ('Numer', models.CharField(max_length=30)),
                ('Mieszkanie', models.CharField(max_length=30)),
                ('KodPocztowy', models.CharField(max_length=30, verbose_name='Kod Pocztowy')),
                ('Miejscowosc', models.CharField(max_length=255, verbose_name='Miejscowość')),
            ],
            options={
                'verbose_name_plural': 'Adresy',
            },
        ),
        migrations.CreateModel(
            name='Artykul',
            fields=[
                ('IdArtykul', models.AutoField(primary_key=True, serialize=False)),
                ('tytul', models.CharField(max_length=30, verbose_name='Tytuł')),
                ('tresc', models.CharField(max_length=1000, verbose_name='Treść')),
                ('IdAdmin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Artykuły',
            },
        ),
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('IdZdjecia', models.AutoField(primary_key=True, serialize=False)),
                ('Zdjecie', models.FileField(upload_to='')),
                ('IdAdmin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Galeria',
            },
        ),
        migrations.CreateModel(
            name='Harmonogram_Startow',
            fields=[
                ('IdHS', models.AutoField(primary_key=True, serialize=False)),
                ('Opis', models.CharField(max_length=256)),
                ('Data', models.DateTimeField(default=django.utils.timezone.now)),
                ('Czas', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'Harmonogram Startów',
            },
        ),
        migrations.CreateModel(
            name='Harmonogram_Zawodow',
            fields=[
                ('IdH', models.AutoField(primary_key=True, serialize=False, verbose_name='Numer identyfikacyjny harmonogramu')),
                ('Opis', models.CharField(max_length=256, verbose_name='Opis wydarzenia')),
                ('Termin', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Termin wykonania')),
            ],
            options={
                'verbose_name_plural': 'Harmonogram Zawodów',
            },
        ),
        migrations.CreateModel(
            name='Harmonogram_Zespol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IdZ_0', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainSite.Harmonogram_Startow', verbose_name='Identyfikator startu')),
            ],
            options={
                'verbose_name_plural': 'Harmonogram zespołów',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Uczelnia', models.CharField(max_length=255)),
                ('Email', models.CharField(max_length=255)),
                ('Telefon', models.CharField(max_length=30)),
                ('Adres', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainSite.Adres')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Wyniki_Zawodow',
            fields=[
                ('IdWynikow', models.AutoField(primary_key=True, serialize=False)),
                ('Czas', models.DateTimeField(default=django.utils.timezone.now)),
                ('IdHs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainSite.Harmonogram_Startow', verbose_name='Numer wyścigu')),
            ],
            options={
                'verbose_name_plural': 'Wyniki zawodów',
            },
        ),
        migrations.CreateModel(
            name='Zawodnik',
            fields=[
                ('IdZ', models.AutoField(primary_key=True, serialize=False)),
                ('Imie', models.CharField(max_length=30)),
                ('Nazwisko', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Zawodnicy',
            },
        ),
        migrations.CreateModel(
            name='Zawody',
            fields=[
                ('IdZawody', models.AutoField(primary_key=True, serialize=False)),
                ('Nazwa', models.CharField(max_length=30, verbose_name='Nazwa zespołu')),
            ],
            options={
                'verbose_name_plural': 'Zawody',
            },
        ),
        migrations.CreateModel(
            name='Zespol',
            fields=[
                ('IdZ', models.AutoField(primary_key=True, serialize=False)),
                ('Nazwa', models.CharField(max_length=30)),
                ('Typ', models.CharField(max_length=30)),
                ('IdHS', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainSite.Harmonogram_Startow', verbose_name='Identyfikator startów')),
                ('IdU', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Zespoły',
            },
        ),
        migrations.CreateModel(
            name='Zespol_Zawody',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IdZ_0', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainSite.Zespol', verbose_name='Identyfikator zespołu')),
                ('IdZawody', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainSite.Zawody', verbose_name='Identyfikator zawodów')),
            ],
            options={
                'verbose_name_plural': 'Zespoły w zawodach',
            },
        ),
        migrations.AddField(
            model_name='zawodnik',
            name='IdZ_0',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainSite.Zespol'),
        ),
        migrations.AddField(
            model_name='wyniki_zawodow',
            name='IdZawody',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainSite.Zespol', verbose_name='Identyfikator zawodów'),
        ),
        migrations.AddField(
            model_name='harmonogram_zespol',
            name='IdZawody',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainSite.Zespol', verbose_name='Identyfikator zespołu'),
        ),
        migrations.AddField(
            model_name='harmonogram_zawodow',
            name='IdZawody',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainSite.Zawody', verbose_name='Numer zawodów'),
        ),
        migrations.AddField(
            model_name='galeria',
            name='IdZawody',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainSite.Zawody'),
        ),
    ]
