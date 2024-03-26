#Ex025
#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

#METODO 1
name = str(input('Digite seu nome: '))
print ('SILVA' in name.upper())

#METODO 2
nome = str(input('Qual é seu nome completo? ')).strip()
print ('Seu nome tem Silva? {}'.format('Silva' in nome.title()))