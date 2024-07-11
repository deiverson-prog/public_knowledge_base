#EX.043
#DESENVOLVA UMA LÓGICA QUE LEIA O PESO E A ALTURA DE UMA PESSOA. 
#CALCULE SEU IMC E MOSTRE SEU STATUS. DE ACORDO COM A TABELA ABAIXO:

#ABAIXO DE 18.5: ABAIXO DO PESO
#ENTRE 18.5 E 25: PESO IDEAL
#25 ATÉ 30: SOBREPESO
#30 ATÉ 40: OBESIDADE
#ACIMA DE 40: OBESIDADE MÓRBIDA

#METODO 1
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso/(altura**2)

if imc < 18.5:
    print('Seu IMC é de: {:.2f}.\nVocê está Abaixo do peso'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('Seu IMC é de: {:.2f}.\nVocê está no Peso ideal'.format(imc))
elif imc >= 25 and imc <= 30:
    print('Seu IMC é de: {:.2f}.\nVocê está com Sobrepeso'.format(imc))
elif imc >= 30 and imc <= 40:
    print('Seu IMC é de: {:.2f}.\nVocê está com Obesidade'.format(imc))
elif imc > 40:
    print('Seu IMC é de: {:.2f}.\nVocê está com Obesidade Mórbida'.format(imc))

#METODO 2
peso = float(input('Qual o seu peso? (Kg)'))
altura = float(input('Qual a sua altura? (m) '))
imc = peso/(altura**2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está Abaixo do peso normal')
elif imc >= 18.5 and imc < 25:
    print('PARABÉNS, Você está na faixa de Peso Normal')
elif imc >= 25 and imc < 30:
    print('Você está em Sobrepeso')
elif imc >= 30 and imc < 40:
    print('Você está em Obesidade')
elif imc >= 40:
    print('Você está em Obesidade Mórbida, cuidado!')

