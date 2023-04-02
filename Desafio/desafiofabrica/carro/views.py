from django.shortcuts import render
from rest_framework import viewsets
from .models import Usuario, CarroUso
from .serializers import UsuarioSerializer, CarroUsoSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class CarroUsoViwSet(viewsets.ModelViewSet):
    queryset = CarroUso.objects.all()
    serializer_class = CarroUsoSerializer






