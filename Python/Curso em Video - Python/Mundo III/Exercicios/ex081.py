'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:

a) Quantos números foram digitados.
b) A lista de valores ordenados de forma decrescente.
c) Se o valor 5 foi digitado e está ou não na lista.'''

valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-='*30)
print(f'Foram digitados {len(valores)} números')
valores.sort(reverse=True)
print(f'Segue lista em ordem decrescente: {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi encontrado na lista!')