''' VARIAVEIS COMPOSTAS [TUPLAS]

EM PY EXISTEM TRÊS TIPOS DE VARIAVEIS COMPOSTAS:

TUPLAS, LISTAS E DICIONÁRIOS

VARIÁVEL SIMPLES = UM ESPAÇO NA MEMÓRIA

= -> ATRIBUIÇÃO

VARIÁVEL SIMPLES

 LANCHE     =    HAMBURGUER
"VARIAVEL RECEBE    ITEM"

 LANCHE     =           SUCO   -> SE FIZER DESSA FORMA, ELIMINA O ITEM ANTERIOR
"VARIAVEL RECEBE    OUTRO ITEM"

CRIANDO UMA VARIÁVEL COM MAIS DE UM ESPAÇO NA MEMÓRIA ATRAVÉS DAS TUPLAS

VARIÁVEIS COMPOSTAS, ARMAZENAM VÁRIOS VALORES

PARA ACESSAR OS ELEMENTOS DENTRO DA VARIÁVEL SERÃO IDENTIFICADOS POR INDICIES NÚMERICOS

#EXEMPLO:
LANCHE = (HAMBURGUER, SUCO, PIZZA, PUDIM)

LANCHE = 4 ELEMENTOS
LANCHE0 = HAMBURGUER
LANCHE1 = SUCO
LANCHE2 = PIZZA
LANCHE3 = PUDIM

STRINGS - SÃO TUPLAS.
FATIAMENTO DE STRINGS.

print(LANCHE) #RETORNA TODOS OS LANCHES
print(LANCHE[2]) #RETORNA APENAS PIZZA
print(LANCHE[0:2]) #RETORNA HAMBURGUER E SUCO (DO 0 ATÉ 2 SENDO ULTIMO FATIAMENTO IGNORADO)
print(LANCHE[1:]) #RETORNA O SUCO, A PIZZA E O PUDIM (O FATIAMENTO 1 ATÉ O FIM)
print(LANCHE[-1]) #RETORNA O PUDIM (O ÚLTIMO ELEMENTO - CONSIDERANDO DE ATRÁS PARA FRENTE)
print(LANCHE[:2]) #RETORNA O HAMBURGUER E SUCO (MOSTRAR DO INICIO AO ELEMENTO 2, DESCONSIDERANDO O 2)
print(LANCHE[-2:]) #RETORNA A PIZZA E O PUDIM (DO ELEMENTO -2 (SEGUNDO DA DIREITA PARA ESQUERDA), ATÉ O FINAL)

#UTILIZANDO LEN
len(LANCHE) 4 #CONTA QUANTOS ELEMENTOS HÁ NA VARIÁVEL

#ESTRUTURAS DE REPETIÇÃO: WHILE SIMPLES, WHILE TRUE (INIFITO) E FOR (COM VARIAVEL DE CONTROLE)

#O PY CRIA A VARIÁVEL "c" (SIMPLES) 
for c in LANCHE: 
    print(c) #FAZ O LOOPING COM TODOS ELEMENTOS DA TUPLA E FINALIZA INDO PRO PROXIMO COMANDO.

#TERMO (AS TUPLAS SÃO IMUTÁVEIS)

PARTE PRÁTICA '''

#TODAS TUPLAS FICAM ENTRE PARENTESES -> ()
#TODAS LISTAS FICAM ENTRE COLCHETES -> []
#TODOS DICIONÁRIOS FICAM ENTRE CHAVES -> {}

lanche = ('hamburguer', 'suco','pizza','pudim','batata frita')  #-> no novo PY não há necessidade de parenteses para TUPLAS
#tuplas são imutáveis
#exemplo:
#lanche[1] = 'refrigerante'  #ERRO (OS objetos tipo tupla não podem ter itens assimilados)
print(lanche[1]) #Para referenciar, sempre utilizar colchetes.

#mostrando em for
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi para caramba!')

#mostrando com len

print(len(lanche)) #retorna quantos elementos há na tupla.

#mostrando for com len
for cont in range(0,len(lanche)):
#    print(cont) #retona os números das posicoes
    print(f'Eu vou comer {lanche[cont]}') #retona os lanches nas posicoes dos números

for cont in range(0,len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posicao {cont}') #retona os lanches nas posicoes dos números e as posições

#or

for pos, comida in enumerate(lanche): #incluindo mais de uma variável no for separando em virgula
    print(f'Eu vou comer {comida} e na posição {pos}')
print('Comi para caramba!')

#mostrando com sorted  = organizar
print(sorted(lanche)) #Retornará ordenado sem desconfigurar a tupla.

#exemplo 2

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b   # quando usar + nas tuplas serão "juntadas" em uma tupla só.
print(c)
print(len(c)) #retorna o tamanho ou quantidade de elementos da tupla
print(c.count(5)) #retorna quantas vezes o elemento "5" aparece na tupla
print(c.index(8)) #retorna em que posição está o elemento "8" na tupla (considerando a primeira ocorrencia)
print(c.index(5,1)) #retorna em que posição está o elemento "5" na tupla a partir da posição 1      #deslocamento#


#exemplo 3

pessoa = ('Deive', 25, 'M', 102.90) #variação de tipos de valores
#del(pessoa)  #utilizando del 'conseguimos deletar uma tupla 
#mostra erro (informando que o grupo "pessoa" não foi definido)
#del(pessoa[0])  
#mostra erro (informando que não pode deletar apenas um item da tupla)
print(pessoa)

#a tupla é imutável(entretanto pode ser deletada por inteiro durante o funcionamento do programa)