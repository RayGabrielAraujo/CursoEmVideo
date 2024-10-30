#desafio 11, faça um programa que leia a largura e altura de uma parede em metros , calcule a sua área e a quantidade de tinta
#necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
largura = int(input('Diga a largura: ' ))
altura = int(input('Digite a altura: '))

area = int(largura * altura)
tinta = int(area / 2)

print('Será necessário {} litros de tinta para pintar uma parede de {}²'.format(tinta, area))