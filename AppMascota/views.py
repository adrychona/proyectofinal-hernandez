#Archivos propies de django
from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
#Archivos del proyecto
from AppMascota.models import * #from .models import Caninos 
from AppMascota.forms import *

# Create your views here.


#Main view
def inicio(request):
    return render(request,'AppMascota/inicio.html')

#Vista de register/login/logout
def inicio_sesion(request):

    if request.method == "POST": #si el usuario hace click en el botón

        form = AuthenticationForm(request, data = request.POST) #obtener la info, usuario y contraseña

        if form.is_valid():

            info = form.cleaned_data #la informacion que puso el usuario se pasa a diccionario

            usuario = info['username']
            contra = info['password']
            usuario_actual = authenticate(username=usuario,password=contra) #comprobar si el usuario existe

            if usuario_actual is not None: #si el usuario actual es "algo"
                login(request, usuario_actual)#iniciar sesion con ese usuario.
                return render(request, 'AppMascota/inicio.html', {"mensaje": f'Bienvenido {usuario}'})
        #si el usuario no existe, entonces...
        else: #el usuario es none, OJO si el usuario actual es NONE django automaticamente pide que se escriban nuevamente los datos, no es necesario este else 
            return render(request, 'AppMascota/inicio.html', {"mensaje": 'Error, datos de usuario o contraseña incorrectos'})
    else:
        form = AuthenticationForm()
    return render(request,'registro/inicio_sesion.html', {"formu":form})



"""
# CRUD Mascota (VISTAS BASADAS EN FUNCIONES)
# C (Create)
def agregar_mascota(request):
    #Depende de darle click al boton enviar
    if request.method == "POST":
        
        nuevo_formulario = Mascotaformulario(request.POST)        
        
        if nuevo_formulario.is_valid(): #Crear un objeto usando el modelo.
            
            info = nuevo_formulario.cleaned_data #Para tenerlos en modo diccionario.
            
            mascota_nueva = Mascota(nombre=info["nombre"], especie=info["especie"], raza=info["raza"], edad=info["edad"])
            
            mascota_nueva.save()
            return render(request, "AppMascota/confirmacion.html") #muestra la plantilla de inicio
        
    else: #si la persona no ha hecho click en el boton enviar
            
        nuevo_formulario = Mascotaformulario() #mostraremos un formulario vacio

    return render(request,"AppMascota/formulario_mascota.html", {"mi_form":nuevo_formulario}) #Conexion HTML con la vista

# R (Read)
def ver_agregar_mascotas(request):
    mascotas = Mascota.objects.all() #obtener todos las mascotas de la tabla.
    info = {"mascotas":mascotas}
    return render(request,'AppMascota/ver_agregar_mascotas.html', info)
# U (Update)

def actualizar_mascota(request, mascota_nombre):
    #¿que mascota se va a actualizar?
    mascota_selecionada =Mascota.objects.get(nombre=mascota_nombre)#encuentro la mascota que quiero actualizar
    #Ojo, el get solo recibe un valor, si hay dos nombres de mascotas iguales habrá error, se debe refinar este codigo, por ejemplo buscando por id.
    
    #Depende de darle click al boton enviar
    if request.method == "POST":
        
        nuevo_formulario = Mascotaformulario(request.POST)        
        
        if nuevo_formulario.is_valid(): #Crear un objeto usando el modelo.
            
            info = nuevo_formulario.cleaned_data #Para tenerlos en modo diccionario.
            
            #actualizar datos de mascota escogida
            mascota_selecionada.nombre = info["nombre"]
            mascota_selecionada.especie = info["especie"]
            mascota_selecionada.raza = info["raza"]
            mascota_selecionada.edad = info["edad"]

            mascota_selecionada.save()

            return render(request, "AppMascota/confirmacion_actualizacion.html") #muestra la plantilla de inicio
        
    else: #si la persona no ha hecho click en el boton enviar
            
        nuevo_formulario = Mascotaformulario(initial={"nombre":mascota_selecionada.nombre, "especie":mascota_selecionada.especie, "raza":mascota_selecionada.raza,"edad":mascota_selecionada.edad}) #mostraremos un formulario vacio

    return render(request,"AppMascota/update_mascota.html", {"mi_form":nuevo_formulario}) #Conexion HTML con la vista

# D (Delete)
def eliminar_mascota(request, mascota_nombre):
#¿que mascota se va a eliminar?
    mascota_selecionada =Mascota.objects.get(nombre=mascota_nombre)#encuentro la mascota que quiero actualizar
    mascota_selecionada.delete() #Eliminamos serie seleccionada
    return render(request, "AppMascota/confirmacion_eliminada.html") #no es necesario un html para esto por ahora

"""
# CRUD Mascotas (VISTAS BASADAS EN CLASES)
#Create
class Createmascotas(CreateView):
    model = Mascota
    template_name = "AppMascota/mascota_create.html"
    fields = ["nombre", "especie", "raza", "edad"]
    success_url = '/mascota_list/'
  
