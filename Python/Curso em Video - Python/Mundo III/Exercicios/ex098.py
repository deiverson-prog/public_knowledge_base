'''Faça um programa que tenha uma função chamada contador(), que receba três 
parâmetros: INICIO, FIM e PASSO e realize a contagem.

Segue programa tem que realizar três contagens através da função criada:

A) De 1 até 10, de 1 em 1.
B) De 10 até 0, de 2 em 2.
C) Uma contagem personalizada.'''

from time import sleep

def contador():
    for c in range(1, 11):
        print(f'{c} ', end='')
    print('FIM!')

    for c in range(10, -1, -2):
        print(f'{c} ', end='')
    print('FIM!')

contador()

# Solução completa:

def Contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-='*20)
    print(f'Contagem de {i} até {f} de {p} em {p}!')

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=False)
            sleep(0.5)
            cont+=p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            cont-=p
        print('FIM!')

Contador(1, 10, 1)
Contador(10, 0, 2)
print('-='*20)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
Contador(ini, fim, pas)