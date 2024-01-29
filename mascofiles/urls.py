"""
URL configuration for mascofiles project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppMascota.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('login/', inicio_sesion, name='login' ),
    path('about/', inicio_sesion, name='about' ),
    #_VISTAS BASADAS EN FUNCIONES_

    # URLs para crear nuevos datos usando formularios django
    #path("formmascota/", agregar_mascota, name='formumascota'),
    #path("formuvacuna/", agregar_vacuna, name='formuvacuna'),
    #path("formuconsulta/", agregar_consulta, name='formuconsulta'),
    # URLs para buscar datos
    path("buscar/", buscar, name='busqueda'),
    path("resultado_especies/", resultado_especie, name='resultado_especie'),
    path("resultado_vacunas/", resultado_vacuna, name='resultado_vacuna'),
    # URLs para agrregar y ver datos
    #path("ver_agregar_mascotas/",ver_agregar_mascotas, name ='ver_agregar_mascota'),
    #path("ver_agregar_vacunas/",ver_agregar_vacunas, name ='ver_agregar_vacuna'),
    #path("ver_agregar_consultas/",ver_agregar_consultas, name ='ver_agregar_consulta'),
    # URLs para crear nuevos datos usando formularios django (mejorado)
    #path("formulario_mascota/", agregar_mascota, name='formulario_mascota'),
    #path("formulario_vacuna/", agregar_vacuna, name='formulario vacuna'),
    #path("formulario_consulta/", agregar_consulta, name='formulario consulta'),
    # URLs para actualizar datos
    #path("update_mascota/<mascota_nombre>", actualizar_mascota, name='actualizar mascota'),
    # URLs para eliminar datos
    #path("eliminar_mascota/<mascota_nombre>", eliminar_mascota, name='eliminar mascota'),
    
    #_VISTAS BASADAS EN CLAES_
    path("vacuna_list/", Listavacunas.as_view(), name = 'lista_vacunas'),
    path("vacuna_detail/<int:pk>", Detallevacunas.as_view(), name = 'vacuna_detail'),
    path("vacuna_create/", Createvacunas.as_view(), name = 'crear_vacuna'),
    path("vacuna_update/<int:pk>", Actualizarvacunas.as_view(), name = 'actualizar_vacuna'),
    path("vacuna_confirm_delete/<int:pk>", Borrarvacunas.as_view(), name = 'eliminar_vacuna'),
    
    path("mascota_list/", Listamascotas.as_view(), name = 'lista_mascotas'),
    path("mascota_detail/<int:pk>", Detallemascotas.as_view(), name = 'mascota_detail'),
    path("mascota_create/", Createmascotas.as_view(), name = 'crear_mascota'),
    path("mascota_update/<int:pk>", Actualizarmascotas.as_view(), name = 'actualizar_mascota'),
    path("mascota_confirm_delete/<int:pk>", Borrarmascotas.as_view(), name = 'eliminar_mascota'),

    path("consulta_list/", Listaconsultas.as_view(), name = 'lista_consultas'),
    path("consulta_detail/<int:pk>", Detalleconsultas.as_view(), name = 'consulta_detail'),
    path("consulta_create/", Createconsultas.as_view(), name = 'crear_consulta'),
    path("consulta_update/<int:pk>", Actualizarconsultas.as_view(), name = 'actualizar_consulta'),
    path("consulta_confirm_delete/<int:pk>", Borrarconsultas.as_view(), name = 'eliminar_consulta'),
    ] 