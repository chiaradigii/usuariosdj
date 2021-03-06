from operator import mod
from pyexpat import model
from django.db import models

from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin

from miProyecto.managers import UserManager



class User(AbstractBaseUser,PermissionsMixin):
    """Model definition for User."""
    objects = UserManager()

    GENDER_CHOICES = (
        ('M','Masculino'),
        ('F','Femenino'),
        ('O','Otros'),
    )

    username = models.CharField(max_length=15,unique=True)
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    genero=models.CharField(max_length=1,choices=GENDER_CHOICES,blank=True)
    codregistro = models.CharField(max_length=6,default='000000')

    REQUIRED_FIELDS = ['email','nombre','apellido']
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False) 
    USERNAME_FIELD = 'username'

    def get_short_name(self):
        return self.username
    def get_full_name(self):
        return self.nombre + " " + self.apellido