from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('temperature/<str:zone_name>', views.temperature, name='temperature'),
    path('lighting/<str:zone_name>', views.lighting, name='lighting')
]