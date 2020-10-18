from django import forms
from re import search

from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    user_email = forms.EmailField(label='Correo institucional')
    password = forms.CharField(widget=forms.PasswordInput(), label='Contraseña')

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = cleaned_data.get('user_email')
        if search("@frm.utn.edu.ar", email):
            return None
        elif search("@docentes.frm.utn.edu.ar", email):
            return None
        elif search('@alumnos.frm.utn.edu.ar',email):
            return None
        else:
            raise ValidationError("Tiene que ser correo institucional")
