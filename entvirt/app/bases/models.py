from django.db import models

from django.contrib.auth.models import User


class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True)
    fc = models.DateTimeField(auto_now_add=True) #para que se ponga la fecha solamente una vez
    fm = models.DateTimeField(auto_now=True) #para que se ponga la fecha cada vez que exista una transaccion
    uc = models.ForeignKey(User, on_delete=models.CASCADE)
    um = models.IntegerField(blank=True,null=True)

    class Meta:
        abstract=True