'''Crie uma classe chamada Musica com os seguintes atributos e 
crie 3 objetos definindo cada atributo'''

class Musica:
    nome = ''
    artista = ''
    duracao = int

musica1 = Musica()
musica1.nome = 'Bohemian Rhapsody'
musica1.artista = 'Queen'
musica1.duracao = 355

musica2 = Musica()
musica2.nome = 'Imagine'
musica2.artista = 'John Lennon'
musica2.duracao = 183

musica3 = Musica()
musica3.nome = 'Shape of You'
musica3.artista = 'Ed Sheeran'
musica3.duracao = 234


class Restaurante:
    nome = ''
    categoria = ''
    ativo = False
    
restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

#1 Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da 
# classe Restaurante.

restaurante_praca.categoria = 'Italiana'

#2 Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.

nome_do_restaurante = restaurante_praca.nome


#3 Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba 
# uma mensagem informando se o restaurante está ativo ou inativo.

if restaurante_praca.ativo:
    print('O restaurante está ativo.')
else:
    print('O restaurante está inativo.')

#4 Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e 
# armazene em uma variável chamada categoria.

categoria = Restaurante.categoria

#5 Altere o valor do atributo nome para 'Bistrô'.

Restaurante.nome = 'Bistrô'

#6 Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 
# 'Pizza Place' e categoria 'Fast Food'.

restaurante_pizza = Restaurante()

restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'

#7 Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.

if restaurante_pizza.categoria == 'Fast Food':
    print('A categoria é Fast Food.')
else:
    print('A categoria não é Fast Food.')

#8 Mude o estado da instância restaurante_pizza para ativo.

restaurante_pizza.ativo = True

#9 Imprima no console o nome e a categoria da instância restaurante_praca.

print(f'Nome: {restaurante_praca.nome}, Categoria: {restaurante_praca.categoria}')


class Musica:
    def __init__(self, nome='', artista='', duracao=0):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

musica1 = Musica(nome='Under Pressure', artista='Queen & David Bowie', duracao=248)
musica2 = Musica(nome='The Trooper', artista='Iron Maiden', duracao=245)
musica3 = Musica(nome='Hotel California', artista='Eagles', duracao=390)


#1 Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. 
# Crie uma instância dessa classe e atribua valores aos seus atributos.

class Carro:
    def __init__(self, modelo='', ano=0, cor=''):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

my_car = Carro(modelo='Monza', cor='Roxo', ano=1970)

#2 Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 
# 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.

class Restaurante:
    def __init__(self, nome, categoria, ativo=False, capacidade=0, estacionamento=False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.capacidade = capacidade
        self.estacionamento = estacionamento

# Instanciando um restaurante e atribuindo valores aos seus atributos
restaurante_1 = Restaurante(nome='Comida Fast', categoria='Lanchonete', ativo=True, capacidade=30, estacionamento=True)

#3 Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como
#  parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.

class Restaurante:
    def __init__(self, nome, categoria, ativo=False, capacidade=0, estacionamento=False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.capacidade = capacidade
        self.estacionamento = estacionamento

# Instanciando um restaurante e atribuindo valores aos seus atributos
restaurante_novo = Restaurante(nome='Comida Fast', categoria='Lanchonete')

#4 Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância,
# seja exibida uma mensagem formatada com o nome e a categoria. 
# Exiba essa mensagem para uma instância de restaurante.

class Restaurante:
    def __init__(self, nome, categoria, ativo=False, capacidade=0, estacionamento=False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.capacidade = capacidade
        self.estacionamento = estacionamento

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

# Exibindo uma instância do restaurante formatada
restaurante_formatado = Restaurante(nome='Bom Sabor', categoria='Tradicional')
print(restaurante_formatado)


#5 Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos 
# desta classe e atribua valores aos seus atributos através de um método construtor.

class Cliente:
    def __init__(self, nome='', idade=0, email='', telefone=''):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone

# Instanciando três objetos da classe Cliente e atribuindo valores aos seus atributos através do construtor
cliente1 = Cliente(nome='Daia', idade=30, email='Daia@gmail.com', telefone='11-1234-1234')
cliente2 = Cliente(nome='Deivid', idade=22, email='Deividg@outlook.com', telefone='11-1122-3344')
cliente3 = Cliente(nome='Lucas', idade=21, email='Lucas@hotmail.com', telefone='11-1133-4422')

#EXEMPLO:

class Livro: #CLASSE
    def __init__(self, titulo='', autor='', paginas=0): #CARACTERISTICAS DA CLASSE 
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self): #STR PARA RETORNAR ESCRITA
        return f'{self.titulo} por {self.autor} - {self.paginas} páginas'

    @property #PROPERTY PARA ALTERAR  O TITULO E AUTOR
    def titulo_autor(self):
        return f'{self.titulo} por {self.autor}'

    def aumentar_paginas(self, quantidade): #AUMENTAR PAGINAS COMO CONTADOR
        self.paginas += quantidade # PAGINAS + NOVA QUANTIA

#Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão. 
# Adicione um método especial __str__ para imprimir uma representação em string da pessoa. 
# Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa 
# em um ano. Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de 
# saudação personalizada com base na profissão da pessoa.

class Pessoa:
    def __init__(self, nome='', idade=0 , profissao=''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'{self.nome}, {self.idade} anos, {self.profissao}'
    
    @property
    def saudacao(self):
        if self.profissao:
            return f'Olá, sou {self.nome}! Trabalho como {self.profissao}.'
        else:
            return f'Olá, sou {self.nome}!'