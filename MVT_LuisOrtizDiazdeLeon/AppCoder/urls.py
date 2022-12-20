from django.urls import path
from AppCoder import views

urlpatterns = [
    path("", views.Inicio,name='Inicio'),
    path("Cursos/", views.Cursos,name='Cursos'),
    path("Busquedacursos/", views.buscarcursos,name='Buscar'), #clase 22
    path("Buscar/", views.Buscar), #clase 22
    path("Busquedaentrenadores/", views.buscarentrenadores,name='BuscarE'), #clase 22
    path("BuscarE/", views.BuscarE), #clase 22
    path("Busquedapokemon/", views.buscarpokemon,name='BuscarP'), #clase 22
    path("BuscarP/", views.BuscarP), #clase 22
    path("CursosApi/", views.Cursosapi),
    path("EntrenadoresApi/",views.Entrenadoresapi),
    path("PokemonApi/",views.Pokemonapi),
    path("Entrenadores/", views.FEntrenadores,name='Entrenadores'),
    path("Pokemon/", views.FPokemon,name='Pokemon'),
    path("leercursos/", views.leer_cursos), #clase 23
    path("crearcurso/", views.crear_cursos),
    path("editarcurso/", views.editar_cursos),
    path("eliminarcurso/", views.eliminar_cursos),
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