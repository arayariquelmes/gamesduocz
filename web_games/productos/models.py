from django.db import models

# Create your models here.
class Producto(models.Model):
    titulo = models.CharField(max_length=50, verbose_name="Titulo del Producto")
    descripcion = models.TextField(verbose_name="Detalle del Producto")
    imagen = models.URLField(max_length=200, verbose_name="Url de la imagen")
    precio = models.IntegerField(verbose_name="Precio del Producto")
    estaEnOferta = models.BooleanField(verbose_name="Esta en oferta?", default=False)
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de Creación") 
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización")

    #Representacion en formato texto del objeto
    def __str__(self):
        return self.titulo