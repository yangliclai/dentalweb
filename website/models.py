from django.db import models
from django import forms
# from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator


class Booking_info(models.Model):
    CHENNEL_CHOICES = (
        ('--Channel You Find Us--', '--Channel You Find Us--'),
        ('referred_by_friends', 'referred_by_friends'),
        ('Insurance_network', 'Insurance_network'),
        ('Newspaper', 'Newspaper'),
        ('Internet', 'Internet'),
        ('Wechat', 'Wechat'),
        ('Treated_by_Dr_Chen_before', 'Treated_by_Dr_Chen_before'),
        ('Others', 'Others'),
    )
    CLINIC_PREFERRED = (
        ('--The Clinic You Prefer--', '--The Clinic You Prefer--'),
        ('Princeton', '4499 Rt 27,Princeton'),
        ('North_Brunswick', '2000 Rt 27,Suite B,North Brunswick'),
    )
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=100)
    email = models.EmailField()
    # appointment_datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    # phone = PhoneNumberField(default='12223334444')
    phone = models.CharField(max_length=20, validators=[RegexValidator(r'^\d{3}-\d{3}-\d{4}$')])
    clinic_prefer = models.CharField(max_length=30,
                              choices=CLINIC_PREFERRED,
                              default='--The Clinic You Prefer--')
    channel = models.CharField(max_length=30,
                              choices=CHENNEL_CHOICES,
                              default='--Channel You find Us--')
    message_body = models.TextField()
    is_signed = models.BooleanField(default=False)

    def __str__(self):
        return self.fname + ' ' + self.lname


class Appointment(models.Model):
    # STATUS_CHOICES = (
    #     ('TV', 'TV'),
    #     ('Print', 'Print'),
    #     ('Internet', 'Internet'),
    #     ('Others', 'Others'),
    # )
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=100)
    # email = models.EmailField()
    # appointment_datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    # phone = PhoneNumberField()
    # status = models.CharField(max_length=10,
    #                           choices=STATUS_CHOICES,
    #                           default='draft')

    def __str__(self):
        return self.fname + ' ' + self.lname
