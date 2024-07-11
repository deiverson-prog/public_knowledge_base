#EX.053
#CRIE UM PROGRAMA QUE LEIA UMA FRASE QUALQUER E DIGA SE ELA É UM PALINDROMO, 
#DESCONSIDERANDO OS ESPAÇOS

#PALINDROMO - FRASE QUE SE LÊ DE TRÁS PRA FRENTE A MESMA FRASE

#EXEMPLO:
#APOS A SOPA
#A SACADA DA CASA
#A TORRE DA DERROTA
#O LOBO AMA O BOLO
#ANOTARAM A DATA DA MARATONA

#METODO 1

frase = str(input('Digite uma frase:')).strip().upper() #tira os espaços antes e depois, deixa a frase em mauscula
palavras = frase.split() #separa palavras
junto = ''.join(palavras) #junta palavras com o critério em ' '.
inverso = ''
for letra in range (len(junto) -1, -1, -1):   #len - usado para a ultima letra
    inverso += junto[letra]
if inverso == junto:
    print('Temos um Palindromo')
else:
    print('A frase digitada NÃO É um Palindromo')