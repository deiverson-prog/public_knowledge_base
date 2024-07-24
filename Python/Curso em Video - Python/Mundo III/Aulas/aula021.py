''' FUNÇÕES - part 2

TOPICOS:
- Interactive Help (Documentação organizada em PY diferenciada)
- Docstrings       (Documentação dos programas e das funções)
- Argumentos Opcionais (Funções com argumentos opcionais)
- Escopo de Variáveis  (Quando a variável nasce, morre, ou momentos que ela aparece)
- Retorno de Resultados (Retornar resultado nas funções)

                        INTERACTIVE HELP (Ajuda interativa)
Função interna 
exemplo:
help() - utilizar como manual (para sair basta digitar 'quit')

utilizar o help dentro da função para entender como pode ser utilizada
exemplo:

help(print)

podemos imprimir o doc interno do comando
exemplo:
print(input.__doc__)


                        DOCSTRINGS

def contador(i, f, p):
    """  #após incluir as aspas e dar enter um mini help é montado para preencher
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: final da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end = '')
        c += p
    print('FIM!')

contador(2, 10, 2)
help(contador)


                        PARÂMETROS OU ARGUMENTOS OPCIONAIS

def somar(a=0, b=0, c=0):   #a=0,b=0,c=0 -> quando não indicado o parâmetro é considerado opcional.
    s = a+b+c
    print(f'A soma vale {s}')

somar(3, 2, 5)


                        ESCOPO DE VARIÁVEIS

def teste():
    x = 8       #varivável X declarada na função, funciona apenas para a função (chamada escopo local)
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

#programa principal
n = 2                   #Variável N declarada no programa principal, funciona para outros parametros (chamado de escopo global)
print(f'No programa principal, n vale {n}')
teste()
print(f'No programa principal, x vale {x}')   #apresentará um erro por X ser declarado apenas na função.

Exemplo:

def teste(b):
    b += 4
    c = 2  # escopo local
    print(f'A dentro vale {a}')   #retorna o valor 5 (escopo global).
    print(f'B dentro vale {b}')   #retorna o valor 9 a soma entre 4 + 5.(escopo local).
    print(f'C dentro vale {c}')   #retorna o valor 2 (escopo local)


a = 5 #escopo global              a = 5
teste(a)                          a = b = a + b = 5 + 4

print(f'A fora vale {a}')   #retorna o valor 5 (escopo global).
print(f'B fora vale {b}')   #retorna erro (escopo local).
print(f'C fora vale {c}')   #retorna erro (escopo local).

#incluindo a variável A dentro da função:
def teste(b):
    a = 8
    b += 4
    c = 2  # escopo local
    print(f'A dentro vale {a}')   #retorna o valor 8 (escopo local).
    print(f'B dentro vale {b}')   #retorna o valor 9 a soma entre 4 + 5.(escopo local).
    print(f'C dentro vale {c}')   #retorna o valor 2 (escopo local).


a = 5 #escopo global              a = 5
teste(a)                          a = b = a + b = 5 + 4

print(f'A fora vale {a}')   #retorna o valor 5 (escopo global).
print(f'B fora vale {b}')   #retorna erro (escopo local).
print(f'C fora vale {c}')   #retorna erro (escopo local).

def funcao ():
    n1 = 4      #escopo local
    print(f'N1 dentro vale {n1}')  #retorna escopo local

n1 = 2           #escopo global
funcao()
print(f'N1 fora vale {n1}')        #retorna escopo global

#Determinando a variável A globaldentro da função:
def teste(b):
    global a                      #indicando a nova variável global
    a = 8
    b += 4
    c = 2  # escopo local
    print(f'A dentro vale {a}')   #retorna o valor 8 (escopo local).
    print(f'B dentro vale {b}')   #retorna o valor 9 a soma entre 4 + 5.(escopo local).
    print(f'C dentro vale {c}')   #retorna o valor 2 (escopo local).


a = 5 #escopo global              a = 5
teste(a)                          a = b = a + b = 5 + 4

print(f'A fora vale {a}')   #retorna o valor 8 (novo escopo global).
print(f'B fora vale {b}')   #retorna erro (escopo local).
print(f'C fora vale {c}')   #retorna erro (escopo local).


                        RETORNO DE VALORES

def somar(a=0, b=0, c=0):
    s = a+b+c
    return s                   #indicar algo antes para que ele retorne
    #print(f'A soma vale {s}')

resp = somar(3, 2, 5)          #'resp' pode ser utilizado como variável para return.
print(somar(3, 2, 5))          #funcao print pode ser utilizado para return.

r1 = somar(3, 2, 5)            #'r1' para resultado da soma
r2 = somar(2, 2)               #'r2' para resultado da soma 
r3 = somar(6)                  #'r3' para resultado da soma
print(f'Meus cálculos deram {r1}, {r2} e {r3}.') '''

''' PARTE PRATICA '''

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c 
    return f

n = int(input('Digite um número: '))
print(f'O fatoral de {n} é igual a {fatorial(n)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()

print(f'Os resultado são {f1}, {f2} e {f3}')

def Par(N=0):
    if N % 2 == 0:
        return True
    else:
        return False
        

num = int(input('Digite um número: '))
print(Par(num))
if Par(num):
    print(f'{num} é Par')
else:
    print(f'{num} não é Par')