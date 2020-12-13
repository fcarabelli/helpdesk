from django.urls import path

from helpdeskapp import views

urlpatterns = [
    path('addQuestion', views.addQuestion, name='addQuestion'),
]