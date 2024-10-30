# desafio 06, crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
num1 = int(input('Escreva um número: '))
triplo = num1 * 3
raiz = num1 ** 0.5

print('O dobro de {} é {}, seu triplo é {}, e sua raiz quadrada é {:.2f}'.format(num1, (num1 * 2), (num1 * 3), (num1 ** (1/2))))
