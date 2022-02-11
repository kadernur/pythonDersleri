#elimizdeki liste üzerinde belirli bir kuralı uygulamak istediğimizde map fonksiyonunu kullanabiliriz.

sayilar=[1,2,5,7,9]

kareleri=[]

for sayi in sayilar:
    kareleri.append(sayi**2)
    
print(kareleri)
    


def kareAl(sayi):
    return sayi**2
#sayilar içerisindeki her bir elemanı kareAl fonksiyonu içerisine yollar.


sonuc= list(map(kareAl,sayilar))
print(sonuc)

#fonks yerine lambda functionda kullanılabilir.
sonuc=list(map(lambda sayi : sayi**2,sayilar))
print(sonuc)

#string değerleri int cevirir.
str_sayilar=["1","2","5","7","9"]

sonuc=list(map(int,str_sayilar))
print(sonuc)

#negatifleri pozitf sayiya çevirme.

sayilar=[1,2,3,-7,6,-9]

sonuc=list(map(abs,sayilar))

sonuc=list(map(float,sayilar))

print(sonuc)
