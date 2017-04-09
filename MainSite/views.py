from django.shortcuts import render
from django.utils import translation
from django.utils.translation import LANGUAGE_SESSION_KEY
from .models import *
def Aktualnosci(request):
	artykuly = Artykul.objects.all()
	return render(request, 'OdraRiverCup/Aktualnosci.html', {'artykuly':artykuly})

def Harmonogram(request):

	return render(request, 'OdraRiverCup/Harmonogram.html', {})

def Partnerzy(request):
	return render(request, 'OdraRiverCup/Partnerzy.html', {})

def Kontakt(request):
	return render(request, 'OdraRiverCup/Kontakt.html', {})

def Galeria(request):
	galeria = Galeria.objects.all()
	return render(request, 'OdraRiverCup/Galeria.html', {'galeria':galeria})

def Wyniki(request):
	wyniki = Wyniki_Zawodow.objects.all()
	return render(request, 'OdraRiverCup/Wyniki.html', {'wyniki':wyniki})

def Loggin(request):
	return render(request, 'OdraRiverCup/Logowanie.html', {})

def setPolski(request):
	request.session[LANGUAGE_SESSION_KEY] = 'pl'
	language = 'pl'
	return render(request,'OdraRiverCup/Aktualnosci.html',{'language':language})

def setAngielski(request):
	request.session[LANGUAGE_SESSION_KEY] = 'en'
	language = 'en'
	return render(request,'OdraRiverCup/Aktualnosci.html',{'language':language})
