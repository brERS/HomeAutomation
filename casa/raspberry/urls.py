from django.urls import path

from . import views

app_name = 'raspberry'

urlpatterns = [
    path('hardware_info', views.hardware_info, name='home'),
    path('get_info_cpu', views.get_info_cpu, name='get_info_cpu'),
    path('get_info_memory', views.get_info_memory, name='get_info_memory'),
    path('get_info_disk', views.get_info_disk, name='get_info_disk'),
]
