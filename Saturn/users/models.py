from django.db import models

# Create your models here.
class Registro(models.Model):
        class Meta(object):
            db_table = 'Registro'
        idUsuario = models.AutoField(primary_key=True)
        email = models.CharField(max_length=50)
        password = models.CharField(max_length=50)
        nombre = models.CharField(max_length=50)
        apellido = models.CharField(max_length=50)
        dni = models.BigIntegerField()
        telefono = models.BigIntegerField()
        fechaDeNacimiento = models.DateField(auto_now=False, auto_now_add=False)
        
        SEXO = (
            ('M', 'Masculino'),
            ('F', 'Femenino'),
            ('O', 'Otros'),
        )
        sexo             = models.CharField(max_length=1, choices=SEXO)
