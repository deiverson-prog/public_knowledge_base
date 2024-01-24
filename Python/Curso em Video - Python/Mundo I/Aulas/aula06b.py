#numero inteiro
n = int(input('digite um valor:'))
print(n)

#numero decimal
n = float(input('digite um valor:'))
print(n)

#verdadeiro ou falso
n = bool(input('digite um valor:'))
print(n)

#caracters
n = str(input('digite um valor:'))
print(n)

#verificando tipo primitivo
n = float(input('digite um valor:'))
print(type(n))

#verificando se é possivel a conversão (numero)
n = input('digite algo:')
print(n.isnumeric())

#verificando se é possivel a conversão (letra)
n = input('digite algo:')
print(n.isalpha())

#verificando se é possivel a conversão (letra&numero)
n = input('digite algo:')
print(n.isalnum())

#verificando se é possivel a conversão (somente letras maiusculas)
n = input('digite algo:')
print(n.isupper())

#verificando se é possivel a conversão (somente letras minusculas)
n = input('digite algo:')
print(n.islower())

#verificando se é possivel a conversão (se pode ser impresso)
n = input('digite algo:')
print(n.isprintable())

