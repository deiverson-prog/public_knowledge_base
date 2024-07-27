'''Crie um pacote chamado utilidadesCEV que tenha dois módulos internos chamados
moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109
para o primeiro pacote e mantenha tudo funcionando.'''

from utilidadescev import moeda #verificar como importar no VSCode
from utilidadescev import dado 

p = float(input('Digite o preço: '))
moeda.resumo(p,12,20)