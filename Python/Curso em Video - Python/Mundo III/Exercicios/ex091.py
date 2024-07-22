'''Crie um programa onde 4 jogadores joguem um dado e tenha resultados
aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse 
dicionário em ordem, sabe que o vencedor tirou o maior número do dado.'''

from random import randint
from time import sleep
from operator import itemgetter   #->itemgetter

JOGO = {'Jogador 1': randint (1,6),
        'Jogador 2': randint (1,6),
        'Jogador 3': randint (1,6),
        'Jogador 4': randint (1,6)}
Ranking = []
print('Valores sorteados: ')
for k, v in JOGO.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
Ranking = sorted(JOGO.items(), key=itemgetter(1), reverse = True)
print('-='*30)
print('  ==','Ranking dos jogadores:','==')
sleep(2)
for i, v in enumerate(Ranking):
    print(f'   {i+1}º Lugar: {v[0]} com {v[1]}.')
    sleep(1)



#METODO 2
#Valores sorteados:
#Jogo = {}
#Jogadores = []
#for c in range(1,5):
#    Jogo['jogador'] = randint(1,6)
#    Jogadores.append(Jogo.copy())
#    print(f'{c}º Jogador: {Jogo["jogador"]}')
    
#Ranking dos jogadores:
