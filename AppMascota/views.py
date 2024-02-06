#Archivos propies de django
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from datetime import datetime

#Decorador por defecto
from django.utils.decorators import method_decorator #me permite usar el decorator en class-based view
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
#Archivos del proyecto
from AppMascota.models import * #from .models import Caninos 
from AppMascota.forms import *

# Create your views here.


#Main view
def inicio(request):
    return render(request,'AppMascota/inicio.html')

def about(request):
    return render(request,'About/about.html')

#Vista de register/login/logout/update profile

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

def registro(request):
    
    #formulario = UserCreationForm()
    #return render(request, "registro/registrar_usuario.html", {"formu":formulario})
    
    if request.method == "POST": #Si le doy click a registrarse
        #formulario = UserCreationForm(request.POST) #tengo la informacion 
        formulario = RegistrarUsuario(request.POST) #Uso formulario creado en forms para obtener más datos
       
        if formulario.is_valid(): 
            info = formulario.cleaned_data
            usuario = info["first_name"] #obtener el nombre de usuario con el que se registro
            
            formulario.save() #Ya se crea el usuario
            
            return render(request, "AppMascota/inicio.html", {"mensaje": f"Gracias por registrarte en Mascofiles {usuario}"})       
    else:
        #formulario = UserCreationForm()
        formulario = RegistrarUsuario()

    return render(request, "registro/registrar_usuario.html", {"formu":formulario})


@login_required
def editar_perfil(request):

    #Instancia del login
    user_actual = request.user
     
    #Si es metodo POST ... actualizo
    if request.method == 'POST':
        formulario = EditarUsuario(request.POST, request.FILES)
        u = User.objects.get (username=request.user)


        if formulario.is_valid(): 
            info = formulario.cleaned_data
            user_actual.email = info['email']
            user_actual.password1 = info['password1']
            user_actual.password2 = info['password1']
            user_actual.password2 = info['password1']
            avatar = Avatar(usuario=u,imagen=info["avatar"])
            
            
            avatar.save()
            user_actual.save()
            
            return render(request, "AppMascota/inicio.html")     
    else: 
        formulario= EditarUsuario(initial={ 'email':user_actual.email}) 
        

    return render(request, "registro/editar_usuario.html", {"mi_form":formulario})

################################################################
#Agregar comentario 


def comentar(request):
 #Instancia del login
    user_actual = request.user
    u = User.objects.get (username=request.user)
    #Si es metodo POST ... actualizo
    if request.method == 'POST':
        comentario = CommentForm(request.POST)
        
        if comentario.is_valid(): 
            
            
            info = comentario.cleaned_data
            comentario = Comment(createdby=u,body=info["body"])
            comentario.save() #Ya se crea el usuario
           
            return redirect('foro-list')  #Si ya se guardo el comentario ir a la lista de comentarios
            
    else:   
   
        comentario = CommentForm()

    return render(request, "registro/foro.html", {"formu":comentario}) #mostrar formulario





def ver_comentarios(request):
 
    comentarios = Comment.objects.all() #ver todos los comentarios
    return render(request, "registro/foro-list.html", { "comment":comentarios})





################################################################
# CRUD Mascotas (VISTAS BASADAS EN CLASES)
#Create
 #es un decorador!! --- me permite agregar funcionalidades a mi vista
class Createmascotas(CreateView):
    model = Mascota
    template_name = "AppMascota/mascota_create.html"
    fields = ["nombre", "especie", "raza", "edad"]
    success_url = '/mascota_list/'

#Read
@method_decorator(login_required, name='dispatch')
class Listamascotas(LoginRequiredMixin, ListView):
    
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
    success_url = '/mascota_list/'

#Detail

class Detallemascotas(DetailView):
    model = Mascota



# CRUD Vacunas (VISTAS BASADAS EN CLASES)
#Create

class Createvacunas(CreateView):
    model = Vacuna
    template_name = "AppMascota/vacuna_create.html"
    fields = ["mascota", "vacuna", "fecha"]
    success_url = '/vacuna_list/'

#Read
#Añadir un Mixin
class Listavacunas(LoginRequiredMixin, ListView):
    
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
    success_url = '/vacuna_list/'


class Detallevacunas(DetailView):
    
    model = Vacuna #django sabe el contexto si coloco el nombre del modelo en minuscula


# CRUD Consultas (VISTAS BASADAS EN CLASES)
#Create

class Createconsultas(CreateView):
    model = Consulta
    template_name = "AppMascota/consulta_create.html"
    fields = ["paciente", "fecha", "motivo", "vet", "establecimiento"]
    success_url = '/consulta_list/'
  
#Read

class Listaconsultas(LoginRequiredMixin, ListView):
    
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
    success_url = '/consulta_list/'


class Detalleconsultas(DetailView):
    model = Consulta
    

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



