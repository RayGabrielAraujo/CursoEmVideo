#desafio 07, desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.
nota1 = float(input('Escreva a primeira nota do aluno: '))
nota2 = float(input('Escreva a segunda nota do aluno: '))

print('A média desse aluno é {:.1f}'.format((nota1 + nota2)/2))