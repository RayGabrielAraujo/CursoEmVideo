#Desafio 16, crie um programa que leia um número qualquer pelo teclado e mostre na tela a sua porção inteira.
from math import trunc

num = float(input('Digite um número para calcular sua porção inteira: '))
print('A porção inteira do número {} é {}.'.format(num,trunc(num)))