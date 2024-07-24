'''Faça um programa que tenha um função chamada área(), que receba as dimensões
de um terreno retangular (Largura e Comprimento) e mostre a área do terreno.'''

def área(L, C):
    m = L*C
    print(f'A área de um terreno {L} x {C} é de {m}m².')

#Programa principal
print('CONTROLE DE TERRENOS')
print('-'*20)
L=float(input('LARGURA (m): '))
C=float(input('COMPRIMENTO (m): '))
área(L, C)