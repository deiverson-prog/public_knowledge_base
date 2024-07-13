'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será
interrompido quando o jogador PERDER, mostrando o total de vitórias 
consecutivas que ele conquistou no final do jogo.'''

#Metodo 1
from random import randint
v = 0
while True:
    player1=(int(input('Digite um número: ')))
    pc = randint(0,11)
    total = pc + player1
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou ìmpar? [P/I] ')).strip().capitalize()[0]
    print(f'Você jogou {player1} e o computador jogou {pc}. Total de {total} ',end='')
    print('DEU PAR' if total % 2 ==0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 ==0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':   
        if total % 2 ==1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')
