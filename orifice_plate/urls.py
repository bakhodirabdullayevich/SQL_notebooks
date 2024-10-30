from django.urls import path
from .views import *

urlpatterns = [

    path('meters/<int:pk>/add_orifice_plate/', add_orifice_plate, name='add_orifice_plate'),
    path('', get_orifice_plates, name='get_orifice_plates'),

]