#Ex006
#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n1 = int ( input ('Digite um número: '))
d = n1 * 2
t = n1 * 3
r = n1 ** (1/2)
print ('O número escolhido foi: {} \n O dobro de {} vale {}. \n O triplo de {} vale {}.'.format(n1, n1, d, n1, t), end=' A raiz de {} vale {:.2f}.'.format(n1, r))

#aplicação de "n\" & "End="""

#outras possibilidades abaixo:
print(' \n teste 002#')
n1 = int ( input ('Digite um número: '))
print ('\n O dobro de {} vale {}. \n O triplo de {} vale {}. \n A raiz de {} vale {:.2f}.'.format(n1, (n1*2), n1, (n1*3), n1, (n1**(1/2))))

#usando "pow" como calculador de potência 
print(' \n teste 003#')
n1 = int ( input ('Digite um número: '))
print ('\n O dobro de {} vale {}. \n O triplo de {} vale {}. \n A raiz de {} vale {:.2f}.'.format(n1, (n1*2), n1, (n1*3), n1, pow(n1, (1/2))))
