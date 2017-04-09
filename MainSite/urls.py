from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.Aktualnosci, name='Odra'),
    url(r'^pl/$', views.setPolski, name='pol'),
    url(r'^Harmonogram/$', views.Harmonogram, name='Harmonogram'),
    url(r'^Partnerzy/$', views.Partnerzy, name='Partnerzy'),
    url(r'^Kontakt/$', views.Kontakt, name='Kontakt'),
    url(r'^Galeria/$', views.Galeria, name='Galeria'),
    url(r'^Wyniki/$', views.Wyniki, name='Wyniki'),
    url(r'^Loggin/$', views.Loggin, name='Loggin'),
    url(r'^en/$', views.setAngielski, name='Odra'),
]