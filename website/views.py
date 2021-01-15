from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Booking_info, Appointment
from .forms import BookingForm, AppointmentForm
from django.core.mail import send_mail


def home(request):
    return render(request, 'home.html', {})


def about_office(request):
    return render(request, 'about_office.html', {})


def about_doctor(request):
    return render(request, 'about_doctor.html', {})


def booking_form(request):
    return render(request, 'booking_form.html', {})


def booking_appointment(request):
    # form = BookingForm(request.POST or None)
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            # obj = form.save(commit=False) # comment this row bcz we switch to model_saving instead of modelform_saving
            # obj.save()
            form.save()

            # get variable from current form's value
            message_fname = form.cleaned_data['fname']
            message_lname = form.cleaned_data['lname']
            message_appointment_date = form.cleaned_data['appointment_date']
            message_appointment_time = form.cleaned_data['appointment_time']
            message_email = form.cleaned_data['email']
            message_phone = form.cleaned_data['phone']
            message_clinic_prefer = form.cleaned_data['clinic_prefer']
            message_channel = form.cleaned_data['channel']
            message_body = form.cleaned_data['message_body']

            # Send email
            send_mail(
                # message_fname + ', <' + message_lname + '>',  # subject
                'Appointment request from ' + message_fname + ' ' + message_lname,  # subject
                'Client Full Name: ' + message_fname + ' ' + message_lname + '.\n'
                'Targeted datetime: ' + str(message_appointment_date) + ' ' + str(message_appointment_time) + '.\n'
                'Email: ' + message_email + ';' + ' Phone: ' + str(message_phone) + '.\n'
                'Clinic Prefer: ' + message_clinic_prefer + ';' + ' Find Us By Channel : ' + message_channel + '.\n'
                'Message_body: ' + message_body,    # message
                'Appointment Info from' + message_email,  # from email
                ['aoaocoolgg@gmail.com'],  # later @20201210 switch to target email  "lcqualitydental@gmail.com"
                fail_silently=False,
            )

            print('form save is proved')
            # print(message_fname)
        # return redirect('appoint_board')
        return render(request, 'booking_appointment.html', {'fname': form.cleaned_data['fname']})
    else:
        return render(request, 'booking_appointment.html', {})

    # if request.method == "POST":
    #     form = BookingForm(request.POST)
    #     if form.is_valid():
    #         obj = form.save(commit=False)  # comment this row bcz we switch to model_saving instead of modelform_saving
    #         obj.save()
            # now I decide to keep using ModelForm as corrected pattern
            # obj = BookingForm(request.POST)
            # # obj.fname = form.cleaned_data['fname']
            # # obj.lname = form.cleaned_data['lname']
            # # obj.appointment_datetime = form.appointment_datetime
            # # # finally save the object in db
            # # obj.save()
            #
            # obj.message_fname = form.cleaned_data['fname']
            # obj.message_lname = form.cleaned_data['lname']
            # obj.message_appointment_date = form.cleaned_data['appointment_date']
            # obj.message_appointment_time = form.cleaned_data['appointment_time']
            # obj.message_email = form.cleaned_data['email']
            # obj.message_phone = form.cleaned_data['phone']
            # obj.message_clinic_prefer = form.cleaned_data['clinic_prefer']
            # obj.message_channel = form.cleaned_data['channel']
            # obj.message_body = form.cleaned_data['message_body']
            # # finally save the object in db
            # obj.save()

            # print('form is valid--proved!')
            # print(form.cleaned_data['fname'])
            # print(form.cleaned_data['lname'])

            # Send email
            # send_mail(
            #     message_fname + ', <' + message_email + '>',  # subject
            #     message_body,  # message
            #     message_email,  # from email
            #     ['aoaocoolgg@gmail.com'],  # later @20201210 switch to target email  "lcqualitydental@gmail.com"
            #     fail_silently=False,
            # )
            # send_mail(
            #     # message_fname + ', <' + message_lname + '>',  # subject
            #     'Appointment request from ' + message_fname + ', ' + message_lname,  # subject
            #     'Targeted datetime: ' + str(message_appointment_date) + ' ' + str(message_appointment_time) + '.\n'
            #     'Email: ' + message_email + ';' + ' Phone: ' + str(message_phone) + '.\n'
            #     'Clinic Prefer: ' + message_clinic_prefer + ';' + ' Find Us By Channel : ' + message_channel + '.\n'
            #     'Message_body: ' + message_body,    # message
            #     message_email,  # from email
            #     ['liyanggm@gmail.com'],  # later @20201210 switch to target email  "lcqualitydental@gmail.com"
            #     fail_silently=False,
            # )
            # now I decide to keep using ModelForm as corrected pattern
            # obj = Appointment()
            # obj.fname = form.cleaned_data['fname']
            # obj.lname = form.cleaned_data['lname']
            # obj.appointment_datetime = form.appointment_datetime
            # # finally save the object in db
            # obj.save()
    #     return redirect('appoint_board')
    # #     return render(request, 'booking_appointment.html', {'fname': form.cleaned_data['fname']})
    # else:
    #     return render(request, 'booking_appointment.html', {})


def testing_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            # obj = form.save(commit=False) # comment this row bcz we switch to model_saving instead of modelform_saving
            # obj.save()
            form.save()

            # get variable from current form's value
            message_fname = form.cleaned_data['fname']
            message_lname = form.cleaned_data['lname']
            message_date = form.cleaned_data['appointment_date']
            message_time = form.cleaned_data['appointment_time']

            print('form save is proved')
            print(message_fname)

            # Send email
            send_mail(
                message_fname + ', <' + message_lname + '>' + str(message_date) + str(message_time),  # subject
                'this is a mesage',  # message
                'from eamil<xx@xx.com>',  # from email
                ['aoaocoolgg@gmail.com'],  # later @20201210 switch to target email  "lcqualitydental@gmail.com"
                fail_silently=False,
            )
        return redirect('appoint_board')
    #     return render(request, 'booking_appointment.html', {'fname': form.cleaned_data['fname']})
    else:
        return render(request, 'booking_appointment.html', {})


def appoint_board(request):
    all_members = Booking_info.objects.all().order_by('-id')
    all_testings = Appointment.objects.all().order_by('-id')
    return render(request, 'appoint_board.html', {'all': all_members, 'all_testings': None})


def contact(request):
    if request.method == "POST":
        pass
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # Send email
        send_mail(
            message_name + ', <' + message_email + '>',  # subject
            message,  # message
            message_email,  # from email
            ['aoaocoolgg@gmail.com'],  # later @20201210 switch to target email  "lcqualitydental@gmail.com"
            fail_silently=False,
        )

        return render(request, 'contact.html', {'message_name': message_name})

    else:
        # return the page
        return render(request, 'contact.html', {})
