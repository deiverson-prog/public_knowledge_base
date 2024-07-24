'''Faça um programa que tenha uma função maior(), que receba vários parâmetros
com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''

def maior(*núm):
    for v in núm:
        print(f'{v} ',end='')

#maior(1,2,3,4,5,6,7)

#Solução Completa

def Maior(*Núm):
    cont = maior = 0
    print('-='*20)
    print('Analisando os valores passados...')
    for v in Núm:
        print(f'{v} ',end='')
        if cont == 0 or v > maior:
            maior = v
            cont+=1
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}!')

Maior(1,2,3,4,5,6,7)