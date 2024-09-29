from django import forms
from .models import Categorias, Inventarioalmacen, Proveedores,Inventariotienda,Rotacioninventario,Tiposderopa


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categorias
        fields = '__all__' 
        labels={
            'Nombre':'tipo de categoria',
            'Descripción':'descripcion de la categoria',
            
        }  


class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventarioalmacen
        fields = ['nombre_producto', 'descripcion', 'categoria', 'cantidad_en_stock', 'precio', 'estado_producto', 'proveedor']

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedores
        fields = ['nombre', 'descripcion', 'telefono', 'email']

class InventarioTiendaForm(forms.ModelForm):
    class Meta:
        model = Inventariotienda
        fields = ['categoria', 'cantidad_en_stock', 'actualizado_por', 'tipo_de_ropa', 'descripcion']

class RotacionInventarioForm(forms.ModelForm):
    class Meta:
        model = Rotacioninventario
        fields = ['categoria_origen', 'categoria_destino', 'cantidad_movida','realizado_por','comentario']

class TiposRopaForm(forms.ModelForm):
    class Meta:
        model = Tiposderopa
        fields = ['tipo','descripcion']