#EX.050
#DESENVOLVA UM PROGRAMA QUE LEIA SEIS NUMEROS INTEIROS E MOSTRE A SOMA 
#APENAS DAQUELES QUE FOREM PARES. 
#SE O VALOR DIGITADO FOR IMPAR, DESCONSIDERE-O.

#METODO 1
s=0
for c in range (1, 7):
    n=int(input('Digite um número: '))
    if n % 2 ==0:
        s+=n
print('A soma apenas do números pares é igual a {}.'.format(s))

#METODO 2
s=0
cont = 0
for c in range (1, 7):
    n=int(input('Digite o {}º número: '.format(c)))
    if n % 2 ==0:
        s+=n
        cont+=1
print('A soma dos {} números PARES é igual a {}.'.format(cont,s))