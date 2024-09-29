
from django.urls import path
from . import views


#urls del inicio de sesion 
urlpatterns = [
    path('', views.home, name="home"),
    path('inventario/', views.inventario, name="inventario"),
    path('logout/', views.exit, name="exit"),

    path('listar_categorias/', views.listar_categorias,name='listar_categorias'),
    path('formulario_Categorias/', views.form_categorias,name='formCategorias'),
    path('categoria/<int:categoria_id>/', views.actualizar_categoria, name= 'update_categorias'),
    path('eliminarCat/<int:categoria_id>/', views.eliminar_categoria, name= 'delete_categoria'),

    path('listar_inventarioAlmacen/', views.listar_inventarioAlmacen,name='listar_inventarioAlmacen'),
    path('formulario_inventarioAlmacen/', views.form_inventario_almacen,name='formInventarioAlmacen'),
    path('invAlm/<int:invAlmacen_id>/', views.actualizar_inventarioAlmacen, name= 'update_inventarioAlmacen'),
    path('eliminarinvAlm/<int:invAlmacen_id>/', views.eliminar_inventarioAlmacen, name= 'delete_inventarioAlmacen'),

    path('listar_proveedores/', views.listar_proveedores,name='listar_proveedores'),
    path('formulario_proveedores/', views.form_proveedores,name='formProveedores'),
    path('proveedores/<int:proveedor_id>/', views.actualizar_proveedor, name= 'update_proveedor'),
    path('eliminarProv/<int:proveedor_id>/', views.eliminar_proveedor, name= 'delete_proveedores'),

    path('listar_inventarioTienda/', views.listar_inventarioTienda,name='listar_inventarioTienda'),
    path('formulario_inventarioTienda/', views.form_inventarioTienda,name='formInventarioTienda'),
    path('inventarioTienda/<int:invTienda_id>/', views.actualizar_inventarioTienda, name= 'update_inventarioTienda'),
    path('eliminarInvTienda/<int:invTienda_id>/', views.eliminar_inventarioTienda, name= 'delete_inventarioTienda'),

    path('listar_rotacionInventario/', views.listar_rotacionInventario,name='listar_rotacionInventario'),
    path('formulario_rotacionInventario/', views.form_rotacionInventario,name='formRotacionInventario'),
    path('rotacionInventario/<int:rotacion_id>/', views.actualizar_rotacionInventario, name= 'update_rotacionInventario'),
    path('eliminarrotacionInventario/<int:rotacion_id>/', views.eliminar_rotacionInventario, name= 'delete_rotacionInventario'),

    path('listar_tiposRopa/', views.listar_tiposRopa,name='listar_tiposRopa'),
    path('formulario_tiposRopa/', views.form_tiposRopa,name='formTiposRopa'),
    path('tiposRopa/<int:tipoRopa_id>/', views.actualiza_tiposRopa, name= 'update_tiposRopa'),
    path('eliminarTiposRopa/<int:tipoRopa_id>/', views.eliminar_tipoRopa, name= 'delete_tiposRopa'),
]
