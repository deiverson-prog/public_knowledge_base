'''Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use alguma dessas funções.'''

from moeda import metade, dobro, aumentar, diminuir

P = float(input('Digite o preço: '))
a = 10
print(f'A metade de R$ {P} é R$ {metade(P)}')
print(f'A Dobro de R$ {P} é R$ {dobro(P)}')
print(f'Ao Aumentar 10% no valor, temos R$ {aumentar(P,a)}')
print(f'Ao Diminuir 10% no valor, temos R$ {diminuir(P,a)}')