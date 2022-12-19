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

#def Buscar(request):
#    cursos_views = request.GET['indicador']
#    cursos_todos = Curso.objects.filter(indicador=cursos_views)
#    return HttpResponse(f'Estoy buscando el ID: {cursos_views} que corresponde al curso {cursos_todos}') #clase 22

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
    #return render(request,'AppCoder/inicio.html')

def Cursos(request):
    if request.method == "POST":

        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            #curso = Curso**[Modelo]**(nombre**[Modelo]**=informacion["nombre_del_curso"]**[form]**,indicador**[Modelo]**=informacion["numero_identificador"]**[Form]**)
            curso = Curso(nombre=informacion["nombre_del_curso"],indicador=informacion["numero_identificador"])
            curso.save()
            return Inicio(request)
    else:
        miFormulario = CursoFormulario()

    return render(request, "AppCoder/Cursos.html", {"miFormulario":miFormulario})


def FEntrenadores(request):
    if request.method == "POST":

        miFormulario = EntrenadoresFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            #curso = Curso**[Modelo]**(nombre**[Modelo]**=informacion["nombre_del_curso"]**[form]**,indicador**[Modelo]**=informacion["numero_identificador"]**[Form]**)
            entrenador = Entrenadores(nombre=informacion["nombre_del_entrenador"],apellido=informacion["apellido_del_entrenador"],email=informacion["email"],badge=informacion["id_de_entrandor"],indicador=informacion["curso"])
            entrenador.save()
            return Inicio(request)
    else:
        miFormulario = EntrenadoresFormulario()

    return render(request, "AppCoder/Entrenadores.html", {"miFormulario":miFormulario})

def FPokemon(request):
    if request.method == "POST":

        miFormulario = PokemonFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            #curso = Curso**[Modelo]**(nombre**[Modelo]**=informacion["nombre_del_curso"]**[form]**,indicador**[Modelo]**=informacion["numero_identificador"]**[Form]**)
            pokemon = Pokemon(nombre=informacion["nombre_del_pokemon"],tipo=informacion["tipo"],sexo=informacion["sexo"],badge=informacion["badge_del_entrenador"],fecha_de_captura=informacion["fecha_de_captura"],en_equipo=informacion["actualmente_en_equipo"])
            pokemon.save()
            return Inicio(request)
    else:
        miFormulario = PokemonFormulario()

    return render(request, "AppCoder/Pokemon.html", {"miFormulario":miFormulario}) 

def Cursosapi(request):
    cursos_todos= Curso.objects.all()
    return HttpResponse(serializers.serialize('json',cursos_todos)) 

def Entrenadoresapi(request):
    entrenadores_todos= Entrenadores.objects.all()
    return HttpResponse(serializers.serialize('json',entrenadores_todos)) 

def Pokemonapi(request):
    pokemon_todos= Pokemon.objects.all()
    return HttpResponse(serializers.serialize('json',pokemon_todos)) 