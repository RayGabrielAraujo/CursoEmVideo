#desafio 09, faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
num = int(input('Digite um número para informar sua tabuada: '))

for i in range(11):
    result = num*i
    print('{} x {} = {}'.format(num, i , result))  
    