'''Crie um programa onde o usuário possa digitar vários valores númericos e
cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será 
adicionado. No final, serão exibidos todo os valores únicos digitados, em 
ordem crescente.'''

valores = list()
while True:
    v= (int(input('Digite um valor: ')))
    if v not in valores:
        valores.append(v)
        print('Valor adicionado com sucesso...')
    else:   
        print('Este número já existe! Não será adicionado!')
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-='*30)
valores.sort()
print(f'Você digitou os valores {valores}')