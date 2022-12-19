from django import forms
from datetime import date

class CursoFormulario(forms.Form):
    nombre_del_curso=forms.CharField(max_length=40)
    numero_identificador=forms.IntegerField()

class EntrenadoresFormulario(forms.Form):
    nombre_del_entrenador=forms.CharField(max_length=40)
    apellido_del_entrenador=forms.CharField(max_length=40)
    email=forms.EmailField()
    id_de_entrandor=forms.IntegerField()
    curso=forms.IntegerField()

class PokemonFormulario(forms.Form):
    nombre_del_pokemon=forms.CharField(max_length=40)
    tipo=forms.CharField(max_length=40)
    sexo=forms.CharField(initial="Macho / Hembra",max_length=40)
    badge_del_entrenador=forms.IntegerField()
    fecha_de_captura=forms.DateField(initial="AAAA-MM-DD")
    actualmente_en_equipo=forms.BooleanField()