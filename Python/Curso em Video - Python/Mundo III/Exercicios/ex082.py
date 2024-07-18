'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares
e os valores impares digitados, respectivamente. Ao final, mostre o conteúdo 
das três listas geradas.'''


lista1 = []
impar = []
par= []
while True:
    v=lista1.append(int(input('Digite um valor: ')))
    r = str(input('Deseja continuar? [S/N] '))
    if r in 'Nn':
        break
print('-='*30)
lista1.sort()
print(f'A lista completa digitada: {lista1}')
for i, v in enumerate(lista1): 
    if v % 2 == 0:        
        par.append(v)
    else:               #or elif v % 2 == 1:
        impar.append(v)
print(f'A lista de pares é: {par}')
print(f'A lista de impares é: {impar}')
