#from .models import UserProfile
from django.contrib.auth.models import User
from django import forms
from django.forms import TextInput,FileInput,RadioSelect
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

#class UserProfileForm(forms.ModelForm):
  #  class Meta:
      #  model = UserProfile
      #  fields = ('website',)


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

    class Meta:
        model = Galeria
        fields = ('IdZawody', 'Zdjecie')
        CHOICES = Zawody
        widgets = {
            'tytul': forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect()),
            'zdjecie': FileInput()
        }
        
#class EmailForm(forms.Form):
  #  email = forms.EmailField(label='email', max_length=120, size=21 )
   # text = forms.Textarea(label='text', )

