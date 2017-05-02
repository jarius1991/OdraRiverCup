from django.contrib import admin
from .models import *

class ZawodyAdmin(admin.ModelAdmin):
    list_display = ['Nazwa']
    search_fields = ['Nazwa']
    ordering = ['Nazwa']

class Harmonogram_ZawodowAdmin(admin.ModelAdmin):
    list_display = ['IdH', 'IdZawody', 'Opis', 'Termin']
    search_fields = ['IdH', 'IdZawody','Termin']
    list_filter = ['IdZawody','Termin']
    ordering = ['IdH', 'IdZawody', 'Termin']

class Harmonogram_StartowAdmin(admin.ModelAdmin):
    list_display = ['IdHS', 'Opis', 'Data', 'Czas']
    search_fields = ['IdHS', 'Opis',]
    list_filter = ['Data',]
    ordering = ['Opis', 'Data', 'Czas']


class ZespolAdmin(admin.ModelAdmin):
    list_display = ['IdZ', 'IdU', 'IdHS', 'Nazwa', 'Typ']
    search_fields = ['IdHS', 'Nazwa']
    list_filter = ['IdHS', 'Nazwa', 'Typ']
    ordering = ['IdZ', 'IdU', 'IdHS', 'Nazwa', 'Typ']

class ZawodnikAdmin(admin.ModelAdmin):
    list_display = ['Imie', 'Nazwisko', 'IdZ_0']
    search_fields = ['Imie', 'Nazwisko', 'IdZ_0']
    list_filter = ['IdZ_0']
    ordering = ['Imie', 'Nazwisko', 'IdZ_0']

class Zespol_ZawodyAdmin(admin.ModelAdmin):
    list_display = ['IdZ_0', 'IdZawody']
    search_fields = ['IdZ_0', 'IdZawody']
    list_filter = ['IdZ_0', 'IdZawody']

class Wyniki_ZawodowAdmin(admin.ModelAdmin):
    list_display = ['IdWynikow', 'IdHs', 'IdZawody', 'Czas']
    search_fields = ['IdWynikow', 'IdHs', 'IdZawody', 'Czas']
    list_filter = ['IdWynikow', 'IdHs', 'IdZawody', 'Czas']
    ordering = ['IdWynikow', 'IdHs', 'IdZawody', 'Czas']

class ArtykulAdmin(admin.ModelAdmin):
    list_display = ['IdArtykul', 'IdAdmin', 'tytul', 'tresc']
    search_fields = ['IdArtykul', 'IdAdmin', 'tytul', 'tresc']
    list_filter = ['IdArtykul', 'IdAdmin', 'tytul', 'tresc']
    ordering = ['IdArtykul', 'IdAdmin', 'tytul', 'tresc']

class Harmonogram_ZespolAdmin(admin.ModelAdmin):
    list_display = ['IdZ_0', 'IdZawody']
    search_fields = ['IdZ_0', 'IdZawody']
    list_filter = ['IdZ_0', 'IdZawody']
    ordering = ['IdZ_0', 'IdZawody']


admin.site.register(Zawody, ZawodyAdmin)
admin.site.register(Harmonogram_Zawodow, Harmonogram_ZawodowAdmin)
admin.site.register(Harmonogram_Startow, Harmonogram_StartowAdmin)
admin.site.register(Zespol, ZespolAdmin)
admin.site.register(Zawodnik, ZawodnikAdmin)
admin.site.register(Zespol_Zawody, Zespol_ZawodyAdmin)
admin.site.register(Wyniki_Zawodow, Wyniki_ZawodowAdmin)
admin.site.register(Galeria)
admin.site.register(Wiadomosci)
admin.site.register(Artykul, ArtykulAdmin)
admin.site.register(Harmonogram_Zespol, Harmonogram_ZespolAdmin)
