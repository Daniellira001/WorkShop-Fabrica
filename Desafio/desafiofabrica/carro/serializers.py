from rest_framework import serializers
from .models import Usuario, CarroUso

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'endereco', 'idade']

class CarroUsoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarroUso
        fields = ['id', 'modelo', 'marca', 'anodocarro']
        

    