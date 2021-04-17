from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import Group
from re import search


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, first_name, last_name, **extra_fields):
        user = self.model(username=email, email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(raw_password=password)
        if search("@alumnos.frm.utn.edu.ar", email):
            group = Group.objects.get(name="Alumno")
        if search("@docentes.frm.utn.edu.ar", email):
            group = Group.objects.get(name="Docente")
        if search("@frm.utn.edu.ar", email):
            group = Group.objects.get(name="No docente")
        user.save()
        if group:
            user.groups.add(group)
        return user

    def create_superuser(self, email, password, first_name, last_name, **extra_fields):
        """
        Crear un superusuario
        """
        if not email:
            raise ValueError('Se requiere correo')
        if not password:
            raise ValueError('Se requiere contraseña')
        if not first_name:
            raise ValueError('Se requiere nombre')
        if not last_name:
            raise ValueError('Se requiere apellido')
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(email, password, first_name, last_name, **extra_fields)
