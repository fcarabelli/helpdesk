from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

'''The user model does not have a password.
   The authentication occurs with the connection 
   to the database of the external system
'''

class User(models.Model):
    username = models.CharField(max_length=80)
    first_name = models.CharField(max_length=50, default='Firstname')
    last_name = models.CharField(max_length=50, default='Lastname')
    phone_regex = RegexValidator(regex=r'^\d{9,15}$', message="Se permiten entre 9 y 15 números")
    phone_number = models.CharField(blank=True, validators=[phone_regex], max_length=15)


    def __str__(self):
        return self.username
