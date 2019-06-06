#Python 3.6

#Classe
def calcula(a,b)
    result = a+b
    return result

#Parse para maiúscula
nome = (input("Insira seu nome:")).upper()
Print (nome)

#If, Else e conversão para int
idade = int(input("Insira sua idade: "))
if idade >= 21 and idade <= 65:
        ingresso = 'Inteira'
else:
    if idade >= 65:
        ingresso = 'Meia idoso'
    else:
        ingresso = 'Meia infantil'

print ("Tipo de ingresso:", ingresso);

#Comparando tipos primitivos
n = input("Insira sua idade:")
if n != int:
    print ("Idade inválida , \"", n,"\" não é uma idade.")
else:
    b = int(n)
    if b > 0:
        print ("Idade válida, você tem", n, "anos")
    else:
        print ("Idade inválida, \"", n, "\" não é uma idade válida")    

#in e float
a = 61
b = 7
print ("Imprimindo valor real:",a/b)
print ("Imprimindo apenas inteiro:",(a//b))
print ("Limitando casa decimal: %.10f",a/b)

#While
n, cont = 100, 0
while cont <= n:
    print (cont)
    cont = cont+1

#For
cont, n =1, 100
for cont in range(n):
    if cont == 1:
        print (cont, "indiozinho")
    else:
        print (cont, "indioszinhos")

#For 
"""
3 valor inicial do for
10 limite onde o for irá acabar
2 contagem de 2 em 2
*contagem positiva ou negativa
"""
n = 10
for i in range (3, 10, 2):
    print(i)

#math
import math

print (math.cos(3))
print (math.tan(2))
print (math.pow(2, 2))

#random
import random

for i in range(10):
    print (random.randrange(1, 7))
"""
1 à 6 o número de opções válidas no random
2 é o número próximo proibido de ser validado
ex: 1, 3, 5, 7, 2, 8
5 é utilizado randint para que o número 5 seja utilizado
"""
for i in range(10):
    print (random.randrange(1, 7, 2))

for i in range(100):
    print (random.randint(1, 5))
