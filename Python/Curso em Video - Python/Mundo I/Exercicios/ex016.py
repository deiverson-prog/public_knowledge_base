#Ex016
#Crie um programa que leia um numero Real qualquer pelo teclado e 
#mostre na tela sua proporção inteira.

import math

num = float(input ('Digite um número: '))
print ('O número {} tem a parte inteira {}.'.format(num, math.trunc(num)))