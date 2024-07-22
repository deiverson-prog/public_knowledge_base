'''VARIAVEIS COMPOSTAS [DICIONÁRIOS - part 1]

DADOS = LIST()
DADOS.APPEND('PEDRO') ->ADDLISTDADOS
DADOS.APPEND(25) ->ADDLISTDADOS
PRINT(DADOS[0]) ->PEDRO
PRINT(DADOS[1]) ->25

TUPLAS ()
LISTAS []
DICIONÁRIOS {}

EXEMPLO: DADOS
            'Pedro' 25
            nome    idade

DADOS=DICT('nome':'Pedro','idade':25) OU 
DADOS={'nome':'Pedro','idade':25}
print(DADOS['nome'])  -> Pedro
print(DADOS['idade']) -> 25
DADOS['sexo']='M'     ->ADD DICIONÁRIO
delDADOS['idade']     -> REMOVE

filme = {'titulo':'Star Wars',
         'ano':1977,
         'diretor':'George Lucas'}   

EM PY SÃO CHAMADAS DE KEYS = ELEMENTOS

VALOR (values) 
CHAVE (key)
ITEM  (items)

print(filme.values())   -> retorna o valor dentro das chaves
    Star Wars, 1977, George Lucas
print(filme.keys())     -> retorna o conjunto de valores das chaves
    titulo, ano, diretor
print(filme.items())    -> retorna todos os valores e chaves
    'titulo':'Star Wars','ano':1977,'diretor':'George Lucas'

for k, v in filme.items():
    print(f'O {k} é {v}')
    #retornará: O titulo é Star Wars
    #retornará: O ano é 1977
    #retornará: O diretor é George Lucas

Locadora
| 'Star Wars' | 1997 | 'George Lucas' | | 'Avengers' | 2012 | 'Joss Whedon' | | 'Matrix' | 1999 | 'Wachowski' |
    titulo       ano       diretor          titulo      ano       diretor        titulo      ano     diretor    
                    0                                      1                                   2                
print(Locadora[0]['ano'])  ->retornará 1977
    1977
print(Locadora[2]['titulo'])  ->retornará Matrix
    Matrix'''

''' PARTE PRATICA '''

pessoas = {'nome':'Deive','sexo':'M','idade':25}
print(pessoas) # Retornará {'nome':'Deive','sexo':'M','idade':25}
print(pessoas['nome']) # Retornará Deive
print(pessoas['idade']) # Retornará 25
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.') #Usar aspas duplas dentro de aspas simples para referenciar
    # Retornará O Deive tem 25 anos.
print(pessoas.keys())   # Retornará dict_keys(['nome', 'sexo' , 'idade'])
print(pessoas.values())   # Retornará dict_values(['Deive', 'M' , '25'])
print(pessoas.items())  # Retornará dict_keys([('nome','Deive'), ('sexo' ,'M'), ('idade', 25)])

#Acessando por laços

for k in pessoas.keys():
    print(k) # Retornará nome sexo idade

for k in pessoas.values():
    print(k) # Retornará Deive M 25

for k, v in pessoas.items():  #pode ser usado no lugar do enumerate(o enumerate é usado apenas em tuplas e listas)
    print(f'{k} = {v}') # Retornará nome = Deive sexo = M idade = 25

del pessoas['sexo'] #chave e valores de sexo serão deletados
for k, v in pessoas.items():  
    print(f'{k} = {v}') # Retornará nome = Deive idade = 25 

pessoas['nome'] = 'Deivid' #trocando o valor da chave 'nome' de Deive para Deivid
for k, v in pessoas.items():  
    print(f'{k} = {v}') # Retornará nome = Deivid idade = 25 

pessoas['peso'] = 98.5 #adicionando a chave 'peso' com valor 98.5
for k, v in pessoas.items():  
    print(f'{k} = {v}') # Retornará nome = Deivid idade = 25 

#Criando um dicionário dentro de uma lista


brasil = [] #lista criada
estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'} #dicionario1 criado
estado2 = {'uf':'São Paulo', 'sigla':'SP'}      #dicionario2 criado
brasil.append(estado1) #dicionario1 adicionado na lista
brasil.append(estado2) #dicionario1 adicionado na lista
print(estado1)         #exibe o dicionario do RJ
    #{'uf':'Rio de Janeiro', 'sigla':'RJ'}
print(estado2)         #exibe o dicionario do SP
    #{'uf':'São Paulo', 'sigla':'SP'}
print(brasil)          #exibe os dois dicionarios dentro da lista
    #[{'uf':'Rio de Janeiro', 'sigla':'RJ'}, {'uf':'São Paulo', 'sigla':'SP'}]
print(brasil[0])       #exibe o dicionario do RJ dentro da lista no indice 0
    #{'uf':'Rio de Janeiro', 'sigla':'RJ'}
print(brasil[0]['uf']) #exibe a UF Rio de Janeiro dentro da lista no indice 0
    #Rio de Janeiro
print(brasil[1]['sigla']) #exibe a SIGLA SP dentro da lista no indice 1
    #SP

estado = dict()
brasil = list()

for c in range(0,3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['SIGLA'] = str(input('Sigla do Estado: '))
    #brasil.append (estado[:]) #não é permitido realizar fatiamento em dicionários
    brasil.append (estado.copy()) #para realizar cópia de dicionário utilizar metodo interno .copy()
print(brasil)
for e in brasil:
    print(e) #mostrará as listas
    for k, v in e.items():
        print(f'O Campo {k} tem valores {v}') #or
    for v in e.values():
        print(v, end=' ')
    print()