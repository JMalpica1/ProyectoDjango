from django.db import models



class Usuario(models.Model):
    rut = models.CharField(primary_key=True, verbose_name="Rut")
    nombres=models.CharField(max_length=80, blank=False, null=False, verbose_name="Nombre")
    direccion=models.CharField(max_length=80, blank=False, null=False, verbose_name="Direccion")
    apellido=models.CharField(max_length=80, blank=False, null=False, verbose_name="Apellido")
    email=models.CharField(max_length=80, blank=False, null=False, verbose_name="email")
    password=models.CharField(max_length=80, blank=False, null=False, verbose_name="contraseña")
    imagen = models.ImageField(upload_to="images/", default="sinfoto.jpg", null=False, blank=False, verbose_name="Imagen")

    def __str__(self):
        return self.usuario

class Producto(models.Model):
    codigo=models.IntegerField(primary_key=True,verbose_name="Codigo")
    categoria=models.CharField(max_length=30, null=False, blank=False, verbose_name="Categoria")
    precio=models.IntegerField(max_length=10, blank=False, null=False, verbose_name="Precio")
    descuentosus = models.DecimalField(max_digits=5, decimal_places=1, verbose_name="Descuento Suscriptor")
    descuentoof=models.DecimalField(max_digits=5, decimal_places=1, verbose_name="Descuento Oferta")
    imagen = models.ImageField(upload_to="images/", default="sinfoto.jpg", null=False, blank=False, verbose_name="Imagen")

def __str__(self):
    return self.codigo