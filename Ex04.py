#desafio 04, crie um programa que leia algo que o usuário digite
#e mostre o seu tipo e todas as informações possiveis sobre ela
msm = input('Digite qualquer coisa: ')

print(f'O tipo primitivo desse valor é: {type(msm)}')

print(f'A mensagem tem espaços? {msm.isspace()}')
print(f'A mensagem é um número? {msm.isnumeric()}')
print(f'A mensagem é um alfabético? {msm.isalpha()}')
print(f'A mensagem é um alfanumérico {msm.isalnum()}')
print(f'A mensagem está em maiúsculas? {msm.isupper()}')
print(f'A mensagem está em minúsculas? {msm.islower()}')
print(f'A mensagem está capitalizada (primeira letra maiúscula)? {msm.istitle()}')
print(f'A mensagem é um dígito? {msm.isdigit()}')
print(f'A mensagem é um identificador válido? {msm.isidentifier()}')

