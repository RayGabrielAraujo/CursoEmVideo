#Desafio 34, escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%
salario = float(input('Digite o seu salário: '))

if salario > 1250:
    aumento = salario * 0.10

elif salario <= 1250:
    aumento = salario * 0.15

print('Seu salário de R$ {:.2f} teve o aumento de R$ {:.2f}, seu novo salário é de R$ {:.2f}'.format(salario, aumento, (salario+aumento)))