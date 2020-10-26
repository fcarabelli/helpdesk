from django import forms
from re import search


class LoginForm(forms.Form):
    user_email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'id': 'user_email', 'placeholder': 'Correo institucional'}),
        label='Correo institucional')
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password', 'placeholder': 'Contraseña'}),
        label='Contraseña')

    def clean_user_email(self):
        email = self.cleaned_data['user_email']
        if search("@frm.utn.edu.ar", email):
            return email
        elif search("@docentes.frm.utn.edu.ar", email):
            return email
        elif search('@alumnos.frm.utn.edu.ar', email):
            return email
        else:
            raise forms.ValidationError("Tiene que ser correo institucional")
            return email
