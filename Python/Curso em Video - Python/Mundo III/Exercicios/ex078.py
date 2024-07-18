'''Faça um programa que leia 5 valores númericos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e suas respectivas
posições na lista.'''

valores = list()
maior = menor = 0
for cont in range(0,5):
    valores.append(int(input(f'Digite um valor na posição {cont}: ')))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]
print('=-'*30)
print(f'Você digitou os valores {valores}.')
print(f'O maior valor encontrado foi {maior} e encontram-se nas posições ',end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...',end='')
print()
print(f'O menor valor encontrado foi {menor} e encontram-se nas posições ',end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...',end='')
print()