"""
django-introduction-bmi URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.shortcuts import HttpResponseRedirect


def view_main_bmi(request):
    """ Funkcja przekierowująca do głównego adresu url aplikacji bmi."""
    return HttpResponseRedirect("calculators/")

urlpatterns = [

    # uruchamianie widoku przy starcie projektu
    url(r'^$', view_main_bmi),

    # panel admina
    url(r'^admin/', admin.site.urls),

    # przypisanie adresów url z aplikacji calculators
    url(r'^calculators/', include('calculators.urls', namespace='calculators')),
]
