from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Categorias,Inventarioalmacen,Proveedores,Inventariotienda,Rotacioninventario
from .forms import InventarioForm,CategoriaForm,ProveedorForm,InventarioTiendaForm,RotacionInventarioForm

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

#listado de tabla de proveedores
def listar_proveedores(request):
    context = {'listar_proveedores' : Proveedores.objects.all()}
    return render(request, 'htmls/listar_proveedores.html',context)

#listado de tabla de inventario Tienda
def listar_inventarioTienda(request):
    context = {'listar_inventarioTienda' : Inventariotienda.objects.all()}
    return render(request, 'htmls/listar_inventarioTienda.html',context)

#listado de la tabla de rotacion de Inventario
def listar_rotacionInventario(request):
    context = {'listar_rotacionInventario' : Rotacioninventario.objects.all()}
    return render(request, 'htmls/listar_rotacionInventario.html',context)


#formulario del inventario de almacen
def form_inventario_almacen(request):
    if request.method == 'GET': 
        return render(request, 'htmls/formInventarioAlmacen.html', {
            'formInvAlm': InventarioForm
        })
    else:
        form= InventarioForm(request.POST)
        new_datos = form.save(commit=False)
        new_datos.save()
        return redirect('listar_inventarioAlmacen')


#formulario de las categorias
def form_categorias(request):
    if request.method == 'GET': 
        return render(request, 'htmls/formCategorias.html', {
            'formCat': CategoriaForm
        })
    else:
        form= CategoriaForm(request.POST)
        new_datos = form.save(commit=False)
        new_datos.save()
        return redirect('listar_categorias')


#formulario de los proveedores
def form_proveedores(request):
    if request.method == 'GET': 
        return render(request, 'htmls/formProveedores.html', {
            'formProv': ProveedorForm
        })
    else:
        form= ProveedorForm(request.POST)
        new_datos = form.save(commit=False)
        new_datos.save()
        return redirect('listar_proveedores')


# formulario de inventario Tienda
def form_inventarioTienda(request):
    if request.method == 'GET': 
        return render(request, 'htmls/formInventarioTienda.html', {
            'formInvTi': InventarioTiendaForm
        })
    else:
        form= InventarioTiendaForm(request.POST)
        new_datos = form.save(commit=False)
        new_datos.save()
        return redirect('listar_inventarioTienda')


#formulario de la rotacion de inventario
def form_rotacionInventario(request):
    if request.method == 'GET': 
        return render(request, 'htmls/formRotacionInventario.html', {
            'formRot': RotacionInventarioForm
        })
    else:
        form= RotacionInventarioForm(request.POST)
        new_datos = form.save(commit=False)
        new_datos.save()
        return redirect('listar_rotacionInventario')
    

#actualizar(update) categorias:
def actualizar_categoria(request,categoria_id):
    if request.method == 'GET':
            categ= get_object_or_404(Categorias,pk=categoria_id)
            form = CategoriaForm(instance=categ)
            return render(request, 'htmls/formCategorias.html', {
                'formCat': form
            })
    else:
        categ= get_object_or_404(Categorias,pk=categoria_id)
        form= CategoriaForm(request.POST, instance=categ)
        form.save()
        return redirect('listar_categorias')


#actualizar(update) inventario almacen:
def actualizar_inventarioAlmacen(request,invAlmacen_id):
    if request.method == 'GET':
            invAlm= get_object_or_404(Inventarioalmacen,pk=invAlmacen_id)
            formInv = InventarioForm(instance=invAlm)
            return render(request, 'htmls/formInventarioAlmacen.html', {
                'formInvAlm': formInv
            })
    else:
        invAlm= get_object_or_404(Inventarioalmacen,pk=invAlmacen_id)
        formInv= InventarioForm(request.POST, instance=invAlm)
        formInv.save()
        return redirect('listar_inventarioAlmacen')
    
#actualizar(update) proveedores:
def actualizar_proveedor(request,proveedor_id):
    if request.method == 'GET':
        prov= get_object_or_404(Proveedores,pk=proveedor_id)
        formProv = ProveedorForm(instance=prov)
        return render(request, 'htmls/formProveedores.html', {
            'formProv': formProv
            })
    else:
        prov= get_object_or_404(Proveedores,pk=proveedor_id)
        formProv= ProveedorForm(request.POST, instance=prov)
        formProv.save()
        return redirect('listar_proveedores')
    
#actualizar(update) inventario tienda:
def actualizar_inventarioTienda(request,invTienda_id):
    if request.method == 'GET':
        invTi= get_object_or_404(Inventariotienda,pk=invTienda_id)
        formInv = InventarioTiendaForm(instance=invTi)
        return render(request, 'htmls/formInventarioTienda.html', {
            'formInvTi': formInv
            })
    else:
        invTi= get_object_or_404(Inventariotienda,pk=invTienda_id)
        formInv= InventarioTiendaForm(request.POST, instance=invTi)
        new_datos = formInv.save(commit=False)
        new_datos.save()
        return redirect('listar_inventarioTienda')
    
#actualizar(update) rotacion de inventario:
def actualizar_rotacionInventario(request,rotacion_id):
    if request.method == 'GET':
        rotacion= get_object_or_404(Rotacioninventario,pk=rotacion_id)
        formRot = RotacionInventarioForm(instance=rotacion)
        return render(request, 'htmls/formRotacionInventario.html', {
            'formRot': formRot
            })
    else:
        try:
            rotacion= get_object_or_404(Rotacioninventario,pk=rotacion_id)
            formRot= RotacionInventarioForm(request.POST, instance=rotacion)
            formRot.save()
            return redirect('listar_rotacionInventario')
        except ValueError:
            return render(request, 'htmls/formRotacionInventario.html', {
            'formRot': formRot,'errorRot':"error en la actualizacion de la rotacion de inventario"
            })
        
#eliminar categoria:
def eliminar_categoria(request,categoria_id):
    elimCat = get_object_or_404(Categorias,pk=categoria_id)
    elimCat.delete()
    return redirect('listar_categorias')

#eliminar Inventario almacen:
def eliminar_inventarioAlmacen(request,invAlmacen_id):
    elimInvAlm = get_object_or_404(Inventarioalmacen,pk=invAlmacen_id)
    elimInvAlm.delete()
    return redirect('listar_inventarioAlmacen')

#eliminar proveedores:
def eliminar_proveedor(request,proveedor_id):
    elimProv = get_object_or_404(Proveedores,pk=proveedor_id)
    elimProv.delete()
    return redirect('listar_proveedores')

#eliminar inventario tienda:
def eliminar_inventarioTienda(request,invTienda_id):
    elimInvTi = get_object_or_404(Inventariotienda,pk=invTienda_id)
    elimInvTi.delete()
    return redirect('listar_inventarioTienda')

#eliminar rotacion de inventario:
def eliminar_rotacionInventario(request,rotacion_id):
    elimRot = get_object_or_404(Rotacioninventario,pk=rotacion_id)
    elimRot.delete()
    return redirect('listar_rotacionInventario')