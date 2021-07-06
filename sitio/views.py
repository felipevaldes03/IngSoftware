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
    producto = Producto.objects.get(id=producto_id)

    return render(request, 'sitio/producto/show.html',{
        'categorias' : Categoria.objects.all(),
        'producto' : producto
    })

def producto_editar(request, producto_id):
    return HttpResponse('Editar Producto con id: ' + str(producto_id))

def producto_delete(request, producto_id):
    return HttpResponse('Eliminar Producto con id: ' + str(producto_id))

def producto_search(request):
    texto_de_busqueda = request.GET["texto"]
    productosPorTitulo = Producto.objects.filter(titulo__icontains = texto_de_busqueda).all()
    productosPorDescripcion = Producto.objects.filter(descripcion__icontains = texto_de_busqueda).all()
    productos = productosPorTitulo | productosPorDescripcion
    return render(request, 'sitio/producto/search.html',
    {
        'categorias' : Categoria.objects.all(),
        'productos' : productos,
        'texto_buscado' : texto_de_busqueda,
        'titulo_seccion' : 'Productos que contienen',
        'sin_productos' : 'No hay producto de la categoria ' + texto_de_busqueda
    })

def productos_por_categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    productos = categoria.productos.all()
    return render(request, 'sitio/producto/search.html',
    {
        'categorias' : Categoria.objects.all(),
        'productos' : productos,
        'categoria' : categoria.descripcion,
        'titulo_seccion' : 'Productos de la categoria',
        'sin_productos' : 'No hay producto de la categoria ' + categoria.descripcion
    })

""" 
    PAGINAS
"""
def acerca_de(request):
    return render(request, 'sitio/paginas/acerca_de.html',{
        'categorias' : Categoria.objects.all(),
    })