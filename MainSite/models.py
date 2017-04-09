from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Zawody(models.Model):
    IdZawody = models.AutoField(primary_key=True)
    Nazwa = models.CharField(max_length=30)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Nazwa

class Artykul(models.Model):
    IdArtykul =  models.AutoField(primary_key=True)
    IdAdmin =  models.ForeignKey('auth.User')
    tytul = models.CharField(max_length = 30)
    tresc = models.CharField(max_length = 1000)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.tytul

class Harmonogram_Zawodow(models.Model):
    IdH = models.AutoField(primary_key=True)
    IdZawody = models.ForeignKey(Zawody, on_delete=models.CASCADE)
    Opis = models.CharField(max_length=256)
    Termin = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Opis


class Harmonogram_Startow(models.Model):
    IdHS = models.AutoField(primary_key=True)
    Opis = models.CharField(max_length=256)
    Data = models.DateTimeField(default=timezone.now)
    # TODO: Zdefiniować co oznacza czas
    Czas = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Opis


class Adres(models.Model):
    IdAdres = models.AutoField(primary_key=True)
    Ulica = models.CharField(max_length=255)
    Numer = models.CharField(max_length=30)
    Mieszkanie = models.CharField(max_length=30)
    KodPocztowy = models.CharField(max_length=30)
    Miejscowosc = models.CharField(max_length=255)


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # The additional attributes we wish to include.
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
    IdHS = models.ForeignKey(Harmonogram_Startow,on_delete=models.CASCADE)
    Nazwa = models.CharField(max_length=30)
    Typ = models.CharField(max_length=30)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Nazwa


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


class Zespol_Zawody(models.Model):
    IdZ_0 = models.ForeignKey(Zespol,on_delete=models.CASCADE)
    IdZawody = models.ForeignKey(Zawody, on_delete=models.CASCADE)


class Wyniki_Zawodow(models.Model):
    IdWynikow =  models.AutoField(primary_key=True)
    IdHs = models.ForeignKey(Harmonogram_Startow,on_delete=models.CASCADE)
    IdZawody = models.ForeignKey(Zespol, on_delete=models.CASCADE)
    Czas = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.IdWynikow


class Galeria(models.Model):
    IdZdjecia =  models.AutoField(primary_key=True)
    Zdjecie = models.FileField()
    IdAdmin = models.ForeignKey('auth.User') # Zobacz w panelu admina,admin to user tylko z uprawnieniami
    IdZawody = models.ForeignKey(Zawody, on_delete=models.CASCADE)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.IdZdjecia

class Harmonogram_Zespol(models.Model):
    IdZ_0 = models.ForeignKey(Harmonogram_Startow,on_delete=models.CASCADE)
    IdZawody = models.ForeignKey(Zespol, on_delete=models.CASCADE)
