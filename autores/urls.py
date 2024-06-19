from django.urls import path
from autores import views
from .views import AutorListView

urlpatterns = [
    path('index_autores/', AutorListView.as_view(), name='autor-list'),
    path('autores_rest/', views.autores_rest, name='autores_rest'),
    path('libros_rest/', views.libros_rest, name='libros_rest'),
    path('new_autor/', views.NewAutorView.as_view(), name='new_autor'),
    path('new_libro/', views.NewLibroView.as_view(), name='new_libro'),
    path('add_autor/', views.add_autor, name='add_autor'),
]