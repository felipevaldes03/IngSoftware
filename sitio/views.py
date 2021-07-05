from django.shortcuts import render, redirect
from django.urls import reverse
from django.http.response import HttpResponse, HttpResponseRedirect

from sitio.models import Categoria, Producto

""" 
    PRODUCTOS
"""
def producto_index(request):
    productos = Producto.objects.all().order_by("-id")
    
    return render(request, "sitio/producto/index.html", {
        'categorias' : Categoria.objects.all(),
        'productos_top3' : productos[:3],
        'productos' : productos[3:10]
    })

# PARA ADMINS/MODERADORES
def producto_agregar(request):
    pass

def producto_show(request, producto_id):
    return HttpResponse('Ver Producto con id: ' + str(producto_id))

def producto_editar(request, producto_id):
    return HttpResponse('Editar Producto con id: ' + str(producto_id))

def producto_eliminar(request, producto_id):
    return HttpResponse('Eliminar Producto con id: ' + str(producto_id))

def productos_por_categoria(request, categoria_id):
    return HttpResponse('Categoria con id: ' + str(categoria_id))

""" 
    PAGINAS
"""
def acerca_de(request):
    return render(request, 'sitio/paginas/acerca_de.html')