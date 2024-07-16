'''Crie um programa que leia nome e o preço de vários produtos. O programa
deverá perguntar se o usuário vai continuar. No final mostre:

A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$ 1000.
C) Qual é o nome do produto mais barato.'''

print('-'*20)
print('Loja do Deivão')
print('-'*20)
soma_compra = totprod1000 = menor = quant = 0
barato = ' '
while True:
    nome_produto = str(input('Nome do produto: ')).capitalize()
    preço_produto = float(input('Preço: R$ '))
    soma_compra += preço_produto
    quant += 1
    if preço_produto > 1000:
        totprod1000 += 1
    if quant == 1 or preço_produto < menor:
        menor = preço_produto
        barato = nome_produto
#    else:
#        if preço_produto < menor:
#            menor = preço_produto
#            barato = nome_produto   # ---- > bloco simplificado na linha 20.#
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N] ')).capitalize().strip()[0]
    if continua == 'N':
        break
print('FIM DO PROGRAMA')
print(f'O total da compra foi de R$ {soma_compra:.2f}')
print(f'Temos {totprod1000} produtos custando mais de R$ 1000')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}.')