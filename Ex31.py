#Desafio 31: desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

km = float(input('Digite a distância da viagem para ser calculado o valorda sua viagem: '))

if km >= 200:
    valor = km * 0.45
    print('O valor da sua viagem é de R$ {:.2f}'.format(valor))
else: 
    valor = km * 0.50
    print('O valor da sua viagem é de R$ {:.2f}'.format(valor))

