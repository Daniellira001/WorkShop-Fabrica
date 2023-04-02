from django.shortcuts import render

from newapp.models import newprojeto
from newapp.serializers import newprojetoSerializers

from django.urls import path, include 
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

class newprojetoViewSet(viewsets.ModelViewSet):
    queryset = newprojeto.objects.all()
    serializer_class = newprojetoSerializers
