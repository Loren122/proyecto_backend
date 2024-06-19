from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import ListView, CreateView
# from django.db.models import Count

from autores.models import Autor, Libro
from autores.serializers import AutorSerializer, LibroSerializer
from autores.forms import AutorForm, LibroForm

# Create your views here.

def get_all_autores():
    autores = Autor.objects.all().order_by('name')
    autores_serializers = AutorSerializer(autores, many=True)
    return autores_serializers.data

def autores_rest(request):
    autores = get_all_autores()
    return JsonResponse(autores, safe=False)

def get_all_libros():
    libros = Libro.objects.all().order_by('titulo')
    libros_serializers = LibroSerializer(libros, many=True)
    return libros_serializers.data

def libros_rest(request):
    libros = get_all_libros()
    return JsonResponse(libros, safe=False)

def index_autores(request):
    autores = get_all_autores()
    return render(request, 'index_autores.html', {'autores': autores})

def index_libros(request):
    libros = get_all_libros()
    return render(request, 'index.libros', {'libros': libros})

class AutorListView(ListView):
    model = Autor
    template_name = 'autor_list.html'  # Nombre del nuevo template
    context_object_name = 'autores'

    def get_queryset(self):
        return Autor.objects.prefetch_related('libros')
    
def add_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('autores:index_autores')  # Ajusta esto a la vista que muestra la lista de autores
    else:
        form = AutorForm()
    return render(request, 'autores/form_autor.html', {'form': form})    

class NewAutorView(CreateView):
    form_class = AutorForm
    template_name = 'form_autor.html'
    success_url = '/index_autores/'


class NewLibroView(CreateView):
    form_class = LibroForm
    template_name = 'form_autor.html'
    success_url = '/'