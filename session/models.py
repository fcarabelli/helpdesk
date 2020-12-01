from django.db import models
from django.contrib.auth.models import (
    AbstractUser
)


class User(AbstractUser):
    email = models.EmailField(verbose_name='Correo institucional', unique=True)
    cellphone = models.CharField(max_length=15, verbose_name='Celular')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']


