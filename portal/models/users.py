from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):

   username= models.IntegerField(
       'codigo estudiante',max_length=15,required=True,unique=True)
   first_name=models.CharField('Nombre de usuario',max_length=20,required=True)
   last_name=models.CharField(
       'apellido del usuario',max_length=20,required=True)
    email = models.EmailField(blank=True, null=True)
    

    
    class Meta():
        verbose_name='Nombre'
        verbose_name_plural='Nombres'
    
    def str(self):
        return f"{self.username}- {self.fist_name}"
    


