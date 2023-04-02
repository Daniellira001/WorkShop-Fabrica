#Exercicio Maior Número!
def maiormenor (n1, n2):
    if n1 > n2:
       return n1
    elif n2 > n1:
       return n2
    else:
        print("números iguais!!")

#Exercicio Múltiplo!
def multiplo (n1, n2):
    if n2 % n1 == 0:
        return True
    return False
    
#Exercicio Areaquadrado!
def areaquadrado (n1):
    area = n1**2
    return area 

n1 = int(input('Digite o Primeiro número: '))
n2 = int(input('Digite o Segundo número: '))


print("O maior número é: " + str(maiormenor(n1, n2)))
print(multiplo(n1, n2))

lado = int(input("Digite o lado do quadrado: "))

print(areaquadrado(lado))

