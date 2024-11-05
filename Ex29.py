#Desafio 29, escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = float(input('Qual a velocidade em que você passou no radar? '))

if velocidade <= 80:
    print('Você estava dentro do limite de velocidade')
else: 
    multa = (velocidade - 80) * 7
    print('Você estava fora do limite de velocidade e foi multado em R$ {:.2f}'.format(multa))    
