'''VARIAVEIS COMPOSTAS [LISTAS]
#EXEMPLO:
LANCHE = (HAMBURGUER, SUCO, PIZZA, PUDIM)

LANCHE0 = HAMBURGUER
LANCHE1 = SUCO
LANCHE2 = PIZZA
LANCHE3 = PUDIM

LANCHE3 = PICOLÉ   -> VALE APENAS PARA SUBSTITUIR ITENS JA EXISTENTES

LANCHE = (HAMBURGUER, SUCO, PIZZA, PICOLÉ)
#LISTAS PODEM SER MUTAVÉIS.

PARA ADICIONAR NOVOS ITENS NO FINAL DA LISTA UTILIZA-SE O COMANDO 'append':

LANCHE.append('COOKIE')   -> USADO PARA ADICIONAR ITENS NO FINAL DA LISTA

LANCHE = (HAMBURGUER, SUCO, PIZZA, PICOLÉ, COOKIE)

PARA ADICIONAR NOVOS ITENS ENTRE OS EXISTENTES UTILIZA-SE O COMANDO 'insert':

LANCHE.insert(0,'HOTDOG')  -> USADO PARA ADICIONAR ITENS ENTRE OUTROS ITENS DA LISTA

LANCHE = (HOTDOG, HAMBURGUER, SUCO, PIZZA, PICOLÉ, COOKIE)

PARA APAGAR ITENS DA LISTA UTILIZA-SE O COMANDO 'del':

del LANCHE[3] -> normalmente utilizado para qualquer item.[mas deve indicar o indice ou chave]
LANCHE.pop(3) -> normalmente para eliminar o ultimo item. [mas deve indicar o indice ou chave]
LANCHE.remove('PIZZA') -> normalmente utilizado para qualquer item. [deve indicar o valor/conteúdo para ser eliminado]

LANCHE = (HOTDOG, HAMBURGUER, SUCO, PICOLÉ, COOKIE)

LANCHE.pop() -> se não indicar o indice remove o ultimo item:

LANCHE = (HOTDOG, HAMBURGUER, SUCO, PICOLÉ)

UTILIZANDO A ESTRUTURA IF e OPERADOR IN, PODEMOS VERFICAR SE O ITEM ESTA DISPONIVEL PARA REMOÇÃO:

if 'PIZZA' in LANCHE:
    LANCHE.remove('PIZZA')

CRIANDO LISTAS A PARTIR DE RANGE:

VALORES = list(range(4,11))  -> FUNÇÃO LIST, NESTE EXEMPLO INICIANDO EM 4 E FINALIZANDO E 10. EM ORDEM CRESCENTE

VALORES = [8,2,5,4,9,3,0]  -> LISTA DESORDENADA.

VALORES.sort() -> COMANDO PARA ORDENAR A LISTA EM ORDEM CRESCENTE

VALORES.sort(reverse = True) -> COMANDO PARA ORDENAR A LISTA EM ORDEM DECRESCENTE

len(VALORES) -> COMANDO PARA VERIFICAR A QUANTIDADE DE ITENS DA LISTA DE (0 A 6)'''

'''PARTE PRATICA'''

num =(2, 5, 9, 1) #->tupla
#num[2] = 3 #erro tupla imutavel
print(num)

num =[2, 5, 9, 1] #->lista
num[2] = 3 #lista mutavel
print(num)

num =[2, 5, 9, 1] 
num[2] = 3
#num[4] = 7 #erro, tentativa de adicionar valores
num.append(7) #-> forma correta de adição
num.sort() #-> retornando valores em ordem crescente
num.sort(reverse=True) #-> retornando valores em ordem decrescente
num.insert(2,2) #-> inserindo mais um valor na posição 2
num.pop() #-> removendo o último elemento
num.pop(2) #-> removendo o elemento na posição 2
num.remove(2) #-> removerá apenas a primeira ocorrência que aparecer primeiro
if 4 in num: #-> condição para evitar o erro.
    num.remove(4) #-> retornará um erro, pois o valor não está listado.
else:
    print('NÃO ACHEI O NÚMERO 4'.)
print(num)
print(f'Essa lista tem {len(num)}elementos.') #-> retorna a quantidade de elementos com o len


#EXEMPLO 2

#valores=list( ) or valores = []

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

#print(valores)

for v in valores:
    print(f'{v}...', end='') #apenas valores

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!') #chaves e valores
print('Acabou a lista!')

#or

valores = list()

for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!') #chaves e valores
print('Acabou a lista!')

#or

a = [2, 3, 4, 7]
b = a
b[2] = 8  #-> ao igualar as listas a modificação valerá para ambas.
print(f'LISTA A: {a}')
print(f'LISTA B: {b}')

#Para criar uma cópia de lista:

a = [2, 3, 4, 7]
b = a [:] #-> cópia dos itens da lista A
b[2] = 8
print(f'LISTA A: {a}')
print(f'LISTA B: {b}')
