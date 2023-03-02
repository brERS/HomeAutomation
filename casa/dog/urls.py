from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('dog/', views.dog, name='dog'),
    path('dog/agua', views.agua, name='agua'),
]
