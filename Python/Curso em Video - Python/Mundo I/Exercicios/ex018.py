#Ex018
#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do
#seno, cosseno e tangente desse ângulo.

#METODO 1
import math
angulo = float(input('Digite o ângulo que você deseja:' ))
seno = math.sin(math.radians(angulo))
print('O ãngulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O ãngulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O ãngulo de {} tem o TANGENTE de {:.2f}'.format(angulo, tangente))

#METODO 2
from math import radians, sin, cos, tan
ângulo = float(input('Digite o ângulo que você deseja:' ))
seno = sin(radians(ângulo))
print('O ãngulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
cosseno = cos(radians(ângulo))
print('O ãngulo de {} tem o COSSENO de {:.2f}'.format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print('O ãngulo de {} tem o TANGENTE de {:.2f}'.format(ângulo, tangente))