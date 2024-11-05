#Desafio 28, escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário
#tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
num = random.randint(1, 5)

tent = int(input('Tente adivinhar um número de 1 a 5 escolhido pela máquina: '))
if tent == num:
    print('Parabéns você acertou!!')
elif tent > 5:
    print('Seu número foi maior que 5, você errou!!')    
else:
    print('Você errou!! O número escolhido era {} e não {}'.format(num, tent))
