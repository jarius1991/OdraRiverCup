# -*- coding: UTF-8 -*-
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Zawody(models.Model):
    IdZawody = models.AutoField(primary_key=True )
    Nazwa = models.CharField(max_length=30, verbose_name="Nazwa zespołu")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Nazwa
    class Meta:

        verbose_name_plural="Zawody"

class Artykul(models.Model):
    IdArtykul =  models.AutoField(primary_key=True)
    IdAdmin =  models.ForeignKey('auth.User')
    tytul = models.CharField(max_length = 30, verbose_name="Tytuł")
    tresc = models.TextField(max_length = 1000, verbose_name="Treść")#Rozwarzyć zamane na TextField -> lepsze wprowadzanie danych, inny rozkład
    data = models.DateTimeField(auto_now_add=True)

    def publish(self):
        self.data = timezone.now()
        self.save()

    def __str__(self):
        return self.tytul

    class Meta:
        #ordering = ('-published_date',)#jak przechowywana jest data publikacji? Według czego porządkujemy.
        verbose_name_plural="Artykuły"


class Wiadomosci(models.Model):
    email=models.CharField(max_length=255)
    tresc=models.TextField(max_length = 1000, verbose_name="Treść")

    def __str__(self):
        return self.email + ":  "+ self.tresc[:20]

    class Meta:
        verbose_name_plural="Wiadomości"

class Harmonogram_Zawodow(models.Model):
    IdH = models.AutoField(primary_key=True, verbose_name="Numer identyfikacyjny harmonogramu")
    IdZawody = models.ForeignKey(Zawody, on_delete=models.CASCADE, verbose_name="Numer zawodów")
    Opis = models.CharField(max_length=256, verbose_name="Opis wydarzenia")
    Termin = models.DateTimeField(default=timezone.now, verbose_name="Termin wykonania")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Opis

    class Meta:

        verbose_name_plural="Harmonogram Zawodów"


class Harmonogram_Startow(models.Model):
    IdHS = models.AutoField(primary_key=True)
    Opis = models.CharField(max_length=256)
    Data = models.DateTimeField(default=timezone.now) #Dzień w którym odbywają się dane starty
    # TODO: Zdefiniować co oznacza czas  -> godzina startu (pojednyczy bieg)
    Czas = models.DateTimeField(default=timezone.now)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Opis


    class Meta:

        verbose_name_plural="Harmonogram Startów"


class Adres(models.Model):
    IdAdres = models.AutoField(primary_key=True)
    Ulica = models.CharField(max_length=255)
    Numer = models.CharField(max_length=30)
    Mieszkanie = models.CharField(max_length=30)
    KodPocztowy = models.CharField(max_length=30, verbose_name="Kod Pocztowy")
    Miejscowosc = models.CharField(max_length=255, verbose_name="Miejscowość")

    class Meta:
        verbose_name_plural="Adresy"


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Uczelnia = models.CharField(max_length=255)
    Adres = models.ForeignKey(Adres, on_delete=models.CASCADE)
    Email = models.CharField(max_length=255)
    Telefon = models.CharField(max_length=30)

    def __unicode__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

class Zespol(models.Model):
    IdZ = models.AutoField(primary_key=True)
    IdU = models.ForeignKey('auth.User')
    IdHS = models.ForeignKey(Harmonogram_Startow,
                             on_delete=models.CASCADE,
                             verbose_name="Identyfikator startów")
    Nazwa = models.CharField(max_length=30)
    # ToDo Określić wybór zespołów z okreslonego odgórnie zbioru
    Typ = models.CharField(max_length=30)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Nazwa


    class Meta:

        verbose_name_plural="Zespoły"


class Zawodnik(models.Model):
    IdZ = models.AutoField(primary_key=True)
    Imie = models.CharField(max_length = 30)
    Nazwisko = models.CharField(max_length = 30)
    IdZ_0 = models.ForeignKey(Zespol,on_delete=models.CASCADE)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Imie

    class Meta:

        verbose_name_plural="Zawodnicy"


class Zespol_Zawody(models.Model):
    IdZ_0 = models.ForeignKey(Zespol,on_delete=models.CASCADE, verbose_name="Identyfikator zespołu")
    IdZawody = models.ForeignKey(Zawody, on_delete=models.CASCADE, verbose_name="Identyfikator zawodów")

    class Meta:
        verbose_name_plural="Zespoły w zawodach"



class Wyniki_Zawodow(models.Model):
    IdWynikow =  models.AutoField(primary_key=True)
    IdHs = models.ForeignKey(Harmonogram_Startow,on_delete=models.CASCADE, verbose_name="Numer wyścigu")
    IdZawody = models.ForeignKey(Zespol, on_delete=models.CASCADE, verbose_name="Identyfikator zawodów")
    Czas = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.IdWynikow

    class Meta:

        verbose_name_plural="Wyniki zawodów"


class Galeria(models.Model):
    IdZdjecia =  models.AutoField(primary_key=True)
    Zdjecie = models.ImageField(upload_to='galeria')
    IdAdmin = models.ForeignKey('auth.User') # Zobacz w panelu admina,admin to user tylko z uprawnieniami
    IdZawody = models.ForeignKey(Zawody, on_delete=models.CASCADE)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.IdZdjecia)

    class Meta:

        verbose_name_plural="Galeria"

class Harmonogram_Zespol(models.Model):
    IdZ_0 = models.ForeignKey(Harmonogram_Startow,on_delete=models.CASCADE, verbose_name="Identyfikator startu")
    IdZawody = models.ForeignKey(Zespol, on_delete=models.CASCADE, verbose_name="Identyfikator zespołu")

    class Meta:

        verbose_name_plural="Harmonogram zespołów"
