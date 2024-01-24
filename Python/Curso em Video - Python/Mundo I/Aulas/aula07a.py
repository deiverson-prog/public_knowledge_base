#Poderes do String = str
#{:x} = quantidade de caráteres
#{:>x} = quantidade de caráteres + alinhamento à direita
#{:<x} = quantidade de caráteres + alinhamento à esquerda
#{:<x} = quantidade de caráteres + centralizado
#{:*<x} = quantidade de caráteres + centralizado com caráteres

nome = input ('Qual é o seu nome?')
print ('Prazer em te conhecer {:*^20}!'.format(nome))

#Entregando a soma direto
n1 = int (input ('Um valor:'))
n2 = int (input ('Outro valor:'))
print ('A soma vale {}'.format(n1+n2))

#Entregando cada resultado
n1 = int (input ('Um valor:'))
n2 = int (input ('Outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

#\n = nova linha ---> end="" = continua na mesma linha
print ('A soma vale {}, \n o produto é {} \n e a divisão é {:.3f}'.format(s, m, d), end=" ")
print ('Divisão inteira {} e potência {}'.format(di, e))
