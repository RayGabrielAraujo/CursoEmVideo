#Desafio 14, escreva um programa que converta uma temperatura digitada em ºC e converta para ºF
c = float(input('Digite a temperatura em Graus Celsius(ºC): '))

f = (c * 9/5) + 32

print('A temperatura de {}ºC corresponde a {}ºF'.format(c,f))

