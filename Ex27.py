#Desafio 27, faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('Digite seu nome completo: ')).split()
print('Seu primeiro nome é {} e seu último nome é {}'.format(nome[0], nome[-1]))