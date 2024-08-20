'''Exercicios: Métodos especiais e atributos'''

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
