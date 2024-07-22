'''Crie um programa qe leia nome, sexo e idade de várias pessoas, guardando
os dados de cada pessoa em um dicionário e todos os dicionários e uma lista.
No final mostre:

a) Quantas pessoas foram cadastradas.
b) A média de idade do grupo.
c) Uma lista com todas as mulheres.
d) Uma lista com todas as pessoas com a idade acima da média.'''

#metodo 1
grupo = []
c=0
while True:
    pessoas = {'nome':str(input('Nome: ')),'Sexo':str(input('Sexo [F/M]: ')),'Idade':int(input('Idade: '))}
    grupo.append(pessoas.copy())
    pessoas.clear
    r= str(input('Deseja continuar? [S/N] '))
    if r in 'Nn':
        break
print(f'Foram cadastradas {len(grupo)}')
print(grupo)

#Metodo 2

pessoa = dict()
galera = []
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa ['sexo'] = str(input('Sexo [F/M]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        r= str(input('Deseja continuar? [S/N] ')).upper()[0]
        if r in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if r == 'N':
        break
print('-='*30)
print(f'a) Ao todo temos {len(galera)} cadastrados.')
média = soma / len(galera)
print(f'b) A média de idade é de {média:5.2f} anos.')
print(f'c) As mulheres cadastradas foram ',end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}',end='')
print()
print(f'd) Lista das pessoas que estão acima da média:',end='')
for p in galera:
    if p['idade'] >=média:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
            print()
print('<< ENCERRADO >>')