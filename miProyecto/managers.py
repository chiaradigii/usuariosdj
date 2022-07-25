from django.db import models
#
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager, models.Manager):
    
    def _create_user(self,username,nombre,apellido,email,password,is_staff,is_superuser,is_active, **extra_fields):
        user= self.model(
            username=username,
            nombre=nombre,
            apellido=apellido,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user


    def create_user(self,username,nombre,apellido,email,password=None,**extra_fields):
        return self._create_user(username,nombre,apellido,email,password,False,False,False, **extra_fields)

    def create_superuser(self,username,nombre,apellido,email,password=None,**extra_fields):
        return self._create_user(username,nombre,apellido,email,password,True,True,True, **extra_fields) 
    
    def cod_validation(self, id, cod_registro):
        if self.filter(id=id , codregistro = cod_registro): #existe la consulta
            return True
        else:
            return False
