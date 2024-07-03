#Ex033
#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

#a = int(input('Primeiro Valor:'))
#b = int(input('Segundo Valor:'))
#c = int(input('Terceiro Valor:'))
#if a<b and a<c:
#    menor = a
#if b<a and b<c:
#    menor = b
#if c<a and c<b:
#    menor = c    
#print('O menor valor digitado foi {}'.format)
#print('O maior valor digitado foi {}'.format)


a = int(input('Primeiro Valor:'))
b = int(input('Segundo Valor:'))
c = int(input('Terceiro Valor:'))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print('O menor valor digitado foi {}'.format(menor))
maior = a
if b<a and b<c:
    maior = b
if c<a and c<b:
    maior = c
print('O maior valor digitado foi {}'.format(maior))
