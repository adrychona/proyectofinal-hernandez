from django import forms

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

