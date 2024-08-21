from django import forms
from .models import Categorias, Inventarioalmacen, Proveedores


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categorias
        fields = '__all__' 
        labels={
            'nombre':'tipo de categoria',
            'descripcion':'descripcion de la categoria',
            
        }  


class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventarioalmacen
        fields = ['nombre_producto', 'descripcion', 'categoria', 'cantidad_en_stock', 'precio', 'estado_producto', 'proveedor']
