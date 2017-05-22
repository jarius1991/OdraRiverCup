from django import forms
from django.contrib.auth.models import User
from django.forms import FileInput, RadioSelect, TextInput

from MainSite.models import *


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'username': TextInput(attrs={'class': 'dform'}),
            'email': TextInput(attrs={'class': 'dform'}),
            'password': TextInput(attrs={'class': 'dform'})

        }


class ArtykulForm(forms.ModelForm):
    def zapisz(self, form, request, timezone):
        artykul = form.save(commit = False)
        artykul.IdAdmin = request.user
        artykul.published_date = timezone.now()
        artykul.save()
        return artykul

    class Meta:
        model = Artykul
        fields = ('tytul', 'tresc')


class GaleriaForm(forms.ModelForm):
    def zapisz(self,form,request,timezone):
        zdjec = form.save(commit=False)
        zdjec.IdAdmin = request.user
        zdjec.published_date = timezone.now()
        zdjec.save()
        return zdjec;
    
    class Meta:
        model = Galeria
        fields = ('IdZawody', 'Zdjecie')
        CHOICES = Zawody
        widgets = {
            'tytul': forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect()),
            'zdjecie': FileInput()
        }


class UserDataForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('Email', 'Uczelnia', 'Telefon', 'Ulica', 'Numer',
                  'Mieszkanie', 'KodPocztowy', 'Miejscowosc')


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password')
#class EmailForm(forms.Form):
  #  email = forms.EmailField(label='email', max_length=120, size=21 )
   # text = forms.Textarea(label='text', )
