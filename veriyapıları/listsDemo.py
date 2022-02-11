from audioop import reverse


model=['Samsung S5','Samsung S6','Samsung S7','Samsung S8']

print(len(model))

print(model[0])
print(model[-1])

model[0]='Samsung S9'
print(model)

if 'Samsung S6' in model:
   print('Evet')
   
   print(model[-3])
   
   print(model[0:2])
   model[-2:]='Samsung S9','Samsung S10'
   print(model)
   
sonuc= model + ['Iphone X','Iphone XR']
print(sonuc)


del model[-1]
print(model)

sonuc=model[::-1]
print(sonuc)

for a in model:
  print(a)


ogrenciA=['Yiğit','Bilgi',2010,[70,60,70]]
ogrenciB=['Sena','Turan',1999,[80,80,70]]
ogrenciC=['Ahmet','Turan',1998,[80,70,90]]

ogrenci=[ogrenciA,ogrenciB,ogrenciC]
print(ogrenci)