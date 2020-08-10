from django.urls import path
from . import views

app_name = 'usman'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:zone_name>', views.control, name='control')
]