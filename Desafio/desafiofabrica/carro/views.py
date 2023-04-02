from django.shortcuts import render
from rest_framework import generics
from .models import Usuario, CarroUso
from .serializers import UsuarioSerializer, CarroUsoSerializer


class UsuarioViewSet(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class Usuariodelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class CarroUsoViwSet(generics.ListCreateAPIView):
    queryset = CarroUso.objects.all()
    serializer_class = CarroUsoSerializer

class CarroUsodelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarroUso.objects.all()
    serializer_class = CarroUsoSerializer






