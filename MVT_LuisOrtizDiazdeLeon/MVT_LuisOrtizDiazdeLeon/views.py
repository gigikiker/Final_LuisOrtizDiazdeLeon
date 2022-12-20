from django.http import HttpResponse
from django.template import Context, Template

#PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
#TEMPLATES_PATH = os.path.join(PROJECT_PATH, 'templates/')

def saludo(request):   #Nuestra primera vista :) 
	return HttpResponse("Bienvenidos al proyecto del dia 22 de Noviembre")


def probandoTemplate(self):
    nom = "Luis"
    ape = "Ortiz Diaz de Leon"

    diccionario = {
        'nombre' :nom,
        'apellido':ape,
    }

    miHtml = open("C:/Users/luizi/Documents/Curso Python/Clase 19/MVT_LuisOrtizDiazdeLeon/MVT_LuisOrtizDiazdeLeon/Templates/Template.html")
    #miHtml = open(TEMPLATES_PATH+"/template1.html")

    plantilla = Template(miHtml.read()) #Se carga en memoria nuestro documento, template1   
    ##OJO importar template y contex, con: from django.template import Template, Context

    miHtml.close() #Cerramos el archivo

    miContexto = Context(diccionario) #EN este caso no hay nada ya que no hay parametros, IGUAL hay que crearlo
    
    documento = plantilla.render(miContexto) #Aca renderizamos la plantilla en documento

    return HttpResponse(documento)



def fechas_navidad(self):
    from datetime import date, timedelta
    hoy = date.today()
    
    navidad = date(2022,12,25)
    
    restantes = navidad - hoy
    diccionario = {
        'actual':hoy,
        'christmas':navidad,        
        'navidad':restantes
    }

    miHtml = open("C:/Users/luizi/Documents/Curso Python/Proyecto Final/Final_LuisOrtizDiazdeLeon/MVT_LuisOrtizDiazdeLeon/AppCoder/Templates/AppCoder/Inicio.html")
    #miHtml = open(TEMPLATES_PATH+"/template1.html")

    plantilla = Template(miHtml.read()) #Se carga en memoria nuestro documento, template1   
    ##OJO importar template y contex, con: from django.template import Template, Context

    miHtml.close() #Cerramos el archivo

    miContexto = Context(diccionario) #EN este caso no hay nada ya que no hay parametros, IGUAL hay que crearlo

    documento = plantilla.render(miContexto) #Aca renderizamos la plantilla en documento

    return HttpResponse(documento)