from django.urls import path

from . import views

app_name = 'automation'

urlpatterns = [
    path('', views.index, name='home'),
    path('water', views.water, name='water'),
    path('light', views.light, name='light'),
    path('status_water_flow',
         views.status_water_flow,
         name='status_water_flow'
         ),
    path('abort_water_flow',
         views.abort_water_flow,
         name='abort_water_flow'
         ),
]
