from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from .models import Categorias,Inventarioalmacen,Proveedores,Inventariotienda,Rotacioninventario,Tiposderopa
from .forms import InventarioForm,CategoriaForm,ProveedorForm,InventarioTiendaForm,RotacionInventarioForm,TiposRopaForm

# vista del home
def home(request):
    # Consultar todas las instancias del modelo
    inventario = Inventarioalmacen.objects.all()
    
    # Extraer las cantidades en stock y los nombres de las categorías
    cantidades_en_stock = [item.cantidad_en_stock for item in inventario]
    nombres_categorias = [item.categoria.nombre for item in inventario if item.categoria]  # Verificar que item.categoria no sea None

    # Agrega líneas de depuración para ver lo que se está pasando al contexto
    print("Cantidades en stock:", cantidades_en_stock)  # Esto se mostrará en la consola
    print("Nombres de categorías:", nombres_categorias)  # Esto se mostrará en la consola

    # Devolver la lista al contexto
    return render(request, 'htmls/home.html', {
        'cantidades_en_stock': cantidades_en_stock,
        'nombres_categorias': nombres_categorias,
    })

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

#listado de la tabla de los tipos de ropa
def listar_tiposRopa(request):
    context = {'listar_tiposRopa' : Tiposderopa.objects.all()}
    return render(request, 'htmls/listar_tiposRopa.html',context)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#formulario del inventario de almacen
def form_inventario_almacen(request):
    if request.method == 'GET': 
        return render(request, 'htmls/formInventarioAlmacen.html', {
            'formInvAlm': InventarioForm
        })
    else:
        form= InventarioForm(request.POST)
        if form.is_valid():
            new_datos = form.save(commit=False)
            new_datos.save()
            messages.add_message(request=request, level=messages.SUCCESS, message='Producto agregado al almacen con éxito')
            return redirect('listar_inventarioAlmacen')
        else:
            messages.add_message(request=request, level=messages.ERROR, message='Error al agregar Producto al almacén')
            return redirect('listar_inventarioAlmacen')    


#formulario de las categorias
def form_categorias(request):
    if request.method == 'GET': 
        return render(request, 'htmls/formCategorias.html', {
            'formCat': CategoriaForm
        })
    else:
        form= CategoriaForm(request.POST)
        if form.is_valid():
            new_datos = form.save(commit=False)
            new_datos.save()
            messages.add_message(request=request, level=messages.SUCCESS, message='Categoría Agregada con éxito')
            return redirect('listar_categorias')
        else:
            messages.add_message(request=request, level=messages.ERROR, message='Error al agregar Categoría')
            return redirect('listar_categorias')


#formulario de los proveedores
def form_proveedores(request):
    if request.method == 'GET': 
        return render(request, 'htmls/formProveedores.html', {
            'formProv': ProveedorForm
        })
    else:
        form= ProveedorForm(request.POST)
        if form.is_valid():
            new_datos = form.save(commit=False)
            new_datos.save()
            messages.add_message(request=request, level=messages.SUCCESS, message='Proveedor Agregado con éxito')
            return redirect('listar_proveedores')
        else:
            messages.add_message(request=request, level=messages.ERROR, message='Error al agregar Proveedor')
            return redirect('listar_proveedores')


# formulario de inventario Tienda
def form_inventarioTienda(request):
    if request.method == 'GET': 
        return render(request, 'htmls/formInventarioTienda.html', {
            'formInvTi': InventarioTiendaForm
        })
    else:
        form= InventarioTiendaForm(request.POST)
        if form.is_valid():
            new_datos = form.save(commit=False)
            new_datos.save()
            messages.add_message(request=request, level=messages.SUCCESS, message='Producto Agregado al inventario de la Tienda con éxito')
            return redirect('listar_inventarioTienda')
        else:
            messages.add_message(request=request, level=messages.ERROR, message='Error al agregar Producto al inventario de la Tienda')
            return redirect('listar_inventarioTienda')


