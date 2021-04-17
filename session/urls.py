from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.IndexView.destroy_session, name="logout"),
    path('', views.IndexView.as_view(), name='Start'),
]