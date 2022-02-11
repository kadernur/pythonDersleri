#1 -3 ürün bilgisini (id,ad,fiyat) kullanıcıdan aldığımız dictionary içinde saklayınız.
#2- ürün id bilgisini kullanıcıdan alıp ilgili ürün bilgisini gösteriniz.



# urunler={}
# id=input('id: ')
# ad=input('ad: ')
# fiyat=input('fiyat: ')

# urunler[id]={
#     "ad": ad,
#     "fiyat": fiyat
# }

# urunler={}
# id=input('id: ')
# ad=input('ad: ')
# fiyat=input('fiyat: ')

# urunler[id]={
#     "ad": ad,
#     "fiyat": fiyat
# }

# urunler={}
# id=input('id: ')
# ad=input('ad: ')
# fiyat=input('fiyat: ')

# urunler[id]={
#     "ad": ad,
#     "fiyat": fiyat
# }

#print(urunler)


players={}
id=input('oyuncu id: ')
name=input('oyuncu ad: ')
nationality=input("ülke: ")
yearOfBirth=input('doğum yılı: ')
current_team=input('takım: ')
history=input('oynadığı yerler: ')

players.update({
    id:{
        "name": name,
    
        "natianality": nationality,  
        "yearOfBirth":yearOfBirth,
        "current_team":current_team,
        "history":history.split(',')
        
        
    }
    
})


id=input('oyuncu id: ')
name=input('oyuncu ad: ')
nationality=input("ülke: ")
yearOfBirth=input('doğum yılı: ')
current_team=input('takım: ')
history=input('oynadığı yerler: ')

players.update({
    id:{
        "name": name,
    
        "natianality": nationality,  
        "yearOfBirth":yearOfBirth,
        "current_team":current_team,
        "history":history.split(',')
        
        
    }
    
})

print(players)

