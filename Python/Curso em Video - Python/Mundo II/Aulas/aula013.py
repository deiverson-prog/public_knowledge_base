#Aula 13 – Estrutura de repetição for

#Estruturas de controle 
#Laço, repetições, Iteração

#Laço

#For

#CRIAR COMANDOS
#ALGORITIMO - DETERMINAR O LIMITE
#PASSO, PASSO, PASSO, PASSO, PASSO E PEGA

#LAÇO COM VARIAVEL DE CONTROLE

#LAÇO_C_NO_INVERVALOR(1.10)   -> NO "C" POSSO ESCOLHER O QUE QUISER
    #PASSO     <- IDENTADO
#PEGAR

#EXEMPLO1: for c in range(1.10)
            #passo
         #pegar

#COMANDOS PASSO E PULA 3X + 1X PASSO PEGA
#for c in range (0,3)
#   passo
#   pula
#passo
#pega

#COMANDOS PASSO, PULA, PEGA 2X, 
#           PASSO, PULA + 1X PASSO PEGA
#for c in range (0,3)
#   if (moeda):
#     pega  
#   passo
#   pula
#passo
#pega

#PRATICANDO
for c in range(0,6):   #---> não considera o ultimo digito (para no último)
    Print('OLÁ')
print('Fim')

for c in range(0,7):   #---> não considera o ultimo digito (para no último)
    Print(c)            #---> será considerada a contagem de 0 a 6.
print('Fim')

for c in range(6,0):   
    Print(c)            #---> Não será executado, até aderir a iteração.
print('Fim')

for c in range(6,0,-1): #---> iteração adicionada (subtraindo) 
    Print(c)            
print('Fim')

for c in range(0,7,2): #---> iteração adicionada  (saltando de 2 em 2)
    Print(c)            
print('Fim')

#TESTE

n = int(input('Digite um número: '))
for c in range(0,n+1):
    print(c)
print ('FIM')

i = int(input('ínicio: '))  #inicio
f = int(input('fim: '))     #limite
p = int(input('passo: '))   #"critério"
for c in range(i, f+1, p):
    print(c)
print ('FIM')

for c in range (0, 3):
    n = int(input('Digite um valor: ')) #---> repete 3x o mesmo comando
print('fim')

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n #or s = s+n
print ('O somatório de todos os valores é igual a {}'.format(s))
