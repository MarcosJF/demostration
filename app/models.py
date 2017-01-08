from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from pymongo import MongoClient
from datetime import datetime

client = MongoClient('mongodb://localhost:27017/')
db = client.test

#Metodo para insertar un nuevo restaurante en la BD de MongoDB. Recibe los datos desde views.py
def insertarEnBD(id_restaurante, nombre, edificio, calle, cp, barrio, cocina, calificacion, puntuacion):
    result = db.restaurants.insert_one(
    {
        "address": {
            "street": calle,
            "zipcode": cp,
            "building": edificio,
            "coord": [-73.9557413, 40.7720266]
        },
        "borough": barrio,
        "cuisine": cocina,
        "grades": [
            {
                "date": datetime.strptime("2014-10-01", "%Y-%m-%d"),
                "grade": calificacion,
                "score": puntuacion
            }
        ],
        "name": nombre,
        "restaurant_id": id_restaurante
    }
)

#Metodo para modificar un restaurante en la base de datos
def actualizarEnBD(id_r, edificio_r, calle_r, cp_r, barrio_r, cocina_r):
    db.restaurants.update(
        { "restaurant_id" : id_r },
        {
            '$set': { 'address.building' : edificio_r,
                      'address.street' : calle_r ,
                      'address.zipcode' : cp_r,
                      'borough' : barrio_r,
                      'cuisine' : cocina_r
            }
        }
    )

    return 0

#Metodo para buscar un restaurante en la base de datos
def buscarEnBD(id_restaurante, nombre_restaurante, barrio_restaurante, cocina_restaurante, calle_restaurante, codigoPostal_restaurante, calificacion_restaurante, puntuacion_restaurante):
    restaurantes = []
    tam_query = None
    query = None

    if id_restaurante:
        if not query:
            query = [{ 'restaurant_id' : id_restaurante }]

    if nombre_restaurante:
        if not query:
            query = [{ 'name' : nombre_restaurante }]
        else:
            query.append({ 'name' : nombre_restaurante })

    if barrio_restaurante:
        if not query:
            query = [{ 'borough' : barrio_restaurante }]
        else:
            query.append({ 'borough' : barrio_restaurante })

    if cocina_restaurante:
        if not query:
            query = [{ 'cuisine' : cocina_restaurante }]
        else:
            query.append({ 'cuisine' : cocina_restaurante })

    if calle_restaurante:
        if not query:
            query = [{ 'address.street' : calle_restaurante }]
        else:
            query.append({ 'address.street' : calle_restaurante })

    if codigoPostal_restaurante:
        if not query:
            query = [{ 'address.zipcode' : codigoPostal_restaurante }]
        else:
            query.append({ 'address.zipcode' : codigoPostal_restaurante })

    if calificacion_restaurante:
        if not query:
            query = [{ 'grades.grade' : calificacion_restaurante }]
        else:
            query.append({ 'grades.grade' : calificacion_restaurante })

    if puntuacion_restaurante:
        if not query:
            query = [{ 'grades.score' : int(puntuacion_restaurante) }]
        else:
            query.append({ 'grades.score' : int(puntuacion_restaurante) })

    if not query:
        query = [{}]

    print "HOLA ANTES DE CONSULTA"
    restaurantes = db.restaurants.find({'$and': query})
    print "HOLA DESPUES DE CONSULTA"
    print restaurantes.count()
    #for field in restaurantes:
    #    print(field)

    tam_query = db.restaurants.count({'$and': query})

    return restaurantes
