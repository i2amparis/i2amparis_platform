from django.urls import path, include

from . import views

urlpatterns = [

    path('harmonisation_manual', views.harmonisation_manual, name='harmonisation_manual'),
    path('request_harmonisation_data', views.request_harmonisation_data, name='request_harmonisation_data'),

]