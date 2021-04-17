from django.shortcuts import redirect
from django.views import generic
from .forms import LoginForm, UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User


class LoginView(generic.FormView):
    template_name = 'session/login_form.html'
    form_class = LoginForm
    success_url = 'login'

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            return redirect('helpdeskapp-index')
        else:
            email = form.cleaned_data.get('user_email')
            password = form.cleaned_data.get('password')
            user = authenticate(self.request, username=email, password=password)
            if user is not None:
                login(self.request, user)
                self.request.session.set_expiry(300)
                return redirect('helpdeskapp-index')
            else:
                messages.error(self.request, 'Revisar correo institucional y/o contraseña.')
                return super(LoginView, self).form_valid(form)


class IndexView(generic.TemplateView):
    template_name = 'session/base.html'

    def destroy_session(request):
        """
        Cerrar sesión.
        """
        logout(request)
        return redirect('login')

