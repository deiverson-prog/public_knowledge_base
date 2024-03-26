#CADEIA DE CARACTERES (STRINGS)
#NO PY TODA CADEIA DE TEXTOS ESTÁ SEMPRE EM ASPAS ' <- SIMPLES OU ASPAS " <- DUPLAS
#EXEMPLO: 'CURSO EM VIDEO' OU "CURSO EM VIDEO"

frase = 'Curso em Video Pyhton'

#cada caracter preenche um 'micro espaço'

#Técnicas:

#Fatiamento de String:

#O PY diferenças letras maiuculas de minusculas#

#conchetes [] - identificador de estrutura de dados chamada lista

#Utilizando a variável + [] com numero do indice, ele retorná apenas o caracter na posição numerada.
print(frase[9]) # ex: print(frase[9]) - retornará 'V'

#Utilizando a variável + [] com intervalo do indice +1 na máxima, ele retorná apenas os caracteres nas posições numeradas.
print(frase[9:13]) # ex: print(frase[9:13]) - retornará 'Vide'
print(frase[9:14]) # ex: print(frase[9:14]) - retornará 'Video'
print(frase[9:21]) # ex: print(frase[9:21]) - retornará 'Video Python'

#Utilizando a variável + [] com intervalo do indice +1 na máxima + intervalo de salto, ele retorná apenas os caracteres nas posições numeradas saltando intervalos.
print(frase[9:21:2]) # ex: print(frase[9:21:2]) - retornará 'VdoPto'

#Utilizando a variável + [] com intervalo do indice final sem indicar o indice no inicio, ele retorná os caracteres nas posições numeradas a partir de zero.
print(frase[:5]) # ex: print(frase[:5]) - retornará 'Curso'

#Utilizando a variável + [] com intervalo do indice inicial sem indicar o indice do final, ele retorná os caracteres nas posições numeradas a partir do indice indicado até o final.
print(frase[15:]) # ex: print(frase[15:]) - retornará 'Python'

#Utilizando a variável + [] com intervalo do indice inicial sem indicar o indice do final + intervalo de salto, ele retorná os caracteres nas posições numeradas a partir do indice indicado até o final, saltando intervalos.
print(frase[9::3]) # ex: print(frase[9::3]) - retornará 'VePh'


#Análise de String:

#len (length) - comprimento (quantidade de caracteres)
len(frase) # ex: len(frase) - retornará '21'

#count (count) - contar (conta strings; frases; repetições)
frase.count('o') # ex: frase.count('o') - retornará '3'
#Contando com fatiamento
frase.count('o',0,13) # ex: frase.count('o',0,13) - retornará '1' 
frase.count('o',0,14) # ex: frase.count('o',0,14) - retornará '2'

#find (find) - encontrar (procura as strings indicadas e retorna a posição de inicio)
frase.find('deo') # ex: frase.find('deo') - retornará '11'
#Quando indica uma string não existente ele retornará como '-1'
frase.find('Android') # ex: frase.find('Android') - retornará '-1'

#Cooperador
#in (procura string dentro da variável)
'Curso' in frase # ex: 'Curso' in frase - retornará 'True' (verdadeiro)
'Banana' in frase # ex: 'Curso' in frase - retornará 'False' (falso)

#Transformação de strings:

#replace (replace) - trocar/reposicionar (procura as strings indicadas e substitui)
frase.replace('Python','Android') # ex: frase.replace('Python','Android') - retornará 'Curso em Video Android'

#upper (upper) - Maiuscula (procura as strings indicadas e deixa em Maiusculo)
frase.upper() # ex: frase.upper() - retornará 'CURSO EM VIDEO PYTHON'

#lower (lower) - Minuscula (procura as strings indicadas e deixa em Minusculo)
frase.lower() # ex: frase.lower() - retornará 'curso em video python'

#capitalize (capitalize) - Capitalizado (procura as strings indicadas e deixa a primeira strings em Maiusculo)
frase.capitalize() # ex: frase.capitalize() - retornará 'Curso em video python'

#title (title) - titulo (procura as strings indicadas e deixa as primeiras strings de cada palavra em Maiusculo)
frase.title() # ex: frase.title() - retornará 'Curso Em Video Python'

#strip (strip) - faixa/espaço (procura as strings indicadas e remove os espaços a direita e a esquerda)
frase1='  Aprenda Python  '
frase1.strip() # ex: frase1.strip() - retornará 'Aprenda Python' sem espaços a direita e a esquerda

#rstrip (right strip) - faixa/espaço a direita (procura as strings indicadas e remove os espaços a direita (os ultimos))
frase1.rstrip() # ex: frase1.rstrip() - retornará '   Aprenda Python' sem espaços a direita

#lstrip (left strip) - faixa/espaço a esquerda (procura as strings indicadas e remove os espaços a esquerda (os iniciais))
frase1.lstrip() # ex: frase1.lstrip() - retornará 'Aprenda Python   ' sem espaços a esquerda

#Divisão de strings:

#split (split) dividir - (Realiza divisão dentro das strings considerando os espaços [gerando uma lista entre as palavras])
frase.split() # ex: frase.split() - retornará '[Curso] [em] [Video] [Python]' - refaz os indices

#Junção de strings:

#Join (join) - juntar (realiza a junção de todas as strings adicionando o elemento inicial indicado no script)
'-'.join(frase) # ex: '-'.join(frase) - retornará 'Curso-em-Video-Python' - junta todas as strings adicionando o elemento de sua preferência no caso o '-'.
' '.join(frase) # ex: ' '.join(frase) - retornará 'Curso em Video Python' - junta todas as strings adicionando o elemento de sua preferência no caso o ' '.


_frase = 'Curso em Video Python'

print(_frase[3])

print(_frase[3:14])

print(_frase[:14])

print(_frase[14:])

print(_frase.count('o'))

print(_frase.upper().count('O'))

print(len(_frase))

print(len(_frase.strip()))

#Apenas nessa ação
print(_frase.replace('Video','Metodos'))

#Para modificar a frase em si utilize:
_frase = _frase.replace('Video','Metodos')
print(_frase)

print('Curso' in _frase)

print(_frase.lower().find('video'))

print(_frase.split())

dividido = _frase.split()
print(dividido[2][3])

#utilize aspas triplas ''' para textos longos com quebras de linhas

print('''Não sei porque
Nosso amor não pode ser diferente
Pois sei que a gente sonha
Nosso amor pode durar para sempre
Então por que não volta
Pra que eu possa me entregar
Te sentir em minha vida
Eternamente''')