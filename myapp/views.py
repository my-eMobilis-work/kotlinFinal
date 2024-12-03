import json
import requests
from decouple import config
from django.http import HttpResponse
from requests.auth import HTTPBasicAuth
from django.shortcuts import render, redirect

from myapp.credentials import MpesaAccessToken, LipanaMpesaPassword
from myapp.forms import AppointmentForm, ImageUploadForm
from myapp.models import Appointment, Contact, Member, ImageModel


# Create your views here.

def index(request):
    if request.method == 'POST':
        if Member.objects.filter(
            username=request.POST['username'],
            password=request.POST['password'],
        ).exists():
            return render(request, 'index.html')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def services(request):
    return render(request, 'service-details.html')

def starter(request):
    return render(request, 'starter-page.html')

def about(request):
    return render(request, 'about.html')

def doctors(request):
    return render(request, 'doctors.html')

def my_service(request):
    return render(request, 'services.html')

def appointment(request):
    if request.method == 'POST':
        my_appointment = Appointment(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            dateTime=request.POST['dateTime'],
            department=request.POST['department'],
            doctor=request.POST['doctor'],
            message=request.POST['message'],
        )
        my_appointment.save()
        return redirect('/show_appointments')
    else:
        return render(request, 'appointment.html')

def show_appointments(request):
    all_appointments = Appointment.objects.all()
    return render(request, 'showAppointments.html', {'appointments': all_appointments})

def edit_appointment(request, id):
    edit_appointment = Appointment.objects.get(id = id)
    return render(request, 'editAppointment.html', {'appointment': edit_appointment})

def update_appointment(request, id):
    update_info = Appointment.objects.get(id = id)
    form = AppointmentForm(request.POST, instance=update_info)
    if form.is_valid():
        form.save()
        return redirect('/show_appointments')
    else:
        return render(request, 'editAppointment.html')

def delete_appointment(request, id):
    appoint = Appointment.objects.get(id = id)
    appoint.delete()
    return redirect('/show_appointments')

def contact(request):
    if request.method == 'POST':
        new_contact = Contact(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],
        )
        new_contact.save()
        return redirect('/contact')
    else:
        return render(request, 'contact.html')

def show_contacts(request):
    all_contacts = Contact.objects.all()
    return render(request, 'showContacts.html', {'contacts': all_contacts})

def delete_contact(request, id):
    appoint = Contact.objects.get(id = id)
    appoint.delete()
    return redirect('/show_contacts')

def register(request):
    if request.method == 'POST':
        new_member = Member(
            name=request.POST['name'],
            username=request.POST['username'],
            password=request.POST['password'],
        )
        new_member.save()
        return redirect('/login')
    else:
        return render(request, 'register.html')
def login(request):
    return render(request, 'login.html')

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/show_images')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def show_images(request):
    images = ImageModel.objects.all()
    return render(request, 'show_images.html', {'images': images})

def image_delete(request, id):
    image = ImageModel.objects.get(id=id)
    image.delete()
    return redirect('/show_images')



def token(request):
    consumer_key = config('CONSUMER_KEY')
    consumer_secret = config('CONSUMER_SECRET')
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def pay(request):
   return render(request, 'pay.html')



def stk(request):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPassword.Business_short_code,
            "Password": LipanaMpesaPassword.decode_password,
            "Timestamp": LipanaMpesaPassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "eMobilis",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("Success")