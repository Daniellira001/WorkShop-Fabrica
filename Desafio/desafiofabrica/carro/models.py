from django.db import models



class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome
    

class CarroUso(models.Model):
    modelo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)  
    anodocarro = models.IntegerField()    

    def __str__(self):
        return self.modelo

    class Meta:
        verbose_name_plural = 'Seu Carro'

