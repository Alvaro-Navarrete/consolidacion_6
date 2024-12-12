from django.http import HttpRequest
from django.shortcuts import render, redirect
from .models import Vehiculos, Marcas, Categorias
from django.contrib.auth.decorators import login_required


"""
    Username: admin, editor, viewer
    Password: vehiculo123    
    
    Username Superuser: root
    Password Superuser: root
    
    
"""


def index(request):
    return render(request, 'vehiculo/index.html')


@login_required
def agregar(request: HttpRequest):
    
    if request.user.role != 'admin' and request.user.role != 'editor':
        return redirect('index')
    
    if request.method == 'POST':
        try:
            marca_id = request.POST.get('marca', '')
            modelo = request.POST.get('modelo', '')
            carroceria = request.POST.get('serial_carro', '')
            motor = request.POST.get('serial_motor', '')
            categoria_id = request.POST.get('categoria', '')
            precio = request.POST.get('precio', '')
            
            if Vehiculos.objects.filter(serial_motor=motor).exists():
                raise Exception('Vehículo ya ingresado con ese serial de motor.')
            
            
            marca = Marcas.objects.get(id = int(marca_id))
            categoria = Categorias.objects.get(id = int(categoria_id))
            
            vehiculo = Vehiculos.objects.create(
                modelo = modelo, 
                marca = marca, 
                serial_carroceria = carroceria, 
                serial_motor = motor, 
                categoria = categoria, 
                precio = precio
            )
            
            return redirect('index')
            
        except Exception as e:
            print(f'Error al crear el registro: {e}')
    
    marcas = Marcas.objects.all()
    categorias = Categorias.objects.all()
    
    return render(request, 'vehiculo/agregar.html', {'marcas' : marcas, 'categorias' : categorias})


def listar(request):
    vehiculos = Vehiculos.objects.all()
    
    return render(request, 'vehiculo/listar.html', {'vehiculos' : vehiculos})