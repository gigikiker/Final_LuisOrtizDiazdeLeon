from django.urls import path
from AppCoder import views

urlpatterns = [
    path("", views.Inicio,name='Inicio'),
    path("Cursos/", views.paginacursos,name='Cursos'),
    path("Busquedacursos/", views.buscarcursos,name='Buscar'), 
    path("Buscar/", views.Buscar), 
    path("Busquedaentrenadores/", views.buscarentrenadores,name='BuscarE'), 
    path("BuscarE/", views.BuscarE),
    path("Busquedapokemon/", views.buscarpokemon,name='BuscarP'),
    path("BuscarP/", views.BuscarP), 
    path("CursosApi/", views.Cursosapi),
    path("EntrenadoresApi/",views.Entrenadoresapi),
    path("PokemonApi/",views.Pokemonapi),
    path("Entrenadores/", views.paginaentrenadores,name='Entrenadores'),
    path("Pokemon/", views.paginapokemon,name='Pokemon'),
    path("curso/list/", views.CursoList.as_view(),name='ListC'),
    path("curso/create/", views.CursoCreate.as_view(),name='NewC'),
    path("entrenadores/list/", views.EntrenadoresList.as_view(),name='ListE'),
    path("entrenadores/create/", views.EntrenadoresCreate.as_view(),name='NewE'),
    path("pokemon/list/", views.PokemonList.as_view(),name='ListP'),
    path("pokemon/create/", views.PokemonCreate.as_view(),name='NewP'),
    path("curso/edit/<pk>", views.CursoEdit.as_view(),name='EditC'), #Clase 24
    path("entrenadores/edit/<pk>", views.EntrenadoresEdit.as_view(),name='EditE'),
    path("pokemon/edit/<pk>", views.PokemonEdit.as_view(),name='EditP'),
    path("curso/detail/<pk>", views.CursoDetail.as_view(),name='DetailC'),
    path("entrenadores/detail/<pk>", views.EntrenadoresDetail.as_view(),name='DetailE'),
    path("pokemon/detail/<pk>", views.PokemonDetail.as_view(),name='DetailP'),
    path("curso/delete/<pk>", views.CursoDelete.as_view(),name='DeleteC'),
    path("entrenadores/delete/<pk>", views.EntrenadoresDelete.as_view(),name='DeleteE'),
    path("pokemon/delete/<pk>", views.PokemonDelete.as_view(),name='DeleteP'),
    path("paginabusquedas/", views.paginabusquedas,name='Busquedas'),

]