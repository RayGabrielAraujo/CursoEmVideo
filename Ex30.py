#Desafio 30, crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
num = int(input('Digite um número qualquer: '))

result = num % 2
if result == 0:
    print('o número {} é par'.format(num))
else: 
    print('O número {} é impar'.format(num))