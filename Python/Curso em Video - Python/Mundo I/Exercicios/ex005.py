#Ex005
#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

#Com 3 Variáveis
n = int ( input ('Digite um número: '))
a = n - 1
s = n + 1
print('O número escolhido foi: {}! \n Seu sucessor é: {}! \n E seu antecessor é: {}!'.format(n, s, a))

#Com 1 Variável
n = int ( input ('Digite um número: '))
print('Analisando o valor {}, seu sucessor é {} e seu antecessor é {}!'.format(n, (n+1), (n-1)))