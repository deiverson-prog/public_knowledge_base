'''MELHORE O JOGO DO DESAFIO 028 ONDE O COMPUTADOR VAI "PENSAR" EM UM NÚMERO 
ENTRE 0 E 10. SÓ QUE AGORA O JOGADOR VAI TENTAR ADIVINHAR ATÉ ACERTAR, 
MOSTRANDO NO FINAL QUANTOS PALPITES FORAM NECESSÁRIOS PARA VENCER.'''

#METODO 1

from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True 
    else:
        if jogador < computador:
            print('MAIS... Tente mais uma vez.')
        elif jogador > computador:
            print('MENOS... Tente mais uma vez.') 
print('Parabéns, você acertou com {} tentativas!'.format(palpites))