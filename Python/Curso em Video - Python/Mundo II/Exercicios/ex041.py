#A CONFEDERAÇÃO NACIONAL DE NATAÇÃO PRECISA DE UM PROGRAMA QUE LEIA O ANO 
#DE NASCIMENTO DE UM ATLETA E MOSTRE SUA CATEGORIA. DE ACORDO COM A IDADE:

#ATÉ 9 ANOS: MIRIM
#ATÉ 14 ANOS: INFANTIL
#ATÉ 19 ANOS: JUNIOR
#ATÉ 25 ANOS: SÊNIOR
#ACIMA: MASTER

#METODO 1
ano = int(input('Insera seu ano de nascimento: '))
ano_atual= 2024
idade= ano_atual-ano

if idade <= 9:
    print('Categoria: Mirim')
elif idade <=14:
    print('Categoria: Infantil')
elif idade <=19:
    print('Categoria: Junior')
elif idade <=25:
    print('Categoria: Sênior')
elif idade >25:
    print('Categoria: Master')

#METODO 2
from datetime import date
atual= datetime.today().year
nascimento = int(input('Ano de nascimento: '))
idade= atual - nascimento
print('O atleta tem {} anos'.format(idade))

if idade <= 9:
    print('Classificação: Mirim')
elif idade <=14:
    print('Classificação: Infantil')
elif idade <=19:
    print('Classificação: Junior')
elif idade <=25:
    print('Classificação: Sênior')
else:
    print('Classificação: Master')