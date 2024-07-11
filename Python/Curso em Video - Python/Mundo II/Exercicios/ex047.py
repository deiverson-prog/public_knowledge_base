#EX.47
#CRIE UM PROGRAMA QUE MOSTRE NA TELA TODOS OS NÚMEROS PARES QUE ESTÃO NO
#INTERVALO ENTRA 1 A 500.

#METODO 1

for c in range(2,51,2):
    print(c)

#METODO 2

for n in range(1,51):
    if n % 2 ==0:           #---> único problema (quantidade de iterações) cuidado!
        print(n, end=' ')