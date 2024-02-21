#MÓDULO, FUNCIONALIDADE E BIBLIOTECA EM PY

#Import -> É utilizado para incluir alguma coisa como módulos/bibliotecas.
#Exemplo:
#Import(bebida) -> incluir o módulo/biblioteca de bebidas inteiro.

#Para utilizar a importação separada utilizamos o "From"
#From+Import -> É utilizado para incluir alguma coisa especifica dos módulos e bibliotecas.
#Exemplo:
#From(Bebida)Import(refrigerante) -> inclui apenas a bebida especifica que eu decidi.

#Exemplo de Biblioteca:
#math -> funcionalidade matemáticas.
 #ceil -> funcionalidade arredondamento para cima ^;
 #floor -> funcionalidade arredondamento para baixo \/;
 #trunc -> funcionalidade Trunqueite (elimina da virgula para frente, sem arrendondar (ex: 1,002 -> considera paras o 1.));
 #pow -> funcionalidade Potência (Power);
 #sqrt -> funcionalidade Raiz quadrada (Square root);
 #factorial -> funcionalidade fatorial de um número.
#from math import sqrt -> importa apenas uma função.
#from math import sqrt,ceil -> importa mais de uma funcão utilizando a virgula.

#Onde verificar todas as bibliotecas padrões do PY?
#R¹.: Python.org > Docs - "Verificar a versão do seu PY"
#R².: Python.org > PYPI - "Pesquisar o tipo de pacote que deseja incluir"

#COMANDO IMPORTADO BIBLIOTECA INTEIRA
#PRIMERA FORMA:
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))

#SEGUNDA FORMA:
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz))) #Arredondando para cima

#TERCEIRA FORMA:
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, math.floor(raiz))) #Arredondando para baixo

#TERCEIRA FORMA:
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz)) #Raiz com 2 casas decimais

#COMANDO IMPORTADO PARTE DA BIBLIOTECA #para verificar os itens da biblioteca apertar ctrl + espaço
#PRIMERA FORMA:
from math import sqrt 
num = int (input('Digite um número: '))
raiz = sqrt (num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

#SEGUNDA FORMA:
from math import sqrt, floor 
num = int (input('Digite um número: '))
raiz = sqrt (num)
print('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz))) #arredendando para baixo

#Importando biblioteca DOCs
#random -> permite gerar números aleatórios
#Exemplo de utilização1
import random
num = random.random ()  #gera um numero float (real) entre 0 e 1
print (num)

#Exemplo de utilização2
import random
num = random.randint(1,10)  #gera um numero int (inteiro) entre 0 e 1
print (num)

#Importação de bibliotecas PYPI
#Exemplo de utilização
import emoji
print(emoji.emojize('Hello, World :globe_showing_Americas:')) #verificar o cód. da versão instalada no manual.