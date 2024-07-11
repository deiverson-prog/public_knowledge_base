#EX.051
#DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZÃO DE UMA PA. 
#NO FINAL, MOSTRE OS 10 PRIMEIROS TERMOS DESSA PROGRESSÃO.

#METODO 1

print('='*21)
print('{:^20}'.format(' 10 TERMOS DE UMA PA '))
print('='*21)
t1=int(input('Primeiro termo: '))
r=int(input('Razão: '))
dec = t1 + (10 - 1) * r
for c in range(t1,dec+r,r):
    print('{}'.format(c), end=' → ')
print('ACABOU!')