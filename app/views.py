from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from app.forms import InsertarRestaurante, ModificarRestaurante, BuscarRestaurante
from app.models import insertarEnBD, buscarEnBD, actualizarEnBD
from django.contrib import messages
import requests

# Create your views here.

@login_required
def index(request):
    return render(request,'index.html', {})

@login_required
def insertar_restaurante(request):
    mensaje = None
    if request.method == 'GET':
        form = InsertarRestaurante()
    else:
        form = InsertarRestaurante(request.POST)

        #Si los datos son validos, creamos un nuevo restaurante y redirigimos al usuario
        if form.is_valid():
            id_restaurante = form.cleaned_data['id_restaurante']
            nombre = form.cleaned_data['nombre']
            edificio = form.cleaned_data['edificio']
            calle = form.cleaned_data['calle']
            cp = form.cleaned_data['codigo_postal']
            barrio = form.cleaned_data['barrio']
            cocina = form.cleaned_data['tipo_cocina']
            calificacion = form.cleaned_data['calificacion']
            puntuacion = form.cleaned_data['puntuacion']

            insertarEnBD(id_restaurante, nombre, edificio, calle, cp, barrio, cocina, calificacion, puntuacion)
            messages.success(request, 'El restaurante ha sido insertado correctamente')
            #Para limpiar los inputs despues de pulsar sobre "insertar"
            form = InsertarRestaurante()

    return render(request, 'insertar_restaurante.html', {'form': form})

@login_required
def modificar_restaurante(request):
    id_r = request.GET['id']
    nombre_r = request.GET['nombre']
    edificio_r = request.GET['edificio']
    calle_r = request.GET['calle']
    cp_r = request.GET['cp']
    barrio_r = request.GET['barrio']
    cocina_r = request.GET['cocina']

    if request.method == 'GET':
        form = ModificarRestaurante(initial={'id_restaurante': id_r, 'nombre': nombre_r, 'edificio': edificio_r, 'calle': calle_r, 'codigo_postal': cp_r, 'barrio': barrio_r, 'tipo_cocina': cocina_r})
    else:
        form = ModificarRestaurante(request.POST)

        if form.is_valid():
            id_r = form.cleaned_data['id_restaurante']
            nombre_r = form.cleaned_data['nombre']
            edificio_r = form.cleaned_data['edificio']
            calle_r = form.cleaned_data['calle']
            cp_r = form.cleaned_data['codigo_postal']
            barrio_r = form.cleaned_data['barrio']
            cocina_r = form.cleaned_data['tipo_cocina']
            print id_r
            print nombre_r
            print edificio_r
            print calle_r
            print cp_r
            print barrio_r
            print cocina_r
            actualizarEnBD(id_r, edificio_r, calle_r, cp_r, barrio_r, cocina_r)
            messages.success(request, 'El restaurante ha sido modificado correctamente')

    return render(request, 'modificar_restaurante.html', {'form': form})

@login_required
def buscar_restaurante(request):
    restaurantes = []
    if request.method == 'GET':
        form = BuscarRestaurante()
    else:
        form = BuscarRestaurante(request.POST)

        if form.is_valid():
            id_restaurante = form.cleaned_data['id_restaurante']
            nombre = form.cleaned_data['nombre']
            barrio = form.cleaned_data['barrio']
            cocina = form.cleaned_data['tipo_cocina']
            calle = form.cleaned_data['calle']
            cp = form.cleaned_data['codigo_postal']
            calificacion = form.cleaned_data['calificacion']
            puntuacion = form.cleaned_data['puntuacion']
            restaurantes = buscarEnBD(id_restaurante, nombre, barrio, cocina, calle, cp, calificacion, puntuacion)

            if restaurantes.count() == 0:
                messages.error(request, 'Su busqueda no ha producido resultados')
                form = BuscarRestaurante()
                
    return render(request, 'buscar_restaurante.html', {'form': form, 'restaurantes': restaurantes})
