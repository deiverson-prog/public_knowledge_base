'''Faça um programa que mostre a tabuada de vários números, um de cada vez, 
para cada valor digitado pelo usuário. O programa será interrompido quando
o número solicitado for negativo.'''

#Metodo 1

n = 0
while True:
    print('-'*40)
    n = int(input('Digite um número para ver sua tabuada:'))
    print('-'*40)
    if n < 0:
        break
    for c in range(1,11):
        print(f'{n} x {c:2} = {n*c}')
print('Programa tabuada encerrando... Volte sempre!')

#Metodo 2

while True:
    print('-'*40)
    n = int(input('Digite um número para ver sua tabuada:'))
    print('-'*40)
    if n < 0:
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
print('Programa tabuada encerrando... Volte sempre!')