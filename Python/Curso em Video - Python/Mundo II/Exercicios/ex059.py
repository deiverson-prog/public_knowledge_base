'''CRIE UM PROGRAMA QUE LEIA DOIS VALORES E MOSTRE UM MENU NA TELA:
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA

SEU PROGRAMA DEVERÁ REALIZAR A OPERAÇÃO SOLICITADA EM CADA CASO.'''

#METODO 1

from time import sleep
n1=int(input('Digite um valor: '))
n2=int(input('Digite outro valor: '))
opção = 0
while opção != 5:
    print('''Escolha uma das opções abaixo:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opção = int(input('Qual é a sua opção? '))
    if opção == 1:
        Soma = n1+n2
        print('A soma entre {} + {} é de {}.'.format(n1, n2, Soma))
    elif opção == 2:
        mult = n1 * n2
        print('O resultado de {} x {} é {}.'.format(n1, n2, mult))
    elif opção == 3:	
        if n1 > n2:
            maior = n1
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
        else:
            menor = n2
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, menor))
    elif opção == 4:
        print('Informe os números novamente: ')
        n1=int(input('Digite um valor: '))
        n2=int(input('Digite outro valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção Inválida. Tente novamente!')
print('=-='*10)
sleep(2)
print('Fim do programa! Volte sempre!')
