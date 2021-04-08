from django.shortcuts import redirect
from django.views import generic
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .CustomSessionLogin.Session import destroy_session as DestroySession, user_authenticated as UserAuthenticated


class LoginView(generic.FormView):
    template_name = 'session/login/navbar_user.html'
    form_class = LoginForm
    success_url = 'login'

    def form_valid(self, form):
        email = form.cleaned_data.get('user_email')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            messages.error(self.request, 'Revisar correo institucional y/o contraseña.')
            return super(LoginView, self).form_valid(form)


class IndexView(generic.TemplateView):
    template_name = 'session/base.html'


def destroy_session(request):
    """
    Cerrar sesión.
    """
    DestroySession(request.session['current_user_session'])
    del request.session['current_user_session']
    del request.session['current_user']
    return redirect('login')


def create_session(request):
    return redirect('/admin/')
