#desafio 26, faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
#  em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} nesta frase'.format(frase.count('A')))
print('Sendo a primeira letra A na {}º posição e a última vez na {}º posição.'.format(frase.find('A')+1, frase.rfind('A')+1))