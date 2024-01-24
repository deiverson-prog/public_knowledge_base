#Ex006
#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n1 = int ( input ('Digite um número: '))
d = n1 * 2
t = n1 * 3
r = t ** (1/2)
print ('O número escolhido foi: {} \n O dobro desse número é: {} \n O triplo desse número é: {}'.format(n1, d, t), end=' >>> a raiz desse número é: {}'.format(r))
