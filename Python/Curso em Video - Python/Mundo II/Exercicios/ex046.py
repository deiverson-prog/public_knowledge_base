#EX.46
#Faça um programa que mostre na tela uma contagem regressiva para o estouro de
#fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

#METODO 1

from time import sleep

for c in range(10,-1,-1):
    print(c)
    sleep(1)
print('Surprise!!!')

#METODO 2

from time import sleep

for cont in range(10,-1,-1):
    print(cont)
    sleep(0.5)
print('BUM! BUM! POOOW!')