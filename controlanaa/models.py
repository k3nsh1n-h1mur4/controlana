from django.db import models
from django.db.models.fields import BigAutoField


class controlModel(models.Model):
    class Meta:
        db_table = 'controlana'

    ZONA = [
        ('ZONA AUTLÁN', 'ZONA AUTLÁN'),
        ('ZONA CD. GUZMÁN', 'ZONA CD. GUZMÁN'),
        ('ZONA METROPOLITANA', 'ZONA METROPOLITANA'),
        ('ZONA OCOTLÁN', 'ZONA OCOTLÁN'),
        ('ZONA PTO. VALLARTA', 'ZONA PTO. VALLARTA'),
        ('ZONA TALA', 'ZONA TALA'),
    ]

    id = models.BigAutoField(primary_key=True)
    n_prop = models.CharField(max_length=100, blank=True)
    f_prop = models.CharField(max_length=50, blank=True)
    n_asp = models.CharField(max_length=250, blank=True)
    propone = models.CharField(max_length=250, blank=True)
    tel = models.CharField(max_length=250, blank=True)
    zona = models.CharField(max_length=250, blank=True, choices=ZONA)
    categoria = models.CharField(max_length=150, blank=True)
    comentarios = models.CharField(max_length=250, blank=True)
    examen = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.n_prop