#Read
class Listamascotas(ListView):
    
    model = Mascota # Con estas dos lineas solamente python va a buscar automaticamente un html que se llame mascota_list.html
    #template_name = "AppMascotas/nombre_personalizado_de_template.html"

#Update
class Actualizarmascotas(UpdateView):
    model = Mascota
    template_name = "AppMascota/mascota_create.html"
    fields = ["nombre", "especie", "raza", "edad"]
    success_url = '/mascota_list/'

#Delete
class Borrarmascotas(DeleteView):
    model = Mascota
    template_name = "AppMascota/mascota_delete.html"
    success_url = '/mascota_list/'


# CRUD Vacunas (VISTAS BASADAS EN CLASES)
#Create
class Createvacunas(CreateView):
    model = Vacuna
    template_name = "AppMascota/vacuna_create.html"
    fields = ["mascota", "vacuna", "fecha"]
    success_url = '/vacuna_list/'

#Read
class Listavacunas(ListView):
    
    model = Vacuna # Con estas dos lineas solamente python va a buscar automaticamente un html que se llame vacuna_list.html
    #template_name = "AppMascotas/nombre_personalizado_de_template.html"

#Update
class Actualizarvacunas(UpdateView):
    model = Vacuna
    template_name = "AppMascota/vacuna_create.html"
    fields = ["mascota", "vacuna", "fecha"]
    success_url = '/vacuna_list/'

#Delete
class Borrarvacunas(DeleteView):
    model = Vacuna
    template_name = "AppMascota/vacuna_delete.html"
    success_url = '/vacuna_list/'

# CRUD Consultas (VISTAS BASADAS EN CLASES)
#Create
class Createconsultas(CreateView):
    model = Consulta
    template_name = "AppMascota/consulta_create.html"
    fields = ["paciente", "fecha", "motivo", "vet", "establecimiento"]
    success_url = '/consulta_list/'
  
#Read
class Listaconsultas(ListView):
    
    model = Consulta # Con estas dos lineas solamente python va a buscar automaticamente un html que se llame mascota_list.html
    #template_name = "AppMascotas/nombre_personalizado_de_template.html"

#Update
class Actualizarconsultas(UpdateView):
    model = Consulta
    template_name = "AppMascota/consulta_create.html"
    fields = ["paciente", "fecha", "motivo", "vet", "establecimiento"]
    success_url = '/consulta_list/'

#Delete
class Borrarconsultas(DeleteView):
    model = Consulta
    template_name = "AppMascota/consulta_delete.html"
    success_url = '/consulta_list/'



"""
# CRUD Vacunas (VISTAS BASADAS EN FUNCIONES)

# C (Create)
def agregar_vacuna(request):
    #Depende de darle click al boton enviar
    if request.method == "POST":
        
        nuevo_formulario = Vacunaformulario(request.POST)        
        
        if nuevo_formulario.is_valid(): #Crear un objeto usando el modelo.
            
            info = nuevo_formulario.cleaned_data #Para tenerlos en modo diccionario.
            
            mascota_nueva = Vacuna(mascota=info["mascota"], vacuna=info["vacuna"], fecha=info["fecha"])
            
            mascota_nueva.save()
            return render(request, "AppMascota/confirmacion.html") #muestra la plantilla de inicio
        
    else: #si la persona no ha hecho click en el boton enviar
            
        nuevo_formulario = Vacunaformulario() #mostraremos un formulario vacio

    return render(request,"AppMascota/formulario_vacuna.html", {"mi_form":nuevo_formulario}) #Conexion HTML con la vista

# R (Read)
def ver_agregar_vacunas(request):
    vacunas = Vacuna.objects.all() #obtener todos las mascotas de la tabla.
    info = {"vacunas":vacunas}
    return render(request,'AppMascota/ver_agregar_vacunas.html', info)
# U (Update)

# D (Delete)
"""


"""
# CRUD Consultas (VISTAS BASADAS EN FUNCIONES)
# C (Create)
def agregar_consulta(request):
    #Depende de darle click al boton enviar
    if request.method == "POST":
        
        nuevo_formulario = Consultaformulario(request.POST)        
        
        if nuevo_formulario.is_valid(): #Crear un objeto usando el modelo.
            
            info = nuevo_formulario.cleaned_data #Para tenerlos en modo diccionario.
            
            mascota_nueva = Consulta(paciente=info["paciente"], fecha=info["fecha"], motivo=info["motivo"], vet=info["vet"], establecimiento=info["establecimiento"] )
            
            mascota_nueva.save()
            return render(request, "AppMascota/confirmacion.html") #muestra la plantilla de inicio
        
    else: #si la persona no ha hecho click en el boton enviar
            
        nuevo_formulario = Consultaformulario() #mostraremos un formulario vacio

    return render(request,"AppMascota/formulario_consulta.html", {"mi_form":nuevo_formulario}) #Conexion HTML con la vista

# R (Read)
def ver_agregar_consultas(request):
    consultas = Consulta.objects.all() #obtener todos las mascotas de la tabla.
    info = {"consultas":consultas}
    return render(request,'AppMascota/ver_agregar_consultas.html', info)
# U (Update)

# D (Delete)
"""


