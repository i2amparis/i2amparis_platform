from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'feedback_form'
urlpatterns = [
    url(r'^$', views.feedback_form, name='home'),
    # url('feedback', views.feedback_form, name='home'),
    # path('feedback', views.feedback_form, name='feedback')
]