"""
django-introduction-bmi URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.shortcuts import HttpResponseRedirect


def view_main_bmi(request):
    """ Funkcja przekierowująca do głównego url aplikacji bmi."""
    return HttpResponseRedirect("/bmi_calculator/")

urlpatterns = [
    url(r'^admin/', admin.site.urls),          # panel admina
    url(r'^$', view_main_bmi),                 # uruchamianie widoku przy starcie projektu
    url(r'^bmi_calculator/', include('bmi_calculator.urls', namespace='bmi_calculator')),
]
