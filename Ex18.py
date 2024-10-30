#Desafio 18, faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

an = float(input('Digite um ângulo qualquer: '))

sen = math.sin(math.radians(an))
cos = math.acos(math.radians(an))
tan = math.tan(math.radians(an))

print('Com o ângulo de {} seu Seno é de {:.2f}'.format(an, sen))
print('Com o ângulo de {} seu Cosseno é de {:.2f}'.format(an,cos))
print('Com o ângulo de {} sua Tangente é de {:.2f}'.format(an,tan))