'''Crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição
de parada. No final, mostre quantos números foram digitados e qual foi a soma 
entre eles (desconsiderando o flag).'''

#metodo 1
n1=1
cont = 0
cont1 = 0
while n1 != 999:
    n1=int(input('Digite um número: '))
    cont1 += 1
    cont += n1
print('A soma dos {} números digitados é de {}'.format((cont1-1),(cont-999)))
print('FIM')

#metodo 2
núm = cont = soma = 0
núm=int(input('Digite um número [999 para parar]: '))
while núm != 999:
    soma += núm
    cont += 1
    núm = int(input('Digite um número [999 para parar]: '))
print('A soma dos {} números digitados é de {}'.format(cont,soma))
print('Acabou')