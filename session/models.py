from django.db import models
from django.contrib.auth.models import (
    AbstractUser
)


class User(AbstractUser):
    email = models.EmailField(verbose_name='Correo institucional', unique=True)
    cellphone = models.CharField(max_length=15, verbose_name='Celular')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def create_user(self, email, first_name, last_name, password):
        """
        Create institutional user
        """
        if not email:
            raise ValueError("User must have email")
        if not first_name:
            raise ValueError("You must add your first name")
        if not last_name:
            raise ValueError("You must add your last name")
        if not password:
            raise ValueError("You need a password")
        user = self.create_user(email, first_name, last_name)
        user.set_password(password)
        user.save(self._db)

    def __str__(self):
        return self.email
