#desafio 08, escreva um programa que leia um valor em metros e o exiba convertendo em centímetros e milímetros.
num = float(input('Escreva um valor em metros: '))

print('Valor em Metros: {} \nValor em Centimetos: {:.0f} \nValor em Milímetros: {:.0f}'.format(num, (num * 100) , (num * 1000)))