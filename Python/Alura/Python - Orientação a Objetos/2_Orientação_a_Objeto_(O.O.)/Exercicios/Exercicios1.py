'''Exercicios: Instância de uma classe'''

#Crie uma classe chamada Musica com os seguintes atributos e 
#crie 3 objetos definindo cada atributo

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