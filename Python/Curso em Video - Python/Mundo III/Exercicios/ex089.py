'''Crie um programa que leia nome e duas notas de vários alunos e guarde
tudo em uma lista composta. No final, mostre um boletim contendo a média
de cada um e permita que o usuário possa mostrar as notas de cada aluno
individualmente.'''
'''
aluno = []
while True:
    aluno.append(str(input('Nome: ')))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
#    for a in range(0,2):
#        aluno.append(float(input('Nota: ')))
    r=str(input('Deseja continuar? [S/N] ' ))
    if r in 'Nn':
        break
print(aluno)'''

#metodo2

ficha= list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    média = (nota1+nota2)/2
    ficha.append([nome,[nota1, nota2],média])  #lista composta
    r=str(input('Deseja continuar? [S/N] ' ))
    if r in 'Nn':
        break
print('-='*30)
print(f'{"Nº":<4}{"Nome":<10}{"Média":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*35)
    opc = int(input('Mostrar notas de qual aluno? [999 interrompe]: '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) -1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
