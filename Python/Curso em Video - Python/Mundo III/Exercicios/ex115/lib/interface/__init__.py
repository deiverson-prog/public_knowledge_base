'''Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo nome
e idade em um arquivo de texto simples. 
O sistema só vai ter 2 opções: Cadastrar uma nova pessoa e listar todas as 
pessoas cadastradas.'''

def leiaInt(msg):
    while True:
        try:
            n=int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mERRO: O usuário prefiriu não digitar esse número.\033[m')
            return 0
        else:
            return n

def linha(tam=42):
    return '-' *tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[m{c}\033[33m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc