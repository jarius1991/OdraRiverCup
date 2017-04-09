from django.shortcuts import render
from django.utils.translation import LANGUAGE_SESSION_KEY

def Aktualnosci(request):
	language = 'pl'
	return render(request, 'OdraRiverCup/Aktualnosci.html', {'language':language})

def Harmonogram(request):
	language = 'pl'
	print(language)
	return render(request, 'OdraRiverCup/Harmonogram.html', {'language':language})

def Partnerzy(request):
	language = 'pl'
	return render(request, 'OdraRiverCup/Partnerzy.html', {'language':language})

def Kontakt(request):
	language = 'pl'
	return render(request, 'OdraRiverCup/Kontakt.html', {'language':language})

def Galeria(request):
	language = 'pl'
	return render(request, 'OdraRiverCup/Galeria.html', {'language':language})

def Wyniki(request):
	language = 'pl'
	return render(request, 'OdraRiverCup/Wyniki.html', {'language':language})

def Loggin(request):
	language = 'pl'
	return render(request, 'OdraRiverCup/Logowanie.html', {'language':language})

def setPolski(request):
	request.session[LANGUAGE_SESSION_KEY] = 'pl'
	language = 'pl'
	return render(request,'OdraRiverCup/Aktualnosci.html',{'language':language})

def setAngielski(request):
	request.session[LANGUAGE_SESSION_KEY] = 'en'
	language = 'en'
	return render(request,'OdraRiverCup/Aktualnosci.html',{'language':language})
