from django.urls import path

from helpdeskapp import views

urlpatterns = [
    path('', views.index, name='helpdeskapp-index'),
    path('addQuestion', views.addQuestion, name='addQuestion'),
]