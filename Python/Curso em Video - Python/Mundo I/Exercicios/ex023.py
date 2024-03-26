#Ex023
#Faça um progama que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.

#Ex.: Digite um número: 1834
#unidade: 4
#dezena: 3
#centena: 8
#milhar: 1

#METODO 1
num = int(input('Digite uma número: '))
u = num // 1 % 10            #-> % significa tirar um módulo
d = num // 10 % 10           #-> % significa tirar um módulo
c = num // 100 % 10          #-> % significa tirar um módulo
m = num // 1000 % 10         #-> % significa tirar um módulo
print('Analisando o número {}'.format(num))
print('Unidade: {} '.format(u))
print('Dezena: {} '.format(d))
print('Centena: {} '.format(c))
print('Milhar: {} '.format(m))

#METODO 2  = funciona só pra 4 digitos
num = int(input('Informe um número: '))
n = str(num)
print('Analisando o número {}'.format(num))
print('Unidade: {} '.format(n[3]))
print('Dezena: {} '.format(n[2]))
print('Centena: {} '.format(n[1]))
print('Milhar: {} '.format(n[0]))