# Otras VISTAS BASADAS EN FUNCIONES

""" 
#No muestran boton para ir a crear mascota desde vista de mascotas.

def agregar_mascota(request):
    #Depende de darle click al boton enviar
    if request.method == "POST":
        
        nuevo_formulario = Mascotaformulario(request.POST)        
        
        if nuevo_formulario.is_valid(): #Crear un objeto usando el modelo.
            
            info = nuevo_formulario.cleaned_data #Para tenerlos en modo diccionario.
            
            mascota_nueva = Mascota(nombre=info["nombre"], especie=info["especie"], raza=info["raza"], edad=info["edad"])
            
            mascota_nueva.save()
            return render(request, "AppMascota/confirmacion.html") #muestra la plantilla de inicio
        
    else: #si la persona no ha hecho click en el boton enviar
            
        nuevo_formulario = Mascotaformulario() #mostraremos un formulario vacio

    return render(request,"AppMascota/formmascota.html", {"mi_form":nuevo_formulario}) #Conexion HTML con la vista

"""

"""
#No muestran boton para ir a crear vacunas desde vista de vacunas.

def agregar_vacuna(request):
    #Depende de darle click al boton enviar
    if request.method == "POST":
        
        nuevo_formulario = Vacunaformulario(request.POST)        
        
        if nuevo_formulario.is_valid(): #Crear un objeto usando el modelo.
            
            info = nuevo_formulario.cleaned_data #Para tenerlos en modo diccionario.
            
            mascota_nueva = Vacuna(mascota=info["mascota"], vacuna=info["vacuna"], fecha=info["fecha"])
            
            mascota_nueva.save()
            return render(request, "AppMascota/confirmacion.html") #muestra la plantilla de inicio
        
    else: #si la persona no ha hecho click en el boton enviar
            
        nuevo_formulario = Vacunaformulario() #mostraremos un formulario vacio

    return render(request,"AppMascota/formvacuna.html", {"mi_form":nuevo_formulario}) #Conexion HTML con la vista

"""
"""
#No muestran boton para ir a crear consultas desde vista de consultas.

def agregar_consulta(request):
    #Depende de darle click al boton enviar
    if request.method == "POST":
        
        nuevo_formulario = Consultaformulario(request.POST)        
        
        if nuevo_formulario.is_valid(): #Crear un objeto usando el modelo.
            
            info = nuevo_formulario.cleaned_data #Para tenerlos en modo diccionario.
            
            mascota_nueva = Consulta(paciente=info["paciente"], fecha=info["fecha"], motivo=info["motivo"], vet=info["vet"], establecimiento=info["establecimiento"] )
            
            mascota_nueva.save()
            return render(request, "AppMascota/confirmacion.html") #muestra la plantilla de inicio
        
    else: #si la persona no ha hecho click en el boton enviar
            
        nuevo_formulario = Consultaformulario() #mostraremos un formulario vacio

    return render(request,"AppMascota/formconsulta.html", {"mi_form":nuevo_formulario}) #Conexion HTML con la vista
"""

#Busqueda personalizada / filtrando elementos.
def buscar(request):
    
    return render(request,"AppMascota/buscar.html")

def resultado_vacuna(request):
    #return HttpResponse(f"Estoy buscando los perros de la especie {request.GET['especie']}")
    if request.method == "GET":
        
        mascotas = request.GET['mascota']
        vacunas = Vacuna.objects.filter(mascota__icontains=mascotas)
        
        return render(request,"AppMascota/resultado_vacunas.html", { "vacunas": vacunas, "mascotas": mascotas})
   
    else: #si aun no le hacer click al boton BUSCAR
        respuesta = "No enviaste datos"

    #return HttpResponse(f'Estas buscando las mascotas por la especie {request.GET["especie"]} ')
    return HttpResponse(respuesta)

def resultado_especie(request):
    #return HttpResponse(f"Estoy buscando los perros de la especie {request.GET['especie']}")
    if request.method == "GET":
        
        especies = request.GET['especie']
        mascotas = Mascota.objects.filter(especie__icontains=especies)
        
        return render(request,"AppMascota/resultado_especies.html", { "mascotas": mascotas, "especies": especies})
   
    else: #si aun no le hacer click al boton BUSCAR
        respuesta = "No enviaste datos"

    #return HttpResponse(f'Estas buscando las mascotas por la especie {request.GET["especie"]} ')
    return HttpResponse(respuesta)



