'''Crie um programa que tenha a função leiaInt(), que vai funcionar de forma
semelhante à função input() do Python, só que fazendo a validação para aceitar
apenas um valor numérico.
Ex.:
N = leiaInt('Digite um n')'''

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor

#n = int(input('Digite um número: '))   #essa é a idéia
n = leiaInt('Digite um número: ')       #essa é a nova função    
print(f'Você digitou o número {n}')