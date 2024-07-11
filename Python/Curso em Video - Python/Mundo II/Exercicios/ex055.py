#EX.055
#FAÇA UM PROGRAMA QUE LEIA O PESO DE CINCO PESSOAS. 
#NO FINAL, MOSTRE O MAIOR E O MENOR PESO LIDO.

#Metodo 1
maior = 0
menor = 0
for p in range (1,6):
    peso = float(input('Qual o peso da {}ª pessoa? ').format(p))
    if p == 1:
        maior = peso
        menor = peso
    else: 
        if peso > maior:
            maior = peso
        if peso < maior:
            menor = peso
print('O maior peso lido foi de {}Kg.'.format(maior))
print('O menor peso lido foi de {}Kg.'.format(menor))