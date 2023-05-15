from django.db import models
from django.db.models.fields import BigAutoField


class controlModel(models.Model):
    class Meta:
        db_table = 'controlTable'

    id = models.BigAutoField(primary_key=True)
    ppta = models.CharField(max_length=100, blank=True)
    fecha = models.CharField(max_length=50, blank=True)
    aspirante = models.CharField(max_length=250, blank=True)
    categoria = models.CharField(max_length=250, blank=True)
    propone = models.CharField(max_length=250, blank=True)
    telefono = models.CharField(max_length=250, blank=True)
    zona = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.aspirante



