#Desafio 25, crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
nome = str(input('Digite seu nome completo: ')).upper()
palavra = 'SILVA'
print(palavra in nome)