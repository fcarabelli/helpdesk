from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import generic
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

class LoginView(generic.FormView):
    template_name = 'session/login/login.html'
    form_class = LoginForm
    success_url = 'login'

    def form_valid(self, form):
        email = form.cleaned_data.get('user_email')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        else:
            messages.success(self.request, 'Revisar correo institucional y/o contraseña.')
        return super(LoginView, self).form_valid(form)


def destroy_session(request):
    """
    Cerrar sesión.
    """
    logout(request)
    return redirect('login')


def create_session(request):
        return redirect('/admin/')
