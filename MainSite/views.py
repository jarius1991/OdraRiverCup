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
	return render(request, 'OdraRiverCup/Partnerzy.html', {'galeria':galeria})

def Kontakt(request):

	return render(request, 'OdraRiverCup/Kontakt.html', {})

def GaleriaV(request):
	galeria = Galeria.objects.all()
	return render(request, 'OdraRiverCup/Galeria.html', {"galeria":galeria})

def Wyniki(request):
	wyniki = Wyniki_Zawodow.objects.all()
	return render(request, 'OdraRiverCup/Wyniki.html', {'wyniki':wyniki})

def Loggin(request):
	return render(request, 'OdraRiverCup/Logowanie.html', {})
	
def success(request):
	return render(request, 'OdraRiverCup/success.html', {})

def setPolski(request):
	translation.activate("pl")
	request.session[LANGUAGE_SESSION_KEY] = 'pl'

	return render(request,'OdraRiverCup/Aktualnosci.html')

def setAngielski(request):
	translation.activate("en")
	request.session[LANGUAGE_SESSION_KEY] = 'en'

	return render(request,'OdraRiverCup/Aktualnosci.html')
