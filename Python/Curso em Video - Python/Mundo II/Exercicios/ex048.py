#EX.48
#FAÇA UM PROGRAMA QUE CALCULE A SOMA ENTRE TODOS OS NÚMEROS IMPARES QUE SÃO
#MULTIPLOS DE TRÊS E QUE SE ENCONTRAM NO INTERVALO DE 1 ATÉ 500.

#METODO 1 

soma = 0     #---> ACUMULADORES
cont = 0
for c in range(1, 501, 2):
    if c % 3 ==0:    #--> DIVISIVEIS POR X 
        cont += 1  #or cont = cont + 1  --> CONTAGEM
        soma += c  #or soma = soma + c  --> SOMA DOS MULTIPLOS
print('A soma de todos os {} valores solicitados é {}'.format(cont,soma))
        