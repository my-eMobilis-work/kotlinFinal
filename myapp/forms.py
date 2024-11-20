from django import forms
from myapp.models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'phone', 'dateTime', 'department', 'doctor', 'message']