#liste içerisndeki elemanları filtrelemek istersek filter fonksiyonunu kullanırız.
from operator import index


yaslar=[5,12,18,24,45]

def yetiskinMi(x):
    if x<18:
        return False
    else:
        return True

for i in filter(yetiskinMi,yaslar):
    print(i)

#yukarıdaki işlemlerle aynı işlemleri yapar.    
sonuc=list(filter(yetiskinMi,yaslar))

sonuc=list(filter(lambda x: x>=18,yaslar))

sayilar=[0,5,2,4,6]

sonuc=list(filter(lambda x: x%2==0,sayilar))

#a ile başlayan isimleri döndür.

isimler=["ada", "helin","ali","sena"]

sonuc=list(filter(lambda n: n[0]=='a', isimler))

sonuc=list(map(lambda n: n.upper(),filter(lambda n: n[0]=='a',isimler)))

print(sonuc)
 
