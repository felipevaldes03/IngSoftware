from django.urls import path
from . import views

app_name = "SITIO"
urlpatterns = [
    # ACERCA DE
    path('acercaDe/', views.acerca_de, name="acerca_de"),
    
    # PRODUCTOS
    path('', views.producto_index, name="producto_index"),
    path('producto/agregar', views.producto_create, name="producto_create" ),
    path('producto/<int:producto_id>', views.producto_show, name="producto_show" ),
    path('producto/<int:producto_id>/editar', views.producto_edit, name="producto_edit" ),
    path('producto/<int:producto_id>/eliminar', views.producto_delete, name="producto_delete" ),
    path('producto/buscador', views.producto_search, name="producto_search"),
    path('categoria/<int:categoria_id>/productos', views.productos_por_categoria, name="productos_por_categoria"),

]