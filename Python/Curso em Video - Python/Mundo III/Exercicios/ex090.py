'''Faça um programa que leia nome e a média de um aluno, guardando também
a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.'''

#metodo 1
aluno = dict()
aluno ['nome'] = str(input('Nome: '))
aluno ['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:  
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print ('-='*30)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')


#Metodo 2
Alun={}
grupo = []
for c in range(0,1):
    Alun['nome'] = str(input('Nome: '))
    Alun['Média'] = float(input(f'Média de {Alun["nome"]}: '))
    if Alun['Média'] >=7:
        Alun['Situation'] = 'Aprovado'
    elif 5 <= Alun['Média'] < 7:
        Alun['Situation'] = 'Recuperação'
    else:
        Alun['Situation'] = 'Reprovado'
    grupo.append(Alun.copy())
print (grupo)
print (aluno)
print ('-='*30)
for k, v in Alun.items():
    print(f' - {k} é igual a {v}')
