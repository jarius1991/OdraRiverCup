from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Zawody(models.Model):
	IdZawody = models.AutoField(primary_key=True)
	Nazwa = models.CharField(max_length=30)
    
	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.Nazwa

class Harmonogram_Zawodow(models.Model):
	IdH = models.AutoField(primary_key=True)
	IdZawody = models.ForeignKey(Zawody, on_delete=models.CASCADE)
	Opis = models.CharField(max_length=256)
	Termin = models.DateTimeField(default=timezone.now)
    
	def publish(self):
		self.published_date = timezone.now()
		self.save()
		
	def __str__(self):
		return self.IdZawody

class Harmonogram_Startow(models.Model):
	IdHS = models.AutoField(primary_key=True)
	IdZawody = models.ForeignKey(Zawody, on_delete=models.CASCADE)
	Opis = models.CharField(max_length=256)
	Data = models.DateTimeField(default=timezone.now)
	Czas = models.DateTimeField(default=timezone.now) #Zdefiniować co oznacza czas
	
	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.IdZawody

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    
    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

class Zespol(models.Model):
	IdZ = models.AutoField(primary_key=True)
	IdU = models.ForeignKey('auth.User')
	IdHS = models.ForeignKey(Harmonogram_Startow,on_delete=models.CASCADE)
	Nazwa = models.CharField(max_length=30)
	Typ = models.CharField(max_length=30)

class Zawodnik(models.Model):
	IdZ = models.AutoField(primary_key=True)
	Imie = models.CharField(max_length = 30)
	Nazwisko = models.CharField(max_length = 30)
	IdZ_0 = models.ForeignKey(Zespol,on_delete=models.CASCADE)

class Zespol_Zawody(models.Model):
	IdZ_0 = models.ForeignKey(Zespol,on_delete=models.CASCADE)
	IdZawody = models.ForeignKey(Zawody, on_delete=models.CASCADE)