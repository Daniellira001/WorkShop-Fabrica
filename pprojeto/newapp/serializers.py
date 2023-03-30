from rest_framework import serializers
from newapp.models import newprojeto

class newprojetoSerializers (serializers.ModelSerializer):

    class Meta: 
        model = newprojeto
        fields = ['id', 'atividade', 'status']
