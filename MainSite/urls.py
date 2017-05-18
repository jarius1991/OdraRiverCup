from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.Aktualnosci, name='Odra'),
    url(r'^pl/$', views.setPolski, name='pol'),
    url(r'^/(?P<pk>[0-9]+)/$', views.Artykul_detail, name="Artykul_detail"),
    url(r'^/(?P<pk>[0-9]+)/edit$', views.Artykul_edit, name="Artykul_edit"),
    url(r'^Artykul/new/$', views.Artykul_new, name='Artykul_new'),
    url(r'^Galeria/new/$', views.Galeria_new, name='Galeria_new'),
    url(r'^Galeria/remove/$', views.Galeria_remove, name='Galeria_remove'),
    url(r'^Galeria/(?P<pk>[0-9]+)/edit/$', views.Galeria_edit, name='Galeria_edit'),
    url(r'^Harmonogram/$', views.Harmonogram, name='Harmonogram'),
    url(r'^Partnerzy/$', views.Partnerzy, name='Partnerzy'),
    url(r'^Kontakt/$', views.Kontakt, name='Kontakt'),
    url(r'^Galeria/$', views.GaleriaV, name='Galeryja'),
    url(r'^Wyniki/$', views.Wyniki, name='Wyniki'),
    url(r'^Wyniki/remove/$', views.Remove_Wyniki, name='Remove_Wyniki'),
    url(r'^Loggin/$', views.Loggin, name='Loggin'),
    url(r'^success/$', views.success, name='succ'),
    url(r'^en/$', views.setAngielski, name='Odra'),
    url(r'^email_poprawny/$', views.email_poprawny, name='email_poprawny'),
    url(r'^email_wyslij/$', views.email_wyslij, name='email_wyslij'),
    url(r'^accounts/edit/$', views.profile_edit, name='edytuj_profil'),
    url(r'^accounts/register/$', views.register, name='register'),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/process_login/$', views.process_login, name='process_login'),
    url(r'^accounts/loggedin/$', views.loggedin, name='loggedin'),
    url(r'^accounts/login_error/$', views.login_error, name='login_error'),
    url(r'^accounts/logout/$', views.logout, name='logout')

]
