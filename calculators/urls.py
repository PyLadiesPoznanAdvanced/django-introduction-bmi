
from django.conf.urls import url
from . import views

urlpatterns = [

    # adres strony z możliwością wyboru kalkulatorów
    url(r'^$', views.calculators, name="calculators"),

    # adres url przekierowujący między kalkulatorami
    url(r'^calc_choose$', views.calc_choose, name="calc_choose"),

    # adres url kalkulatora kalorii
    url(r'^calories_calculator', views.view_main_calories, name="calories"),


    # adres url przekierowujący do głównego widoku kalkulatora bmi
    url(r'^bmi_calculator/$', views.view_main_bmi, name='main_bmi'),

    # adres url przekierowujący do widoku obliczającego indeks bmi
    url(r'^count_bmi/$', views.view_count_bmi, name='count_bmi'),

    # adres url przekierowujący do widoku z wynikami bmi
    url(r'^bmi_result/$', views.view_bmi_result, name='bmi_result'),


]
