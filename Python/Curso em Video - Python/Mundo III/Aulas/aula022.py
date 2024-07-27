'''MÓDULOS E PACOTES

            MODULARIZAÇÃO [CRIAR MODÚLOS]
- Surgiu no início da década de 60;
- Sistemas ficando cada vez maiores;
- Foco: dividir um programa grande;
- Foco: aumentar a legibilidade.'''

'''PARTE PRATICA'''

import Uteis022  #or        from Uteis022 import  fatorial,dobro,triplo 
num=int(input('Digite um número: '))
fat= Uteis022.fatorial(num)  #or        fat=fatorial(num) 
print(f'O fatorial de {num} é {fat}.')
print(f'O Dobro de {num} é {Uteis022.dobro(num)}.') #or        print(f'O Dobro de {num} é {dobro(num)}.')
print(f'O triplo de {num} é {Uteis022.triplo(num)}.') #or      print(f'O triplo de {num} é {triplo(num)}.')

#Basta criar um novo arquivo chamado por exemplo "Uteis022.py" (ou qualquer outro nome) para reduzir o programa

'''
            VANTAGENS
- Organização do código;
- Facilidade na manutenção;
- Ocultação do código detalhado;
- Reutilização em outros projetos.'''

'''PARTE PRATICA'''

''' JUNÇÃO DE MÓDULOS E SEPARADOS POR ASSUNTO = PACOTES 

EXEMPLO: PACOTE UTEIS:
         ASSUNTOS:  NÚMEROS:
                        A+B=C
                    STRINGS:
                        TXT
                    DATAS:
                        1998
                    CORES:
                        AZUL

Para criar um pacote basta criar uma Pasta Uteis, e subpastas para os módulos.
EXEMPLO DE CRIAÇÃO DE PASTA:
UTEIS
__init__.py
    NÚMEROS
    __init__.py
    STRINGS
    __init__.py
    DATAS
    __init__.py
    CORES
    __init__.py'''