#formulario de la rotacion de inventario
def form_rotacionInventario(request):
    if request.method == 'GET': 
        return render(request, 'htmls/formRotacionInventario.html', {
            'formRot': RotacionInventarioForm
        })
    else:
        form= RotacionInventarioForm(request.POST)
        if form.is_valid():
            new_datos = form.save(commit=False)
            new_datos.save()
            messages.add_message(request=request, level=messages.SUCCESS, message='Rotación de inventario agregada con éxito')
            return redirect('listar_rotacionInventario')
        else:
            messages.add_message(request=request, level=messages.ERROR, message='Error al agregar Rotación de inventario')
            return redirect('listar_rotacionInventario')

#formulario Tipos de Ropa
def form_tiposRopa(request):
    if request.method == 'GET': 
        return render(request, 'htmls/formTiposRopa.html', {
            'formTipRop': TiposRopaForm
        })
    else:
        form= TiposRopaForm(request.POST)
        if form.is_valid():
            new_datos = form.save(commit=False)
            new_datos.save()
            messages.add_message(request=request, level=messages.SUCCESS, message='Tipo de Ropa agregado con éxito')
            return redirect('listar_tiposRopa')
        else:
            messages.add_message(request=request, level=messages.ERROR, message='Error al agregar Tipo de Ropa')
            return redirect('listar_tiposRopa')

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#actualizar(update) categorias:
def actualizar_categoria(request,categoria_id):
    if request.method == 'GET':
            categ= get_object_or_404(Categorias,pk=categoria_id)
            form = CategoriaForm(instance=categ)
            return render(request, 'htmls/formCategorias.html', {
                'formCat': form
            })
    else:
        try:
            categ= get_object_or_404(Categorias,pk=categoria_id)
            form= CategoriaForm(request.POST, instance=categ)
            form.save()
            messages.add_message(request=request, level=messages.SUCCESS, message='Categoría actualizada con éxito')
            return redirect('listar_categorias')
        except ValueError:
            messages.add_message(request=request, level=messages.ERROR, message='Error al actualizar Categoría')
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
        try:
            invAlm= get_object_or_404(Inventarioalmacen,pk=invAlmacen_id)
            formInv= InventarioForm(request.POST, instance=invAlm)
            formInv.save()
            messages.add_message(request=request, level=messages.SUCCESS, message='Producto de Almacén actualizado con éxito')
            return redirect('listar_inventarioAlmacen')
        except ValueError:
            messages.add_message(request=request, level=messages.ERROR, message='Error al actualizar Producto de Almacén')
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
        try:
            prov= get_object_or_404(Proveedores,pk=proveedor_id)
            formProv= ProveedorForm(request.POST, instance=prov)
            formProv.save()
            messages.add_message(request=request, level=messages.SUCCESS, message='Proveedor actualizado con éxito')
            return redirect('listar_proveedores')
        except ValueError:
            messages.add_message(request=request, level=messages.ERROR, message='Error al actualizar Proveedor')
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
        try:
            invTi= get_object_or_404(Inventariotienda,pk=invTienda_id)
            formInv= InventarioTiendaForm(request.POST, instance=invTi)
            new_datos = formInv.save(commit=False)
            new_datos.save()
            messages.add_message(request=request, level=messages.SUCCESS, message='Producto de Tienda actualizado con éxito')
            return redirect('listar_inventarioTienda')
        except ValueError:
            messages.add_message(request=request, level=messages.ERROR, message='Error al actualizar Producto del inventario de Tienda')
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
            messages.add_message(request=request, level=messages.SUCCESS, message='Rotación actualizada con éxito')
            return redirect('listar_rotacionInventario')
        except ValueError:
            messages.add_message(request=request, level=messages.ERROR, message='Error al actualizar Rotación de inventario')
            return redirect('listar_rotacionInventario')

