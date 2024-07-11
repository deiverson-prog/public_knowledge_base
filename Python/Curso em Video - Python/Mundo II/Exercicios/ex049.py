#EX.49
#REFAÇA O DESAFIO 009, MOSTRANDO A TABUADA DE UM NÚMERO QUE O USUÁRIO 
#ESCOLHER SÓ QUE AGORA UTILIZANDO UM LAÇO FOR.

#METODO 1

num = int( input ('Digite um número para ver sua tabuada:'))
print('-' * 13)
for c in range(1,11):
    print('{} x {:2} = {}'.format(num, c, num*c))
print('-' * 13)

#METODO 2

num = int(input('Digite um número para ver sua tabuada:'))
for c in range(1,11):
    print('{} x {:2} = {}'.format(num, c, num*c))
