'''Crie uma programa que tenha uma função fatorial() que receba dois paramêtros:
o primeiro que indique número a calcular e o outro chamado show, que será um 
valor lógico(opcional) indicado se será mostrado ou não na tela o processo de
cálculo do fatorial.''' 


def fatorial(a, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param a: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número a.
    """

    f = 1
    for c in range(a, 0, -1):
        if show == True:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c 
    return f

n = int(input('Digite um número: '))
print(f'O fatoral de {n} é igual a {fatorial(n)}')

print(fatorial(5, show=True)) #or 
print(fatorial(5)) #or
print(fatorial(5, show=False))
help(fatorial)