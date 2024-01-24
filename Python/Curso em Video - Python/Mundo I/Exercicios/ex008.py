#Ex008
#Escreva um programa que leia um valor em metros e o exiba convertido em centimentos e milimetros.

V = float ( input ('Insira um valor:'))
M = V * 1
CM = M * 100
MM = CM * 10
print ('{:.2f} m \n{:.2f} cm\n{:.2f} mm'.format(M, CM, MM))
