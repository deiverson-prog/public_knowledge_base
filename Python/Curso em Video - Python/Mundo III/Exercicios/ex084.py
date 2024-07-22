'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em
uma lista. No final, mostre:

a) Quantas pessoas foram cadastradas.
b) Uma listagem com as pessoas mais pesadas.
c) Uma listagem com as pessoas mais leves. '''

'''#METODO 1
pessoas = []
dado = []
pesados =[]
leves = []
c = maior = menor = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso [Kg]: ')))
    pessoas.append(dado[:])
    dado.clear()
    r=str(input('Deseja continuar? [S/N] '))
    if r in 'Nn':
        break
for p in pessoas:
    c +=1
    if p[1] == 1:
        maior = menor = p[1]
    else:
        if p[1] > maior:
            maior = p[1] 
        if p[1] < maior:
            menor = p[1]
#print(f'Foram cadastradas {c} pessoas.') #or 
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ')
print(f'O menor peso foi de {menor}Kg. Peso de ')

#METODO 2'''

temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso [Kg]: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    r=str(input('Deseja continuar? [S/N] '))
    if r in 'Nn':
        break
print(f'Foram cadastradas {len(princ)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ',end='')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}]',end='')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ',end='')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}]',end='')
print()
