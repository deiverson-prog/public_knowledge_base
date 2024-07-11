#EX.054
#CRIE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE SETE PESSOAS. 
#NO FINAL, MOSTRE QUANTAS PESSOAS AINDA NÃO ATINGIRAM A MAIORIDADE E 
#QUANTAS JÁ SÃO MAIORES.
#CONSIDERE A MAIORIDADE 21 ANOS.

#Metodo 1
s=0
from datetime import date
atual= datetime.today().year
for c in range(1,8):
    pessoa = int(input('Pessoa {} - Digite seu ano de nascimento:'.format(c)))

#Metodo 2
from datetime import date
atual= datetime.today().year
totmaior = 0
totmenor = 0
for pessoas in range (1,8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? ').format(pessoas))
    idade = atual - nasc
    print('Essa pessoa tem {} anos'.format(idade))
    if idade >=21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmenor))