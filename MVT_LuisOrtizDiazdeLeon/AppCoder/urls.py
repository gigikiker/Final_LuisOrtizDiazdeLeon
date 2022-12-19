from django.urls import path
from AppCoder import views

urlpatterns = [
    path("", views.Inicio,name='Inicio'),
    path("Cursos/", views.Cursos,name='Cursos'),
    path("Busquedacursos/", views.buscarcursos), #clase 22
    path("Buscar/", views.Buscar), #clase 22
    path("Busquedaentrenadores/", views.buscarentrenadores), #clase 22
    path("BuscarE/", views.BuscarE), #clase 22
    path("Busquedapokemon/", views.buscarpokemon), #clase 22
    path("BuscarP/", views.BuscarP), #clase 22
    path("CursosApi/", views.Cursosapi),
    path("EntrenadoresApi/",views.Entrenadoresapi),
    path("PokemonApi/",views.Pokemonapi),
    path("Entrenadores/", views.FEntrenadores,name='Entrenadores'),
    path("Pokemon/", views.FPokemon,name='Pokemon'),
]