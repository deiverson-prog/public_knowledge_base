#Ex014
#Escreva um programa que converta uma temperatura digitando em 
#Graus Celsius e converta para graus Fahrenheit.

temp = float ( input ( 'informe a temperatura em °C: '))
F = (temp * 1.8) + 32 

print('A temperatura de °C {:.1f} corresponde a {:.1f} °F.'.format(temp, F))

#outra forma
#sem necessidade de parenteses por ordem de precedentes

C = float ( input ( 'informe a temperatura em °C: '))
F = 9 * C / 5 + 32 

print('A temperatura de °C {1} corresponde a {0} °F.'.format(F, C))
#usando {} com format em posições variadas.