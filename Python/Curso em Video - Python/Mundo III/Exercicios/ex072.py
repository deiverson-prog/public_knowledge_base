'''CRIE UM PROGRAMA QUE TENHA UMA TUPLA TOTALMENTE PREENCHIDA COM UMA CONTAGEM
POR EXTENSO, DE ZERO ATÉ VINTE.
SEU PROGRAMA DEVERÁ LER UM NÚMERO PELO TECLADO (ENTRE 0 E 20) E MOSTRÁ-LO POR 
EXTENSO.'''

#METODO 1
from num2words import num2words

extenso = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
n = ' '
while n not in extenso:
    n = int(input('Digite um número de 0 a 20: '))
    
n_ptbr = num2words(n, lang = 'pt-br')
print(f'Você digitou o número {n_ptbr}')

#METODO 2

cont = ('zero', 'um', 'dois', 'três','quatro','cinco','seis','sete','oito','nove',
'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis','dezessete',
'dezoito','dezenove','vinte')
while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente! ', end='')
    print(f'Você digitou o número {cont[num]}')    
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('PROGRAMA ENCERRANDO')