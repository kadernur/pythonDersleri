liste=["1","2","5a","10b","abc","10","50"]

for x in liste:
    
    try:
     sonuc=int(x)
     print(sonuc)
    except ValueError:
        continue

#kullanıcı quit(q) değerini girmedikçe aldığınız her inputun sayı
#emin olunuz aksi halde hata mesajı yazınız.
while True:
    sayi=input('sayi: ')
    if(sayi=='q'):
        break
    
    try:
     sonuc=float(sayi)
     print(f'girilen sayı: {sonuc}')
     break
 
    except:
        print("Geçersiz sayı")
        continue
    
    
#dictionary ve key bilgilerini parametre olarak get(d,key)
#fonk.hazırlayınız.
#d={"urunAdi" : "samsung s10"}
#d["price"]=> KeyError

#get(d,"price")=>None

urun={"urunAdi" : "samsung s10"}

def get(d,key):
    try:
        return d[key]
    except KeyError:
        return None
    
print(get(urun,'fiyat'))
print(get(urun,'urunAdi'))
