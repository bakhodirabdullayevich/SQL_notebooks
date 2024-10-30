from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('organizations/', get_organizations, name='organizations'),
    path('objects/', get_objects, name='objects'),
    path('object/add', add_object, name='add_object'),
    path('object/edit/<int:pk>/', edit_object, name='edit_object'),
    path('object/delete/<int:pk>/', delete_object, name='delete_object'),
    path('object/<int:pk>/details/', object_details, name='object_details'),
    path('object/<int:pk>/add-meter/', add_meter, name='add_meter'),
    path('meters/', get_meters, name='meters'),
    path('object/<int:pk>/meter/details/', meter_details, name='meter_details'),
    path('object/meter/edit/<int:pk>/', edit_meter, name='edit_meter'),
    path('object/meter/delete/<int:pk>/', delete_meter, name='delete_meter'),
    path('object/meter/<int:pk>/add-flowmeter-sertificate/', add_flowmeter_sertificate, name='add_flowmeter_sertificate'),
    path('object/meter/<int:pk>/edit-flowmeter-sertificate/', edit_flowmeter_sertificate, name='edit_flowmeter_sertificate'),
    path('object/meter/<int:pk>/delete-flowmeter-sertificate/', delete_flowmeter_sertificate, name='delete_flowmeter_sertificate'),

    path('sertificates/', get_all_sertificates, name='all_sertificates'),
    path('sertificates/active/', get_active_sertificates, name='active_sertificates'),
    path('sertificates/not-active/', get_not_active_sertificates, name='not_active_sertificates'),
]