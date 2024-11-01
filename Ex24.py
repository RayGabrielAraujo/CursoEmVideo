#Desafio 24, crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input('Digite o nome de uma cidade: ')).upper()
palavra = 'SANTO'
print(palavra in cidade)
