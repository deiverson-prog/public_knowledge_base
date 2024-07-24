'''Faça um programa que tenha uma lista chamada números e duas funções chamadas
sorteio() e somapar(). A primeira função vai sortear 5 números e vai colocá-los
dentro da lista e a segunda função vai mostrar a soma entre todos os valores 
PARES sorteados pela função anterior.'''


from random import randint
from time import sleep

def sorteio(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        n = randint(1,10)
        lista.append(n)    # or lista.append(randint(1,10))
        print(f'{n} ', end='', flush=False)
        sleep(0.3)
    print('\nPronto!')

def somaPar(lista):
    soma=0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {lista}, temos {soma}')


números = list() #or número = []
sorteio(números)
somaPar(números)
