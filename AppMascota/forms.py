from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Mascotaformulario(forms.Form):
   
    nombre = forms.CharField(max_length=40)
    especie = forms.CharField(max_length=40)
    raza = forms.CharField(max_length=40)
    edad = forms.IntegerField()


class Vacunaformulario(forms.Form):
    
    mascota = forms.CharField(max_length=40)
    vacuna = forms.CharField(max_length=40)
    fecha = forms.DateField()
    


class Consultaformulario(forms.Form):
    
    paciente = forms.CharField(max_length=40)
    fecha = forms.DateField()
    motivo = forms.CharField(max_length=100)
    vet = forms.CharField(max_length=40)
    establecimiento = forms.CharField(max_length=100)
   


class RegistrarUsuario(UserCreationForm):
    username = forms.CharField(label= "Ingrese un nombre de usuario", help_text="Evite utilizar espacios") 
    email = forms.EmailField(label= "Correo electronico") 
    #password1 = forms.PasswordInput() Este modelo agrega nuevamente el registro or default de django
    #password2 = forms.PasswordInput()
    password1 = forms.CharField(label= "Ingrese la contraseña", widget= forms.PasswordInput) 
    password2 = forms.CharField(label= "Confirme la contraseña", widget= forms.PasswordInput)
    first_name = forms.CharField(label= "Nombre")
    last_name = forms.CharField(label= "Apellido")


    class Meta:
        model = User
        #["username", "email", "password1", "password2", "first_name", "last_name"] campos django por defecto
        fields = ["username", "email", "password1", "password2", "first_name", "last_name"]

class EditarUsuario(UserCreationForm):
    
    email = forms.EmailField(label= "Correo electronico")
    password1 = forms.CharField(label= "Ingrese la contraseña", widget= forms.PasswordInput) 
    password2 = forms.CharField(label= "Confirme la contraseña", widget= forms.PasswordInput)
    avatar = forms.ImageField(label= "Foto")
    
    class Meta:
        model = User
        fields = ["email","password1", "password2", "avatar"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']