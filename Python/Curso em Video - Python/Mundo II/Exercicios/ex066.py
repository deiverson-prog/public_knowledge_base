'''Crie um programa que leia vários números inteiros pelo teclado. O programa
só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final mostre quantos números foram digitados e qual foi a soma entre deles
(desconsiderando o Flag).'''

#metodo 1
n = s = c = 0 
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    c += 1
    s += n
print(f'Foram digitado {c} números e a soma deles vale {s}.')