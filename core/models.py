from django.db import models
from django.utils import timezone


# Create your models here.
class Documento(models.Model):
    dados = models.JSONField()
    data_gerado = models.DateTimeField(default=timezone.now)
    usuario = models.CharField(max_length=20)