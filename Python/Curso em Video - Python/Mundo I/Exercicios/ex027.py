#Ex027
#Faça um programa que leia o nome completo de uma pessoa mostrando em seguida o primeiro e 
#o último nome separadamente.

#Ex.: Ana Maria de Souza
#primeiro = Ana
#último = Souza

#METODO 1  
name = str(input('Digite seu nome: '))
primeiro = name.split()
ultimo = name.rsplit()
print(primeiro[0])
print(ultimo[2])    #sabendo o final

#METODO 2
name = str(input('Digite seu nome completo: ')).strip()
print('Muito prazer em te conhecer!')
primeiro = name.split()
ultimo = name.rsplit()
print('Seu primeiro nome é {}'.format(primeiro[0]))
print('Seu último nome é {}'.format(name[len(name)-1]))  #sem saber o final
