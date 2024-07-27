'''Crie um pacote chamado utilidadesCEV que tenha dois módulos internos chamados
moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109
para o primeiro pacote e mantenha tudo funcionando.'''

#from ex111.utilidadescev import moeda
#from ex111.utilidadescev import dado
from moeda import moeda #verificar como importar no VSCode

p = float(input('Digite o preço: '))
moeda.resumo(p,12,20)