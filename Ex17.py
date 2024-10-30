#Desafio 17, faça um programa que leia o comprimento de um cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.
from math import hypot
co = float(input('Digite o valor do Cateto Oposto: '))
ca = float(input('Digite o valor do Cateto Adjacente:'))

hipo = hypot(co, ca)

print('O valor da Hipotenusa é: {:.2f}'.format(hipo))