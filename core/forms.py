from django import forms
from core import models
from .models import Clients


class ClientForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ['client_name', 'email', 'phone', 'course', 'customer']

class ClientUpdateForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = '__all__'
        model = models.Clients
        fields = ['logo', 'date', 'client_name', 'email','phone', 'course', 'customer', 'reg', 'email', 'phone', 'admin_sign']
