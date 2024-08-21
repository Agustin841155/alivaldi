from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Categorias,Inventarioalmacen
from .forms import InventarioForm

# vista del home
def home(request):
    return render (request, 'htmls/home.html')

#vista del inventario
@login_required
def inventario(request):
    return render (request, 'htmls/inventario.html')

#salida logout
def exit(request):
    logout(request)
    return redirect('home')

#listado de tabla de categorias
def listar_categorias(request):
    context = {'listar_categorias' : Categorias.objects.all()}
    return render(request, 'htmls/listarCategorias.html',context)

#listado de tabla de inventario Almacen
def listar_inventarioAlmacen(request):
    context = {'listar_inventarioAlmacen' : Inventarioalmacen.objects.all()}
    return render(request, 'htmls/listar_inventarioAlmacen.html',context)

#formulario del inventario de almacen
def form_inventario_almacen(request):
    if request.method == 'GET': 
        return render(request, 'htmls/formInventarioAlmacen.html', {
            'form': InventarioForm
        })
    else:
        form= InventarioForm(request.POST)
        new_datos = form.save(commit=False)
        new_datos.save()
        return redirect('listar_inventarioAlmacen')