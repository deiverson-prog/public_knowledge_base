#REFAÇA O DESAFIO 035 DOS TRIÂNGULOS. ACRESCENTANDO O RECURSO DE MOSTRAR QUE 
#TIPO DE TRIÂNGULO SERÁ FORMADO:

#EQUILÁTERO: TODOS OS LADOS IGUAIS
#ISÓSCELES: DOIS LADOS IGUAIS
#ESCALENO: TODOS OS LADOS DIFERENTES

#METODO 1

print('-=-' *20)
print('Analisador de Triângulos')
print('-=-' *20)

r1 = float (input('Primeiro segmento: '))
r2 = float (input('Segundo segmento: '))
r3 = float (input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR UM TRIÂNGULO', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1: 
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR UM TRIÂNGULO!')