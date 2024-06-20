from django.urls import path
from autores import views
from .views import AutorListView, LibroListView, home

urlpatterns = [
    path('', home, name='home'),
    path('index_autores/', AutorListView.as_view(), name='autor_list'),
    path('autores_rest/', views.autores_rest, name='autores_rest'),
    path('index_libros/', LibroListView.as_view(), name='index_libros'),
    path('libros_rest/', views.libros_rest, name='libros_rest'),
    path('new_autor/', views.NewAutorView.as_view(), name='new_autor'),
    path('new_libro/', views.NewLibroView.as_view(), name='new_libro'),
]