from django.shortcuts import render, redirect
from myapp.forms import AppointmentForm
from myapp.models import Appointment, Contact, Member

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
    updateInfo = Appointment.objects.get(id = id)
    form = AppointmentForm(request.POST, instance=updateInfo)
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

