from django.urls import path
from . import views


urlpatterns = [

    path(
        "",
        views.inicio,
        name="inicio"
    ),

    path(
        "detalle/<int:posicion>/",
        views.detalle,
        name="detalle"
    ),

]