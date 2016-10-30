
from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views)  # element zadania 3

    # adres url przekierowujący do głównego widoku kalkulatora bmi
    url(r'^bmi_calculator/$', views.view_main_bmi, name='main_bmi'),

    # adres url przekierowujący do widoku obliczającego indeks bmi
    url(r'^count_bmi/$', views.view_count_bmi, name='count_bmi'),

    # adres url przekierowujący do widoku z wynikami bmi
    url(r'^bmi_result/$', views.view_bmi_result, name='bmi_result'),
]
