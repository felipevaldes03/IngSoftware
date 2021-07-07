from django.contrib.auth.models import User
from sitio.forms import FormProducto
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http.response import HttpResponse, HttpResponseRedirect

from sitio.models import *

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
def producto_create(request):
    categorias = Categoria.objects.all()
    if request.method == "POST":
        categoria_del_producto = Categoria.objects.get(id=request.POST["categoria"])
        form = FormProducto(request.POST, request.FILES, instance=Producto(imagen=request.FILES['imagen'], categoria=categoria_del_producto))   
        if form.is_valid():
            #return HttpResponse('Los campos fueron validados y aceptados!!! ' + str(categoria_del_producto))
            form.save()
            return redirect("SITIO:producto_index")
        else:
            return render(request, 'sitio/producto/create.html', {
                'categorias' : categorias,
                'error_message' : 'Ingreso un campo incorrecto, vuelva a intentar'
            })
    else:
        return render(request, 'sitio/producto/create.html', {
            'categorias' : categorias
        })

def producto_show(request, producto_id):
    producto =  get_object_or_404(Producto, id=producto_id)

    return render(request, 'sitio/producto/show.html',{
        'categorias' : Categoria.objects.all(),
        'producto' : producto
    })

def producto_edit(request, producto_id):
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
    
    #categoria = Categoria.objects.get(id=categoria_id)
    categoria = get_object_or_404(Categoria, id = categoria_id)
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
    CARRITO
"""
def carrito_index(request):
    categorias = Categoria.objects.all()
    usuario_logeado = User.objects.get(username=request.user)
    productos = Carrito.objects.get(usuario=usuario_logeado.id).items.all()

    return render(request, 'sitio/carrito/index.html', {
        'categorias' : categorias,
        'usuario' : usuario_logeado,
        'items_carrito' : productos
    })

def carrito_save(request):
    #tieneCarrito = Carrito.objects.filter(usuario=8).count()
    # Devuelve un 404 si no encuentra el carrito
    #arrito = get_object_or_404(Carrito, usuario=usuario_logeado.id)

    if request.method == 'POST':
        producto = Producto.objects.get(id=request.POST['producto_id'])
        usuario_logeado = User.objects.get(username=request.user)

        # ESTO PUEDE IR EN EL REGISTRO DEL USUARIO
        # Si el usuario no tiene carrito lo creo
        if Carrito.objects.filter(usuario=usuario_logeado.id).count() == 0:
            carrito = Carrito()
            carrito.usuario = usuario_logeado
            carrito.total = 0
            carrito.save()

        # Agrego producto al carrito
        carrito = Carrito.objects.get(usuario=usuario_logeado.id)
        item_carrito = Carrito_item()
        item_carrito.carrito = carrito
        item_carrito.producto = producto
        item_carrito.save()

        # Sumo el precio del producto al carrito
        carrito.total = producto.precio + carrito.total
        carrito.save()

        #return HttpResponse(f"{usuario_logeado.id} | ITEM_CARRITO: {item_carrito} | CARRITO: {carrito}")
        return redirect("SITIO:producto_index")

    else:
        return redirect("SITIO:producto_index")

def item_carrito_delete(request, item_carrito_id):
    item_carrito = Carrito_item.objects.get(id=item_carrito_id)
    carrito = item_carrito.carrito
    precio_item = item_carrito.producto.precio
    
    carrito.total = carrito.total - precio_item
    item_carrito.delete()
    carrito.save()
    return redirect("SITIO:carrito_index")
    #return HttpResponse(f'Carrito_id: {carrito.id} Total: {carrito.total} | Item_carrito: {item_carrito} | Precio: {precio_item}')

"""
    PAGINAS
"""
def acerca_de(request):
    return render(request, 'sitio/paginas/acerca_de.html',{
        'categorias' : Categoria.objects.all(),
    })