
from django.urls import path
from .views import home,inventario,exit,listar_categorias,form_inventario_almacen,listar_inventarioAlmacen

#urls del inicio de sesion 
urlpatterns = [
    path('', home, name="home"),
    path('inventario/', inventario, name="inventario"),
    path('logout/', exit, name="exit"),
    path('listar_categorias/', listar_categorias,name='listar_categorias'),
    path('listar_inventarioAlmacen/', listar_inventarioAlmacen,name='listar_inventarioAlmacen'),
    path('formulario_inventarioAlmacen/', form_inventario_almacen,name='formInventarioAlmacen'),    

]
