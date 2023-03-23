from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Requerido. Ingrese una dirección de correo válida.')
    full_name = forms.CharField(max_length=100, help_text='Requerido. Ingrese su nombre completo.')
    region = forms.CharField(max_length=50, help_text='Requerido. Ingrese su región de residencia.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'full_name', 'region',)
