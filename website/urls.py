from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about_doctor/', views.about_doctor, name='about_doctor'),
    path('about_office/', views.about_office, name='about_office'),
    # path('booking_form/', views.booking_form, name='booking_form'),
    path('booking_appointment/', views.booking_appointment, name='booking_appointment'),
    # path('testing_appointment/', views.testing_appointment, name='testing_appointment'),
    path('appoint_board/', views.appoint_board, name='appoint_board'),
    path('contact/', views.contact, name='contact'),
    # path('contact.html', views.contact, name='contact'),
]
