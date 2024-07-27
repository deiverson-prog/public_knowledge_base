'''Modifique as funções que form criadas no desafio 107 para que elas aceitem 
um parâmetro a mais, informando se o valor retornado por elas vai ser ou não 
formatado pela função moeda(), desenvolvida no desafio 108.'''

import moeda

p = float(input('Digite o preço: '))
a = 10
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, False)}')
print(f'A Dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Ao Aumentar 10% no valor, temos {moeda.aumentar(p, a, True)}')
print(f'Ao Diminuir 10% no valor, temos {moeda.diminuir(p, a,True)}')