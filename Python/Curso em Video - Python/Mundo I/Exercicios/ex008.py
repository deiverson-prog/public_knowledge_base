#Ex008
#Escreva um programa que leia um valor em metros e o exiba convertido em centimentos e milimetros.

medida = float ( input ('Insira um valor:'))
m = medida * 1
cm = medida * 100
mm = medida * 1000
print ('{:.2f}m \n{:.0f}cm \n{:.0f}mm'.format(m, cm, mm))

#outra escrita
print ('A medida de {:.2f}m corresponde a {:.0f}cm e {:.0f}mm'.format(m, cm, mm))

#continuação
medida = float ( input ('Insira um valor:'))
km = medida * 0.001
hm = medida * 0.01
dam = medida * 0.1
m = medida * 1
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print ('A medida de {:.2f}m, corresponde a: \n {:.4f}km \n {:.3f}hm \n {:.2f}dam \n {:.1f}m \n {:.0f}dm \n {:.0f}cm \n {:.0f}mm'.format(medida, km, hm, dam, m, dm, cm, mm))

#outra forma:
m= float ( input ('Insira um valor:'))
print ('A medida de {:.2f}m, corresponde a: \n {:.4f}km \n {:.3f}hm \n {:.2f}dam \n {:.1f}m \n {:.0f}dm \n {:.0f}cm \n {:.0f}mm'.format(m, (m*0.001), (m*0.01), (m*0.1), (m*1), (m*10), (m*100), (m*1000)))