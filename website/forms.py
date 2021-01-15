from django import forms
from .models import Booking_info, Appointment


# back to this valid mode, that is to say we should insist to use forms.Modelform
class BookingForm(forms.ModelForm):
    # appointment_datetime = forms.DateTimeField(input_formats=["%d %b %Y %H:%M:%S %Z"])
    # appointment_datetime = forms.DateTimeField(input_formats=['%m/%d/%Y %H:%M'])
    # phone = forms.CharField(max_length=20, min_length=12)

    class Meta:
        model = Booking_info
        fields = '__all__'
        # fields = ['fname', 'lname', 'email', 'phone', 'appointment_date', 'appointment_time', 'clinic_prefer',
        #           'channel', 'message_body', 'is_signed']


class AppointmentForm(forms.ModelForm):  # temporarily added by Ly for testing.
    class Meta:
        model = Appointment
        fields = '__all__'
        # fields = ['fname', 'lname', 'appointment_datetime']


# class AppointmentForm(forms.Form):
#     fname = forms.CharField(max_length=50)
#     lname = forms.CharField(max_length=100)
#     appointment_datetime = forms.DateTimeField(input_formats=["%d %b %Y %H:%M:%S %Z"])


# obsolted by LY because I need to add a date format on "form.datefield"
# class AppointmentForm(forms.ModelForm):
#     class Meta:
#         model = Appointment
#         fields = ['fname', 'lname', 'appointment_datetime']

# class MemberForm(forms.ModelForm):
#     class Meta:
#         model = Member
#         fields = ['fname', 'lname', 'email', 'passwd', 'age']
#
# class DateForm(forms.Form):
#     date = forms.DateTimeField(
#         input_formats=['%d/%m/%Y %H:%M'],
#         widget=forms.DateTimeInput(attrs={
#             'class': 'form-control datetimepicker-input',
#             'data-target': '#datetimepicker1'
#         })
#     )
#
