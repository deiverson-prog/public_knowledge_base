'''Crie um programa que leia nome e o preço de vários produtos. O programa
deverá perguntar se o usuário vai continuar. No final mostre:

A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$ 1000.
C) Qual é o nome do produto mais barato.'''

print('-'*20)
print('Loja do Deivão')
print('-'*20)
nome_produto = str(input('Nome do produto: ')).capitalize() 
print(nome_produto)
preço_produto = int(input('Preço: R$ '))
continua = str(input('Quer continuar? [S/N] '))

print('FIM DO PROGRAMA')
print(f'O total da compra foi de R$ {}')
print(f'Temos {} produtos custando mais de R$ {}')
print(f'O produto mais barato foi {} que custa R$ {}.')