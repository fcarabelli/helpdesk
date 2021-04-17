from django import forms
from re import search


class LoginForm(forms.Form):
    user_email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'id': 'user_email', 'placeholder': 'Correo institucional'}),
        label='Correo institucional')
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password', 'placeholder': 'Contraseña'}),
        label='Contraseña')
