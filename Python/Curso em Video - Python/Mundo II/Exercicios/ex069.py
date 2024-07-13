'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada
pessoa cadastras, o programa deverá perguntar se o usuário quer ou não 
continuar. No final, mostre:

A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.'''

#METODO 1

while True:
soma = conta = 0

print('-'*15)
idade= int(input('Idade: '))
sexo= str(input('Sexo: [M/F] '))
print('-'*15)
Continua = str(input('Quer continuar? [S/N] '))

