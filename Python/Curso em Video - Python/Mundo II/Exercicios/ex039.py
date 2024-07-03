#FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME. 
#DE ACORDO COM SUA IDADE:

#SE ELE AINDA VAI SE ALISTAR NO SERVIÇO MILITAR
#SE É A HORA DE SE ALISTAR
#SE JA PASSOU DO TEMPO DO ALISTAMENTO

#SEU PROGRAMA TAMBÉM DEVERÁ MOSTRAR O TEMPO QUE FALTA OU QUE PASSOU DO PRAZO.

#METODO 1

ano = int(input('Qual seu ano de nascimento? '))
ano_atual = 2024

if ano_atual-ano == 18:
    print('Hora de se alistar no Serviço Militar!')
elif ano_atual-ano < 18:
    print('Ainda não está no periodo de alistamento! \nfalta(m) {:.0f} ano(s)'.format((18-(ano_atual-ano))))
elif ano_atual-ano > 18:
    print('Você está {:.0f} ano(s) fora do periodo de alistamento! \nRegulariza-se com a Junta Militar!'.format(((ano_atual-ano)-18)))

#METODO 2

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade= atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade,atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))

