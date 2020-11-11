from django.urls import path

from . import views

urlpatterns = [
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.destroy_session, name="logout"),
    path('create', views.create_session, name="create"),
    path('', views.IndexView.as_view(), name='Start'),
]