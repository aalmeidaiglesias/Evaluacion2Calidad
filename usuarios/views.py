import requests
from django.shortcuts import render


def obtener_usuarios():

    url = "https://randomuser.me/api/"

    parametros = {
        "results": 10,
        "seed": "abc"
    }

    respuesta = requests.get(
        url,
        params=parametros
    )

    if respuesta.status_code == 200:

        datos = respuesta.json()

        return datos["results"]

    return []


def inicio(request):

    usuarios = obtener_usuarios()

    contexto = {
        "usuarios": usuarios
    }

    return render(
        request,
        "usuarios/inicio.html",
        contexto
    )


def detalle(request, posicion):

    usuarios = obtener_usuarios()

    if posicion >= len(usuarios):

        return render(
            request,
            "usuarios/error.html"
        )

    usuario = usuarios[posicion]

    contexto = {
        "usuario": usuario
    }

    return render(
        request,
        "usuarios/detalle.html",
        contexto
    )