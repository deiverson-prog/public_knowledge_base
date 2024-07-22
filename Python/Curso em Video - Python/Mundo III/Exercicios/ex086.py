'''Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores
lidos pelo teclado. Nofinal mostre a matriz na tela com a formatação correta.'''
'''
listan=[[int(input('Digite um valor para [0, 0]: '))], 
        [int(input('Digite um valor para [0, 1]: '))], 
        [int(input('Digite um valor para [0, 2]: '))], 
        [int(input('Digite um valor para [1, 0]: '))], 
        [int(input('Digite um valor para [1, 1]: '))], 
        [int(input('Digite um valor para [1, 2]: '))], 
        [int(input('Digite um valor para [2, 0]: '))], 
        [int(input('Digite um valor para [2, 1]: '))],
        [int(input('Digite um valor para [2, 2]: '))]]
print('-='*20)
print(f'{listan[0]:^5} {listan[1]:^5} {listan[2]:^5}\n{listan[3]:^5} {listan[4]:^5} {listan[5]:^5}\n{listan[6]:^5} {listan[7]:^5} {listan[8]:^5}')

#metodo2'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0,3):  #para cada linha no critério de 1 a 3
    for c in range (0,3): #para cada coluna no critério de 1 a 3
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: ')) #inclua valores nas linhas e colunas da matriz

print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
