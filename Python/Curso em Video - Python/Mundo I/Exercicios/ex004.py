#Ex004
#Crie um programa que leia algo pelo teclado e mostre na tela o seu tipo e todas as informações possiveis sobre ele.

a = input('Digite algo:')
print('O tipo primitivo desse valor é {}'.format(type(a)))
print('Só tem espaços?',a.isspace())
print('É um número?',a.isnumeric())
print('É alfabético?',a.isalpha())
print('É alfanumérico?',a.isalnum())
print('Está em maiúsculo?',a.isupper())
print('Está em minúsculo?',a.islower())
print('Está capitalizado?',a.istitle())