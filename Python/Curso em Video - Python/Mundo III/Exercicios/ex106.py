'''Faça um mini-sistema que utilieza o interactive Help do Python. O Usuário
vai digitar o comando e o manual vai aparecer. Qaundo o usuário digitar a 
palavra 'FIM', o programa se encerrará.

Obs.: Use cores.'''  

from time import sleep
c = ('\033[m',       # 0 - sem cores
     '\033[0;30;41m', # 1 - vermelho
     '\033[0;30;42m', # 2 - verde
     '\033[0;30;43m', # 3 - amarelo
     '\033[0;30;44m', # 4 - azul
     '\033[0;30;45m', # 5 - roxo
     '\033[7,30m'     # 6 - branco
     );

def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[3],end='')
    help(com)
    print(c[0],end='')

def título(msg, cor=0):
    tam = len(msg) +4
    print(c[cor])
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    print(c[3])
    sleep(1)

#Programa Principal
comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP',2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!',1)