#actualizar(update) Tipos de Ropa:
def actualiza_tiposRopa(request,tipoRopa_id):
    if request.method == 'GET':
            tiposRop= get_object_or_404(Tiposderopa,pk=tipoRopa_id)
            formtiposRopa = TiposRopaForm(instance=tiposRop)
            return render(request, 'htmls/formTiposRopa.html', {
                'formTipRop': formtiposRopa
            })
    else:
        try:
            tiposRop= get_object_or_404(Tiposderopa,pk=tipoRopa_id)
            formtiposRopa= TiposRopaForm(request.POST, instance=tiposRop)
            formtiposRopa.save()
            messages.add_message(request=request, level=messages.SUCCESS, message='Tipo de Ropa actualizada con éxito')
            return redirect('listar_tiposRopa')
        except ValueError:
            messages.add_message(request=request, level=messages.ERROR, message='Error al actualizar Tipo de Ropa')
            return redirect('listar_tiposRopa')


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#eliminar categoria:
def eliminar_categoria(request, categoria_id):
    if request.method == "POST":
        elimCat = get_object_or_404(Categorias, pk=categoria_id)
        
        # Obtener la contraseña ingresada por el usuario
        password = request.POST.get('password')
        
        # Obtener el usuario autenticado
        user = request.user
        
        # Verificar si el usuario está autenticado y es superusuario
        if user.is_authenticated and user.is_superuser:
            # Autenticar al usuario con la contraseña proporcionada
            authenticated_user = authenticate(request, username=user.username, password=password)
            if authenticated_user is not None:
                # Si la autenticación es exitosa, eliminar la categoría
                elimCat.delete()
                messages.success(request, 'Categoría eliminada correctamente.')
            else:
                messages.error(request, 'Contraseña incorrecta. No se pudo eliminar la categoría.')
        else:
            messages.error(request, 'No tienes permisos para realizar esta acción.')
    
    return redirect('listar_categorias')

#eliminar Inventario almacen:
def eliminar_inventarioAlmacen(request,invAlmacen_id):
    elimInvAlm = get_object_or_404(Inventarioalmacen,pk=invAlmacen_id)
    elimInvAlm.delete()
    messages.add_message(request, messages.SUCCESS, 'Producto de Almacén eliminado correctamente')
    return redirect('listar_inventarioAlmacen')

#eliminar proveedores:
def eliminar_proveedor(request,proveedor_id):
    elimProv = get_object_or_404(Proveedores,pk=proveedor_id)
    elimProv.delete()
    messages.add_message(request,messages.SUCCESS, 'Proveedor eliminado correctamente')
    return redirect('listar_proveedores')

#eliminar inventario tienda:
def eliminar_inventarioTienda(request,invTienda_id):
    elimInvTi = get_object_or_404(Inventariotienda,pk=invTienda_id)
    elimInvTi.delete()
    messages.add_message(request, messages.SUCCESS, 'Producto de Tienda eliminado correctamente')
    return redirect('listar_inventarioTienda')

#eliminar rotacion de inventario:
def eliminar_rotacionInventario(request,rotacion_id):
    elimRot = get_object_or_404(Rotacioninventario,pk=rotacion_id)
    elimRot.delete()
    messages.add_message(request, messages.SUCCESS, 'Rotación de Inventario eliminada correctamente')
    return redirect('listar_rotacionInventario')

#eliminar Tipo de Ropa:
def eliminar_tipoRopa(request,tipoRopa_id):
    if request.method == "POST":
        elimTipoRopa = get_object_or_404(Tiposderopa,pk=tipoRopa_id)
        password = request.POST.get('password')
        user = request.user
        if user.is_authenticated and user.is_superuser:
            # Autenticar al usuario con la contraseña proporcionada
            authenticated_user = authenticate(request, username=user.username, password=password)
            if authenticated_user is not None:
                # Si la autenticación es exitosa, eliminar la categoría
                elimTipoRopa.delete()
                messages.add_message(request, messages.SUCCESS, 'Tipo de Ropa eliminado correctamente')
            else:
                messages.error(request, 'Contraseña incorrecta. No se pudo eliminar la categoría.')
        else:
            messages.error(request, 'No tienes permisos para realizar esta acción.')
    
    return redirect('listar_tiposRopa')

def stock_view(request):
    # Consultar todas las instancias del modelo
    inventario = Inventarioalmacen.objects.all()
    
    # Extraer las cantidades en stock y almacenarlas en un array
    cantidades_en_stock = [item.cantidad_en_stock for item in inventario]

    # Agrega una línea de depuración para ver lo que se está pasando al contexto
    print("Cantidades en stock:", cantidades_en_stock)  # Esto se mostrará en la consola

    # Devolver la lista al contexto
    return render(request, 'htmls/home.html', {'cantidades_en_stock': cantidades_en_stock})