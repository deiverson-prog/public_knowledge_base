#Ex022
#Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas
# - O nome com todas as letras minusculas
# - Quantas letras ao todo (sem considerar espaços)
# - Quantas letras tem o primeiro nome.

#METODO 1
name = str(input('Digite seu nome completo: '))

print(name.upper())
print(name.lower())
print(len(name.replace(' ','')))
dname = name.split()
print(len(dname[0]))


#METODO 2
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculo é {}'.format(nome.upper()))
print('Seu nome em minúsculo é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu nome tem ao todo {} letras'.format(len(name.replace(' ',''))))
dnome = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(dnome[0], len(dnome[0])))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))