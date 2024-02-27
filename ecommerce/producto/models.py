from django.db import models

# Create your models here.

class Producto(models.Model):
    name = models.CharField(max_length = 100,verbose_name="Nombre del producto")
    description = models.TextField(verbose_name="Descripcion del producto",null=True,blank=True)
    image = models.ImageField(null=True,blank=True)
    price = models.DecimalField(max_digits=9,decimal_places=2,verbose_name="Precio del producto",null = False,blank=False)
    category = models.ForeignKey("Categoria",on_delete = models.CASCADE,related_name="categoria",null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Categoria(models.Model):
    name = models.CharField(max_length = 100,verbose_name="Nombre de la categoria")

    def __str__(self):
        return self.name


