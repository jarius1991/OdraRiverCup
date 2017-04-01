from Comment.models import UserProfile
from django.contrib.auth.models import User
from django import forms
from django.forms import TextInput

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

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website',)
