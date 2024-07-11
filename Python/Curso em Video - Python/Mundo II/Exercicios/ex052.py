#EX.052
#FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E DIGA SE ELE É OU NÃO 
#UM NÚMERO PRIMO.

#METODO 1

cont=0
n=int(input('Digite um número: '))
for c in range(1,n+1):
    if n % c == 0:
        print('\033[33m', end='')
        cont+= 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(n, cont))
if cont == 2:
    print('e por isso é PRIMO!')
else:
    print('e por isso NÃO É PRIMO!')
