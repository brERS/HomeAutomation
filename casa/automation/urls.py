from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home-automation'),
    path('home', views.index, name='home-automation'),
    path('water', views.water, name='water-automation'),
    path('status_water_flow', views.status_water_flow,
         name='water_flow-automation'),
    path('abort_water_flow', views.abort_water_flow,
         name='water_flow-automation'),
]
