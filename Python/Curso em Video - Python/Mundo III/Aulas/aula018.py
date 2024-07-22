'''VARIAVEIS COMPOSTAS [LISTAS - part 2]

LISTAS DENTRO DE LISTAS

dados = ['PEDRO', '25']
pessoas = list()
pessoas.append(dados[:])  -> cópia dos dados da lista anterior

pessoas= [['PEDRO',25],['MARIA',19],['JOÃO',32]] -> DECLARAÇÃO DE 3 LISTAS EM PESSOAS

print(pessoas[0][0]) - retornará PEDRO (GRUPO 0, indice 0)

print(pessoas[1][1]) - retornará 19 (GRUPO 1, indice 1)

print(pessoas[2][0]) - retornará JOÃO (GRUPO 2, indice 0)

print(pessoas[1]) - retornará a lista inteira com colchetes ['MARIA', 19] (GRUPO 1)'''

''' PARTE PRATICA '''

'''teste = list()         #-> criando uma lista
teste.append ('Deive') #-> incluindo item na lista 'teste'
teste.append (25)   #-> incluindo item na lista 'teste'
#print(teste)        #-> escrevendo/mostrando a lista 'teste'
galera = list()     #-> criando uma nova lista
#galera.append(teste) #-> incluindo a lista 'teste' dentro da lista 'galera'
galera.append(teste[:]) #-> copiando os dados da lista 'teste' para dentro da lista 'galera'
teste[0] = 'Maria' #-> alterandando indice 0 de Deive para Maria
teste[1] = 42       #-> alterandando indice 1 de 25 para 42
galera.append(teste) #->alterando em ambas listas
galera.append(teste[:]) #->alterando a cópia da lista 'teste' para a lista 'galera'
print(galera)        #-> escrevendo/mostrando a lista 'galera''''


galera = [['João', 19], ['Ana',33], ['Joaquim',13], ['Maria',45]] #4 estruturas dentro de 1
print(galera) #mostra todas as listas 
print(galera[0]) #mostra o grupo 0 - ['João',19] 
print(galera[0][0]) #mostra o grupo 0 e o indice 0 do grupo - João
print(galera[2][1]) #mostra o grupo 2 e o indice 1 do grupo - 13
for p in galera:    #'for' para cada 'p' pessoa 'in' na 'galera' lista
   # print(p)        #mostra cada lista completa
   # print(p[0])        #para mostrar o item adicione o indice [] - neste caso os nomes no indice '0'
   # print(p[1])        #para mostrar o item adicione o indice [] - neste caso as idades no indice '1'
    print(f'{p[0]} tem {p[1]} anos de idade.')   #mostrando formatado em cada posição

galera = list() #primeira lista
dado = list()   #lista secundária (auxiliar)
totmaior = totmenor = 0 #(iniciando o contador zerado)
for c in range(0,5):    #'for' para cada 'c' contagem 'in' no 'range' critério (0,5) - de 0 a 5 (desconsiderando o '5')
    dado.append(str(input('Nome: '))) #adicione 'escrevendo' na lista 'dado' o nome 5x
    dado.append(int(input('Idade: '))) #adicione 'escrevendo' na lista 'dado' a idade 5x
    galera.append(dado[:]) #levando uma cópia dos itens da lista 'dado' para a lista 'galera'
   #galera.append(dado) #levando os itens da lista 'dado' para a lista 'galera' (ressaltando que no item abaixo a lista 
                        #será apagada, sendo assim não levará valor nenhum)
    dado.clear() #limpando a lista 'dado'

for p in galera:    #'for' para cada 'p' pessoas 'in' na 'galera' lista
    if p[1] >= 21:      # 'if' se 'p[1]' a idade da pessoa na lista for maior ou igual a 21
        print(f'{p[0]} é maior de idade.') #retornará o nome da pessoa que é maior de 21 
        totmaior +=1    #soma quantas pessoas são maior de idade
    else:                   #se não for maior ou igual a 21
        print(f'{p[0]} é menor de idade.')  #retornará o nome da pessoa que é menor de 21 
        totmenor +=1    #soma quantas pessoas são menor de idade

print(f'Temos {totmaior} pessoas maiores de idade & {totmenor} menores de idade.')
print(galera) #mostrará a cópia dos itens da lista 'dado' antes de ser limpa
print(dado) #mostrará a lista 'dado' limpa (sem itens)