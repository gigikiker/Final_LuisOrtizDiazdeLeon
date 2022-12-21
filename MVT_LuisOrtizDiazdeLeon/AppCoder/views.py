from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template
# Create your views here.
from datetime import date, timedelta
from AppCoder.models import Curso, Entrenadores, Pokemon
from django.core import serializers
from AppCoder.forms import CursoFormulario, EntrenadoresFormulario, PokemonFormulario

def buscarcursos(request):
    return render(request,"AppCoder/busquedacursos.html") #clase 22

def Buscar(request):
    cursos_views = request.GET['indicador']
    cursos_todos = Curso.objects.filter(indicador=cursos_views)
    entrenadores_todos = Entrenadores.objects.filter(indicador=cursos_views)
    return render(request, "AppCoder/resultadocursos.html",{"indicador":cursos_views,"cursos":cursos_todos,"entrenadores":entrenadores_todos})

def buscarentrenadores(request):
    return render(request,"AppCoder/busquedaentrenadores.html") #clase 22

def BuscarE(request):
    entrenadores_views = request.GET['badge']
    cursos_todos = Curso.objects.filter(indicador=entrenadores_views)
    entrenadores_todos = Entrenadores.objects.filter(badge=entrenadores_views)
    pokemon_todos = Pokemon.objects.filter(badge=entrenadores_views)
    return render(request, "AppCoder/resultadoentrenadores.html",{"badge":entrenadores_views,"cursos":cursos_todos,"entrenadores":entrenadores_todos, "pokemon":pokemon_todos})

def buscarpokemon(request):
    return render(request,"AppCoder/busquedapokemon.html") #clase 22

def BuscarP(request):
    pokemon_views = request.GET['nombre']
    pokemon_todos = Pokemon.objects.filter(nombre=pokemon_views)
    return render(request, "AppCoder/resultadopokemon.html",{"nombre":pokemon_views,"pokemon":pokemon_todos})

def Inicio(self):
    hoy = date.today()
    
    navidad = date(2022,12,25)
    
    restantes = navidad - hoy
    
    diccionario = {
        'actual':hoy,
        'christmas':navidad,        
        'navidad':restantes
    }

    miHtml = open("C:/Users/luizi/Documents/Curso Python/Clase 19/MVT_LuisOrtizDiazdeLeon/AppCoder/Templates/AppCoder/Inicio.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context(diccionario) 
    documento = plantilla.render(miContexto) 

    return HttpResponse(documento)

def Cursosapi(request):
    cursos_todos= Curso.objects.all()
    return HttpResponse(serializers.serialize('json',cursos_todos)) 

def Entrenadoresapi(request):
    entrenadores_todos= Entrenadores.objects.all()
    return HttpResponse(serializers.serialize('json',entrenadores_todos)) 

def Pokemonapi(request):
    pokemon_todos= Pokemon.objects.all()
    return HttpResponse(serializers.serialize('json',pokemon_todos)) 



from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

class CursoList(ListView):
    model = Curso
    template = 'AppCoder/curso_list.html'

class CursoCreate(CreateView):
    model = Curso
    fields = '__all__'
    success_url = '/AppCoder/curso/list/'

class EntrenadoresList(ListView):
    model = Entrenadores
    template = 'AppCoder/entrenadores_list.html'

class EntrenadoresCreate(CreateView):
    model = Entrenadores
    fields = '__all__'
    success_url = '/AppCoder/entrenadores/list/'

class PokemonList(ListView):
    model = Pokemon
    template = 'AppCoder/pokemon_list.html'

class PokemonCreate(CreateView):
    model = Pokemon
    fields = '__all__'
    success_url = '/AppCoder/pokemon/list/'

#Update View Clase 24

class CursoEdit(UpdateView):
    model = Curso
    fields = '__all__'
    success_url = '/AppCoder/curso/list/'

class EntrenadoresEdit(UpdateView):
    model = Entrenadores
    fields = '__all__'
    success_url = '/AppCoder/entrenadores/list/'

class PokemonEdit(UpdateView):
    model = Pokemon
    fields = '__all__'
    success_url = '/AppCoder/pokemon/list/'


#Detalle

from django.views.generic.detail import DetailView

class CursoDetail(DetailView):
    model = Curso
    template = 'AppCoder/curso_detail.html'

class EntrenadoresDetail(DetailView):
    model = Entrenadores
    template = 'AppCoder/entrenadores_detail.html'

class PokemonDetail(DetailView):
    model = Pokemon
    template = 'AppCoder/pokemon_detail.html'


#Borrar

class CursoDelete(DeleteView):
    model = Curso
    success_url = '/AppCoder/curso/list/'

class EntrenadoresDelete(DeleteView):
    model = Entrenadores
    success_url = '/AppCoder/entrenadores/list/'

class PokemonDelete(DeleteView):
    model = Pokemon
    success_url = '/AppCoder/pokemon/list/'


#Pagina de Busqueda para 3 opciones

def paginabusquedas(request):
    return render(request,"AppCoder/paginabusquedas.html") 


#Pagina de cada modelo con 2 opciones y un Home

def paginacursos(request):
    return render(request,"AppCoder/Cursos.html") 

def paginaentrenadores(request):
    return render(request,"AppCoder/Entrenadores.html") 

def paginapokemon(request):
    return render(request,"AppCoder/Pokemon.html") 