
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.view_main_bmi, name='bmi_main_view'),
    url(r'^count_bmi/$', views.view_count_bmi, name='count_bmi'),
    url(r'^result/$', views.view_bmi_result, name='bmi_result'),
]
