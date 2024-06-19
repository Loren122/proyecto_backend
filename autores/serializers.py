from rest_framework import serializers

from autores.models import Autor, Libro


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        # fields = ['name', 'number', 'collection', 'is_backlight']
        fields = '__all__'
        
class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        # fields = ['name', 'number', 'collection', 'is_backlight']
        fields = '__all__'