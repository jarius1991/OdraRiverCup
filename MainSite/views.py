from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from django.utils import translation
from django.shortcuts import render, get_object_or_404
from django.utils.translation import LANGUAGE_SESSION_KEY
from .models import *
from .forms import ArtykulForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime


def email_poprawny(request):
	context = RequestContext(request)
	if request.method == 'GET':
		email= request.GET['email']
	poprawny=validateEmail(email)
	return HttpResponse(poprawny)

def validateEmail( email ):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email( email )
        return True
    except ValidationError:
        return False

def email_wyslij(request):
	if request.method == 'POST':
		email =  request.POST.get("nav-input","")
		text = request.POST.get("comment","")

	print(email, text)
	wiadomosc = Wiadomosci()
	wiadomosc.email = email
	wiadomosc.tresc = text
	wiadomosc.save()

	return redirect('Kontakt')


def Aktualnosci(request):
	artykuly = Artykul.objects.all()
	return render(request, 'OdraRiverCup/Aktualnosci.html', {'artykuly':artykuly})


@login_required
def Artykul_new(request):
    if request.method == "POST":
        form = ArtykulForm(request.POST)
        if form.is_valid():
            artykul = form.save(commit = False)
            artykul.IdAdmin = request.user
            artykul.published_date = timezone.now()
            artykul.save()
            return redirect('Artykul_detail', pk=artykul.pk)
    else:
        form = ArtykulForm()

    return render(request, "OdraRiverCup/Artykul_new.html", {'form':form})

@login_required
def Artykul_edit(request, pk):
    artykul = get_object_or_404(Artykul, pk=pk)
    if request.method == "POST":
        form = ArtykulForm(request.POST, instance=artykul)
        if form.is_valid():
            artykul = form.save(commit=False)
            artykul.IdAdmin = request.user
            artykul.published_date = timezone.now()
            artykul.save()
            return redirect('Artykul_detail', pk=artykul.pk)
    else:
        form = ArtykulForm(instance=artykul)

    return render(request, 'OdraRiverCup/Artykul_new.html', {'form': form})


def Artykul_detail(request, pk):
    artykul = get_object_or_404(Artykul, pk=pk)
    return render(request, "OdraRiverCup/Artykul_detail.html", {'artykul':artykul})

def Harmonogram(request):
    return render(request, 'OdraRiverCup/Harmonogram.html', {})

def Partnerzy(request):
    return render(request, 'OdraRiverCup/Partnerzy.html', {})

def Kontakt(request):
    return render(request, 'OdraRiverCup/Kontakt.html', {})

def GaleriaV(request):
    galeria = Galeria.objects.all()
    return render(request, 'OdraRiverCup/Galeria.html', {"galeria":galeria})

def Wyniki(request):
    wyniki = Wyniki_Zawodow.objects.all()
    tabela_wynikow = dict()
    # Sekcja zakomentowana; problem leży w dobraniu się do Zawodów, w
    # obecnym model. W wersji roboczej dodałem pole IdZawody w tabeli, co
    # poprawię Wkrótce.
    #
    # for wynik in wyniki:
    #     zespol = wynik.IdZespol
    #     zawody = wynik.IdZawody

    #     if zawody not in tabela_wynikow:
    #         tabela_wynikow[zawody.Nazwa] = []
    #     harmon = wynik.IdHs
    #     dateandtime = datetime.strptime(str(harmon.Data)[:19],
    #                                     '%Y-%m-%d %H:%M:%S')
    #     data = dateandtime.date()
    #     godzina = dateandtime.time()
    #     tabela_wynikow[zawody.Nazwa].append([data, godzina,
    #                                          zespol.Nazwa, wynik.Czas])
    tabela_wynikow['Rysy22'] = [['22-10-2016', '10:00', 'Drużyna PWr', '10:12:500']]
    return render(request, 'OdraRiverCup/Wyniki.html', {'wyniki':tabela_wynikow})

# @login_required
# def UserPanel(request):
#     pass

def Loggin(request):
    return render(request, 'OdraRiverCup/Logowanie.html', {})

def success(request):
    return render(request, 'OdraRiverCup/success.html', {})

def setPolski(request):

    artykuly = Artykul.objects.all()
    translation.activate("pl")
    request.session[LANGUAGE_SESSION_KEY] = 'pl'

    return render(request,'OdraRiverCup/Aktualnosci.html', {'artykuly':artykuly})

def setAngielski(request):

	artykuly = Artykul.objects.all()
	translation.activate("en")
	request.session[LANGUAGE_SESSION_KEY] = 'en'


    return render(request,'OdraRiverCup/Aktualnosci.html', {'artykuly':artykuly})
