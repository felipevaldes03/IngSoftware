from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    descripcion = models.CharField(max_length=60, null=False)

    def __str__(self) -> str:
        return f"Id: {self.pk} | Descripcion: {self.descripcion}"


class Producto(models.Model):
    titulo = models.CharField(max_length=30, null=False)
    imagen = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=100, null=False)
    precio = models.FloatField(null=False)
    # FK
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE, related_name="productos")

    def __str__(self) -> str:
        return f"Id: {self.pk} | Titulo: {self.titulo} | Imagen: {self.imagen} | Descripcion: {self.descripcion} | Precio: {self.precio} || Categoria_id: {self.categoria.id} "


class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="carritos")
    productos = models.ManyToManyField(Producto, related_name='carritos')
    precio_total = models.FloatField(null=False)

    def __str__(self) -> str:
        return f"Id: {self.pk} | Usuario_id: {self.usuario.id} | Productos: {self.productos}"