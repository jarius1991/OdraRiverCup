# -*- coding: UTF-8 -*-
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import (get_object_or_404, redirect, render,
                              render_to_response)
from django.template import RequestContext
from django.utils import translation
from django.utils.translation import LANGUAGE_SESSION_KEY
from django.contrib import auth
from django.contrib.auth.forms import PasswordChangeForm


from .forms import *
from .models import *


def email_poprawny(request):
    context = RequestContext(request)
    if request.method == 'GET':
        email = request.GET['email']
        poprawny = validateEmail(email)
        return HttpResponse(poprawny)


def validateEmail(email):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False


def email_wyslij(request):
    if request.method == 'POST':
        email = request.POST.get("nav-input", "")
        text = request.POST.get("comment", "")

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
            # artykul = form.save(commit = False)
            # artykul.IdAdmin = request.user
            # artykul.published_date = timezone.now()
            # artykul.save()
            artykul = form.zapisz(form,request, timezone)
            return redirect('Artykul_detail', pk=artykul.pk)
        else:
            form = ArtykulForm()

    return render(request, "OdraRiverCup/Artykul_new.html", {'form': form})


@login_required
def Artykul_edit(request, pk):
    artykul = get_object_or_404(Artykul, pk=pk)
    if request.method == "POST":
        form = ArtykulForm(request.POST, instance=artykul)
        if form.is_valid():
            #artykul = form.save(commit = False)
            #artykul.IdAdmin = request.user
            #artykul.published_date = timezone.now()
            #artykul.save()
            artykul = form.zapisz(form,request,timezone)
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
    for wynik in wyniki:
        zespol = wynik.IdZespol
        zawody = wynik.IdZawody

        if zawody.Nazwa not in tabela_wynikow:
            tabela_wynikow[zawody.Nazwa] = dict()
        harmon = wynik.IdHs
        if harmon.Opis not in tabela_wynikow[zawody.Nazwa]:
            tabela_wynikow[zawody.Nazwa][harmon.Opis] = []
        dateandtime = datetime.strptime(str(harmon.Data)[:19],
                                        '%Y-%m-%d %H:%M:%S')
        data = dateandtime.date()
        godzina = dateandtime.time()
        tabela_wynikow[zawody.Nazwa][harmon.Opis].append([data, godzina,
                                                          zespol.Nazwa, wynik.Czas])
    return render(request, 'OdraRiverCup/Wyniki.html',
                  {'wyniki': tabela_wynikow})


def Remove_Wyniki(request):
    if request.method == "POST":
        id = request.POST.get('remove', '')
        wyniki = Zawody.objects.filter(Nazwa=id)[0]

        return redirect('Wyniki')

# @login_required
# def UserPanel(request):
#     pass


def Loggin(request):
    return render(request, 'OdraRiverCup/accounts/Logowanie.html', {})


def success(request):
    return render(request, 'OdraRiverCup/accounts/success.html', {})


def setPolski(request):

    artykuly = Artykul.objects.all()
    translation.activate("pl")
    request.session[LANGUAGE_SESSION_KEY] = 'pl'
    return render(request, 'OdraRiverCup/Aktualnosci.html',
                  {'artykuly': artykuly})


def setAngielski(request):
    artykuly = Artykul.objects.all()
    translation.activate("en")
    request.session[LANGUAGE_SESSION_KEY] = 'en'
    return render(request, 'OdraRiverCup/Aktualnosci.html',
                  {'artykuly': artykuly})


@login_required
def Galeria_new(request):
    form = GaleriaForm(request.POST or None, request.FILES)
    if form.is_valid():
        # TODO
        # Wydzielić funkcje
        zdjec = form.save(commit=False)
        zdjec.IdAdmin = request.user
        zdjec.published_date = timezone.now()
        zdjec.save()
        return redirect(GaleriaV)

    return render(request, "OdraRiverCup/Galeria_new.html",
                  {'form': form})


@login_required
def Galeria_remove(request):
    if request.method == "POST":
        id = request.POST.get('rem', '')
        lista = get_object_or_404(Galeria, pk=id)
        lista.delete()
        return redirect(GaleriaV)


@login_required
def Galeria_edit(request, pk):
    zdjecie = get_object_or_404(Galeria, pk=pk)
    if request.method == "POST":
        form = GaleriaForm(request.POST, request.FILES, instance=zdjecie)
        if form.is_valid():
            zdjecie = form.save(commit=False)
            zdjecie.IdAdmin = request.user
            zdjecie.published_date = timezone.now()
            zdjecie.save()
            return redirect(GaleriaV)
        else:
            form = GaleriaForm(instance=zdjecie)
        return render(request, 'OdraRiverCup/Galeria_new.html', {'form': form})


@login_required
def profile_edit(request):
    try:
        profile = request.user.profile
    except:
        profile = Profile(user=request.user)
    profile_message = address_message = password_message = ''
    profile_form = UserDataForm(data=request.POST or None, instance=profile)
    password_form = PasswordChangeForm(request.user, request.POST)
    if request.method == "POST":
        if 'Email' in request.POST and profile_form.is_valid():
            profile_form.save()
            profile_message = "Dane zapisane"
        if 'old_password' in request.POST and password_form.is_valid():
            password_form.save()
            password_message = "Haslo zmienione"
    return render(request, 'OdraRiverCup/accounts/profile_edit.html',
                  {'password_form': password_form,
                   'profile_form': profile_form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success')
    else:
        form = UserCreationForm()
    return render(request, 'OdraRiverCup/accounts/Register.html', {'form': form})


def registration_complete(request):
    return render(request, 'OdraRiverCup/accounts/success.html')


def login(request):
    return render(request, 'OdraRiverCup/accounts/Login.html')


def process_login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/login_error')


def loggedin(request):
    return render(request, 'OdraRiverCup/accounts/loggedin.html',
                  {'username': request.user.username})


def login_error(request):
    return render(request, 'OdraRiverCup/accounts/login_error.html')


def logout(request):
    auth.logout(request)
    return render(request, 'OdraRiverCup/accounts/logged_out.html')
