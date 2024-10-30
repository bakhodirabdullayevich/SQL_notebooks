from django.urls import path
from .views import *

urlpatterns = [

    path('', get_restored_volume, name='get_restored_volume'),
    path('meters-restored-volumes/', get_meters_with_restored_volumes, name='meters_with_restored_volumes'),
    path('add-restored_volume/', add_restored_volume, name='add_restored_volume'),
    path('restored_volumes/', get_restored_volume, name='restored_volumes'),
    path('calendar/', calendar, name='calendar'),

]