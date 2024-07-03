#ESCREVA UM PROGRAMA QUE LEIA DOIS NÚMEROS E COMPARE-OS. 
#MOSTRANDO NA TELA UMA MENSAGEM:
#- O PRIMEIRO VALOR É MAIOR
#- O SEGUNDO VALOR É MAIOR
#- NÃO EXISTE VALOR MAIOR. OS DOIS SÃO IGUAIS

#METODO 1

Num1 = float(input('Escreva um número: '))
Num2 = float(input('Escreva outro número: '))

if Num1 > Num2:
    print('O primeiro Valor é Maior')
elif Num1 < Num2:
    print('O segundo Valor é Maior')
elif Num1 == Num2:
    print('Não existe valor maior. Os dois são iguais')

#METODO 2
N1 = int(input('Primeiro número: '))
N2 = int(input('Segundo número: '))

if N1 > N2:
    print('O PRIMEIRO Valor é Maior')
elif N1 < N2:
    print('O SEGUNDO Valor é Maior')
else:
    print('Não existe valor maior. Os dois são IGUAIS')
