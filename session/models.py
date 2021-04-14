from django.db import models
from django.contrib.auth.models import (
    AbstractUser
)
from .manager import CustomUserManager


class User(AbstractUser):
    cellphone = models.CharField(max_length=15, verbose_name='Celular')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = CustomUserManager()

    def __str__(self):
        return self.email
