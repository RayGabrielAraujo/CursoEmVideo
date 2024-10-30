#desafio 10, crie um programa que leia quanto dinhero a pessoa tem na sua carteira e mostra quantos Dólares ela pode comprar.
#considere a cotação do dólar para o real seja de R$ 3.27

num = float(input('Diga quantos reais você tem: '))

real = 3.27

print('Você poderá pegar {:.2f} Dólares.'.format(num/real))