#1 METODO
'''class Restaurante:
    nome = ''
    categoria = ''
    ativo = False
    
restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

restaurante_pizza = Restaurante()

restaurantes = [restaurante_praca, restaurante_pizza]

print(dir(restaurante_praca)) #Mostra todos  os métodos da classe e como ela funciona.
#mostrará tudo: os atributos, métodos e propriedades de um objeto.

print(vars(restaurante_praca))
#mostrará um dicionário desses atributos e métodos.

'''
#2 METODO

from Modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):  
        self._nome = nome.title()                  
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
        
    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} |{'Status'}')
       #ao alterar para @classmethod conseguimos substiruir o nome da Classe por cls.
       #for restaurante in Restaurante.restaurantes:
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} |{restaurante.ativo}')  #separados por pip -> | 
       #Transformando a media de avaliaçoes um valor "float" em "str" para exibição

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5: 
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
    
# Função "sum" + "for" para somar cada nota avaliada para cada restaurante 
# Função "len" para informar o tamanho ou quantidade
# Função "round" para arredondar valores 
# Função "__init__" um método construtor, que é sempre chamado quando criamos uma instância de um objeto.
# Parâmetro "self" : o self como primeiro parâmetro, trata daquele objeto (instancia) que estamos referenciando naquele momento.
# Podemos utilizar o "this" ou "objeto" ao invés de "self".
# Ctrl + f para procurar e substituir "replace"
# Função "@property" tem o poder para modificar como aquele atributo vai ser lido através de uma função.
# F2 para renomear o parâmento em todos os campos que ele for conectado.

#metodos de apresentação
restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.alternar_estado() 
restaurante_pizza = Restaurante('pizza express', 'Italiana')

Restaurante.listar_restaurantes()