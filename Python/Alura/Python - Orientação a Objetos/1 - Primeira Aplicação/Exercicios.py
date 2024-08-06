# 1 - Imprima a frase: Python na Escola de Programação da Alura
print('Python na Escola de Programação da Alura')

#2 - Imprima a frase: Meu nome é {nome} e tenho {idade} anos em 
# que nome e idade precisam ser valores armazenados em variáveis.
n = str(input('Nome:'))
i = int(input('Idade:'))
print(f'Meu nome é {n} e tenho {i} anos')

#3 - Imprima a palavra: ‘ALURA’ de modo que cada letra fique em 
# uma linha, como mostrado a seguir: cada letra na vertical
print('''
A
L
U
R
A''') #or print('A\nL\nU\nR\nA\n')  #or print('A','L','U','R','A',sep='\n')

#4 - Imprima a frase: O valor arredondado de pi é: {pi_arredondado} 
# em que o valor de pi precisa ser armazenado em uma variável e 
# arredondado para apenas duas casas decimais. Para facilitar, 
# utilize: pi = 3.14159
pi = 3.14159

print(f'O valor arredondado de pi é: {pi:.2f}')

#or

# Utilizando a função round()
print('O valor arredondado de pi é:', round(pi, 2))

#1 - Solicite ao usuário que insira um número e, em seguida, use uma 
# estrutura if else para determinar se o número é par ou ímpar.

n = int(input('Digite um número: '))

if n % 2 == 0:
    print(f'o número {n} é PAR.')
else:
    print(f'o número {n} é IMPAR.')

#2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura 
# if elif else para classificar a idade em categorias de acordo com as 
# seguintes condições:

#Criança: 0 a 12 anos;
#Adolescente: 13 a 18 anos;
#Adulto: acima de 18 anos.

p = int(input('Qual a sua idade? '))

if p > 18:
    print(f'Você tem {p} anos e é um Adulto.')
elif p <= 12:
    print(f'Você tem {p} anos e é uma Criança.')
else:
    print(f'Você tem {p} anos e é um Adolescente.')

    #outra proposta
idade = int(input("Digite sua idade: "))
if 0 < idade <= 12:
    print("Criança")
elif 12 < idade < 18:
    print("Adolescente")
elif idade >= 18:
    print("Adulto")
else: 
    print("Valor inválido!")

#3 - Solicite um nome de usuário e uma senha e use uma estrutura 
# if else para verificar se o nome de usuário e a senha fornecidos 
# correspondem aos valores esperados determinados por você.

user_c = "DEIVAO_12"
senha_c = "deivao123"

user = input('Digite o nome de usuário: ')
senha = input('Digite a senha: ')

if user == user_c and senha == senha_c:
    print("Login bem sucedido!")
else:
    print("Credenciais inválidas. Tente novamente.")

#4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer 
# e utilize uma estrutura if elif else para determinar em qual 
# quadrante do plano cartesiano o ponto se encontra de acordo com as 
# seguintes condições:

#Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
#Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
#Terceiro Quadrante: os valores de x e y devem ser menores que zero;
#Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
#Caso contrário: o ponto está localizado no eixo ou origem.


x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

if x > 0 and y > 0:
    print("O ponto está no primeiro quadrante.")
elif x < 0 and y > 0:
    print("O ponto está no segundo quadrante.")
elif x < 0 and y < 0:
    print("O ponto está no terceiro quadrante.")
elif x > 0 and y < 0:
    print("O ponto está no quarto quadrante.")
else:
    print("O ponto está sobre um eixo ou na origem.")


#Exercicios

#1 - Crie uma lista para cada informação a seguir:
#Lista de números de 1 a 10;
#Lista com quatro nomes;
#Lista com o ano que você nasceu e o ano atual.

lista_de_numeros = [1,2,3,4,5,6,7,8,9,10]
lista_de_nomes = ['deive','daia','deivid','lucas']
lista_de_anos = [1998,2023]

#2 - Crie uma lista e utilize um loop for para 
# percorrer todos os elementos da lista.

lista_de_numeros = [1,2,3,4,5,6,7,8,9,10]
for numero in lista_de_numeros:
    print(numero)

#3 - Utilize um loop for para calcular a soma dos números
#  ímpares de 1 a 10.

soma_impares = 0
for i in range(1, 11, 2):
    soma_impares += i
print(soma_impares)

#4 - Utilize um loop for para imprimir os números de 1 a 10 
# em ordem decrescente.

for i in range(10, 0, -1):
    print(i)

#5 - Solicite ao usuário um número e, em seguida, utilize um loop 
# for para imprimir a tabuada desse número, indo de 1 a 10.

numero_tabuada = int(input("Digite um número para a tabuada: "))
for i in range(1, 11):
    resultado = numero_tabuada * i
    print(f"{numero_tabuada} x {i} = {resultado}")

#6 - Crie uma lista de números e utilize um loop for para calcular 
# a soma de todos os elementos. Utilize um bloco try-except para 
# lidar com possíveis exceções.

lista_numeros = [10, 5, 8, 3, 7]
soma = 0

try:
    for numero in lista_numeros:
        soma += numero
    print(f"Soma dos elementos: {soma}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")


#7 - Construa um código que calcule a média dos valores em uma lista. 
# Utilize um bloco try-except para lidar com a divisão por zero, 
# caso a lista esteja vazia.

lista_valores = [15, 20, 25, 30]
soma_valores = 0

try:
    for valor in lista_valores:
        soma_valores += valor
    media = soma_valores / len(lista_valores)
    print(f"Média dos valores: {media}")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")



#1 - Crie um dicionário representando informações sobre uma pessoa, 
# como nome, idade e cidade.

pessoa = {'nome': 'Deive', 'idade': 25, 'cidade': 'São Paulo'}

#2 - Utilizando o dicionário criado no item 1:
#Modifique o valor de um dos itens no dicionário 
# (por exemplo, atualize a idade da pessoa);
#Adicione um campo de profissão para essa pessoa;
#Remova um item do dicionário.

# Atualização de Idade
pessoa['idade'] = 26

# Adicionando Profissão
pessoa['profissao'] = 'Programador'

# Remoção de Elemento
del pessoa['cidade']


#3 - Crie um dicionário utilizando para representar números e seus 
# quadrados de 1 a 5.

numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)

#4 - Crie um dicionário e verifique se uma chave específica existe 
# dentro desse dicionário.

pessoa = {'nome': 'Deive', 'idade': 25, 'cidade': 'São Paulo'}
if 'nome' in pessoa:
    print("A chave 'nome' existe no dicionário.")
else:
    print("A chave 'nome' não existe no dicionário.")

#5 - Escreva um código que conte a frequência de cada palavra em uma 
# frase utilizando um dicionário.

frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)