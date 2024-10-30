#desafio 12, faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Digite o preço do produto: '))

desconto = preco * 0.05
novopreco = preco - desconto

print('O valor com desconto é de {} reais, o valor novo é de {} reais'.format(desconto, novopreco))