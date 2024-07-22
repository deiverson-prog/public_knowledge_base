'''Crie um programa onde o usuário possa digitar sete valores númericos e 
cadastre-os em uma lista única que mantenha separados os valores pares e 
impares. No final mostre os valores pares e impares em ordem crescente.'''

#METODO 1

listao = list()
par= impar = 0
for c in range(0,7):
    n=int(input('Digite um número: '))
    listao.append(n)
print('-='*20)
print(f'Os valores impares digitados foram: ',end='')
for i,n in enumerate(listao):
    if n % 2 == 0:
        listao.remove(n)
#print(f'Os valores impares digitados foram: ')
#    if n % 2 == 1:
#        listao.remove(n)

#METODO 2

num = [[],[]]
valor = 0
for c in range(1,8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

print('-='*30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram {num[0]}')
print(f'Os valores impares digitados foram {num[1]}')
#print(f'Todos os valores: {num}')