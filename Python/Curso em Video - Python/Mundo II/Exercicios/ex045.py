#EX.045
#CRIE UM PROGRAMA QUE FAÇA O COMPUTADOR JOGAR JOKENPÔ COM VOCÊ.

#METODO 1
from random import choice
print('Escolha uma opção: \n Pedra \n Papel \n Tesoura')
eu = str(input('Digite a opção desejada: ')).strip().capitalize()
print('Você escolheu: {}'.format(eu))
opções = ['Pedra','Papel','Tesoura']
pc = choice (opções)
print('Pc escolheu: {}'.format(pc))

if eu == 'Pedra' and pc == 'Papel':
    print('Pc ganhou! \n Jogue novamente!')
elif eu == 'Pedra' and pc == 'Tesoura':
    print('Você ganhou! \n Jogue novamente!')
elif eu == 'Papel' and pc == 'Tesoura':
    print('Pc ganhou! \n Jogue novamente!')
elif eu == 'Papel' and pc == 'Pedra':
    print('Você ganhou! \n Jogue novamente!')
elif eu == 'Tesoura' and pc == 'Pedra':
    print('Pc ganhou! \n Jogue novamente!')
elif eu == 'Tesoura' and pc == 'Papel':
    print('Você ganhou! \n Jogue novamente!')
elif eu == pc:
    print('Nós empatamos! \n Jogue novamente!')

#METODO 2
from random import randint 
from time import sleep
itens = ('Pedra','Papel','Tesoura')
computador = randint (0, 2)
print('''Suas Opções: 
[0] PEDRA 
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-='*12)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*12)

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
    print('JOGADA INVALIDA')
elif computador == 1
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
    print('JOGADA INVALIDA')
elif computador == 2
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
    print('JOGADA INVALIDA')