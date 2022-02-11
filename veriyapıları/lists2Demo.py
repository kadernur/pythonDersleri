isimler =['Ada','Yiğit','Hasan','Beril']
yaslar=[1998,2000,1998,1987]

isimler.append('Cenk')
isimler.insert(0,'Sena')

#isimler.remove('Yiğit')

print(isimler.index('Yiğit'))

if 'Beril' in isimler:
    print('Evet')
    
isimler.reverse()
isimler.sort()

yaslar.sort()
print(yaslar)
sonuc=isimler
print(sonuc)

liste=['Iphone X', 'Iphone XR']
print(liste)

print(max(yaslar))
print(min(yaslar))

print(yaslar.count(1998))

yaslar.clear()
print(yaslar)

markalar=[]


marka=input("marka: ")
markalar.append(marka)

marka=input("marka: ")
markalar.append(marka)

marka=input("marka: ")
markalar.append(marka)

print(markalar)
