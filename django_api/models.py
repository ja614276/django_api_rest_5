from django.db import models

# Create your models here.

class Product(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_vencimiento = models.DateField()