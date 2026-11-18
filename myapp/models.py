from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    age = models.IntegerField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} {self.last_name}"


class Programa(models.Model):
    """Programa universitario. El campo id lo crea Django automáticamente."""

    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=200)
    estado = models.BooleanField(default=True)
    facultad = models.CharField(max_length=200)

    class Meta:
        ordering = ["codigo"]
        verbose_name = "programa"
        verbose_name_plural = "programas"

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"
