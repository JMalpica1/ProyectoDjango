from django import forms
from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Usuario
from django.contrib.auth.views import RegisterView

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = Usuario
        fields = ['rut', 'nombres', 'apellido', 'email', 'direccion','password','password2']


