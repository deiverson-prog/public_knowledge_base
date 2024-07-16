'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada
pessoa cadastras, o programa deverá perguntar se o usuário quer ou não 
continuar. No final, mostre:

A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.'''

#METODO 1
tot18 = totM = totF = 0
while True:
    print('-'*15)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >=18:
        tot18 += 1
    if sexo == 'M':
        totM += 1
    elif sexo == 'F' and idade < 20:
        totF += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Total de homens cadastrados: {totM}')
print(f'Total de mulheres cadastradas com menos de 20 anos: {totF}')