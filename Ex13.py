#desafio 13, faça um algotimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input("Digite o seu salário: "))
aumento = salario * 0.15

novosalario = salario + aumento

print('Você recebeu um aumento de R${:.2f}, seu novo salário é de R${:.2f}'.format(aumento, novosalario))