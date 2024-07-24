'''Crie um programa que tenha uma função chamada voto() que vai receber como
parâmetro o ano de nascimento de uma pessoa, retornando um valor literal 
indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.'''

from datetime import datetime
def voto(a):
    atual = datetime.now().year
    idade =  atual - ano

ano = int(input('Ano de Nascimento: '))

print(voto(ano))