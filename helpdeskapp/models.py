from django.db import models

from django.core.validators import RegexValidator


# Create your models here.
class Question(models.Model):
    subject = models.CharField(max_length=72,blank=False)
    message = models.CharField(max_length=1000,blank=False)
    question_datetime = models.DateTimeField(auto_now=True)
    email = models.EmailField(max_length=254,blank=False,help_text="Ingresá tu mail de uso frecuente")
    phone_regex = RegexValidator(regex=r'^\d{9,15}$', message="Se permiten entre 9 y 15 números")
    phone_number = models.CharField(blank=True, validators=[phone_regex], max_length=15) # validators should be a list


