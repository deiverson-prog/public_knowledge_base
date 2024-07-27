'''Adapte o código do desafio #107, criando uma função adicional chamada 
moeda() que consiga mostrar os números como um valor monetário formatado.'''

from moeda import metade,moeda,diminuir, aumentar, dobro

P = float(input('Digite o preço: '))
a = 10
print(f'A metade de {moeda(P)} é {moeda(metade(P))}')
print(f'A Dobro de {moeda(P)} é {moeda(dobro(P))}')
print(f'Ao Aumentar 10% no valor, temos {moeda(aumentar(P,a))}')
print(f'Ao Diminuir 10% no valor, temos {moeda(diminuir(P,a))}')