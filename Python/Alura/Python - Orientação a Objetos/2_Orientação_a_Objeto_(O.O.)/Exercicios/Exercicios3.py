'''Exercicios: Criando classes, construtores e métodos'''

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
        
    def aniversario(self):
        self.idade += 1

# Criando 3 instâncias da classe Pessoa
pessoa1 = Pessoa(nome='Deive', idade=25, profissao='Programador')
pessoa2 = Pessoa(nome='Caio', idade=20, profissao='Desenvolvedor')
pessoa3 = Pessoa(nome='Jaque', idade=22)

# Imprimindo informações iniciais
print("Informações Iniciais:")
print(pessoa1)
print(pessoa2)
print(pessoa3)
print()

# Utilizando o método de instância aniversario para aumentar a idade de uma pessoa
pessoa1.aniversario()
pessoa3.aniversario()

# Imprimindo informações após aniversário
print("Informações após aniversário:")
print(pessoa1)
print(pessoa3)
print()

# Utilizando o método de classe saudacao para exibir mensagens personalizadas
print(pessoa1.saudacao)
print(pessoa2.saudacao)
print(pessoa3.saudacao)



#1 Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular
#  e saldo. Inicie o atributo ativo como False por padrão.

class ContaBancaria:
    def __init__ (self, titular,saldo):
        self.titular = titular
        self.saldo = saldo 
        self._ativo = False  #Atributo protegido

#2 Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem 
# formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas 
# instâncias.

    def __str__(self):
        return f'O titular da conta é {self.titular} e seu saldo é de {self.saldo}'
    
conta1 = ContaBancaria(titular='Deive',saldo= 'R$ 3.000')
conta2 = ContaBancaria(titular='Deivid',saldo= 'R$ 6.000')

print('\nExibir contas:')
print(conta1)
print(conta2)

#3 Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o 
# atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima 
# o valor de ativo.

class ContaBancaria:
    def __init__ (self, titular,saldo):
        self.titular = titular
        self.saldo = saldo 
        self._ativo = False 

    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True

conta3 = ContaBancaria("Carlos", 200)
print(f"Antes de ativar: Conta ativa? {conta3._ativo}")
ContaBancaria.ativar_conta(conta3)
print(f"Depois de ativar: Conta ativa? {conta3._ativo}")


#4 Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de 
# atributos. Utilize propriedades, se necessário.

class ContaBancariaPythonica:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo

#5 Crie uma instância da classe e imprima o valor da propriedade titular.

conta4 = ContaBancariaPythonica("Alex",20000)

print(conta4.titular)

#6 Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. 
# Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método 
# construtor.

class ClienteBanco:
    def __init__(self, nome, idade, cpf, telefone, profissao):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.telefone = telefone
        self.profissao = profissao

cliente1 = ClienteBanco('Deive', 26, '321.321.321-21','11 9 9999-9999','Eletricista')
cliente2 = ClienteBanco('Davi', 22, '421.321.321-22','11 9 9999-8888','Estudante')
cliente3 = ClienteBanco('Guga', 28, '521.321.321-23','11 9 9999-2222','Barman')        

#7 Crie um método de classe para a conta ClienteBanco.

class ClienteBanco:
    # ... (outros métodos e atributos)

    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = ContaBancariaPythonica(titular, saldo_inicial)
        return conta

# Exemplo de uso do método de classe
conta_cliente1 = ClienteBanco.criar_conta("Ana", 5000)
print(f"Conta de {conta_cliente1.titular} criada com saldo inicial de R${conta_cliente1.saldo}")
