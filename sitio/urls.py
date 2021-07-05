from django.urls import path
from . import views

app_name = "SITIO"
urlpatterns = [
    # ACERCA DE
    path('acercaDe/', views.acerca_de, name="acerca_de"),
    
    # PRODUCTOS
    path('', views.producto_index, name="producto_index"),
    #path('producto/agregar', views.producto_agregar, name="producto_agregar" ),
    path('producto/<int:producto_id>', views.producto_show, name="producto_show" ),
    path('producto/<int:producto_id>/editar', views.producto_editar, name="producto_editar" ),
    path('producto/<int:producto_id>/eliminar', views.producto_eliminar, name="producto_eliminar" ),
    # Productos por categorias
    path('categoria/<int:categoria_id>/productos', views.productos_por_categoria, name="productos_por_categoria"),

]