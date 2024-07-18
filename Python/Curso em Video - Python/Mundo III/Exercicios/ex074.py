'''Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o
maior valor que estão na tupla.'''

from random import randint
num = (randint (1,10), randint (1,10), randint (1,10), 
    randint (1,10), randint (1,10),)
print(f'Os valores sorteados são: {num}', end='')
for n in num:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(n)}')
print(f'O menor valor sorteado foi {min(n)}')
    
