'''Aprimore o desafio anterior, mostrando no final:

a) A soma de todos os valores pares digitados.
b) A soma dos valores da terceira coluna.
c) O maior valor da segunda linha.'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = maior = somacol = 0
for l in range(0,3):  #para cada linha no critério de 1 a 3
    for c in range (0,3): #para cada coluna no critério de 1 a 3
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: ')) #inclua valores nas linhas e colunas da matriz

print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
    print()
print('-='*30)
print(f'A soma dos valores pares é:{somapar}')
for l in range(0,3):
    somacol += matriz[l][2] #fixando a coluna, variando apenas as linhas
print(f'A soma dos valores da terceira coluna é: {somacol}')
for c in range(0,3):
    if c == 0 or matriz[1][c] > maior: #fixando a linha, variando apenas as colunas
        maior = matriz[1][c]
#    elif matriz[1][c] > maior:
#        maior = matriz[1][c]
print(f'O maior valor da segunda linha é: {maior}')