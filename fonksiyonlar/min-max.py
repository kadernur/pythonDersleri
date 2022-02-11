sayilar=[1,5,7,45,25,89]

sonuc=min(sayilar)

sonuc=max(sayilar)

isimler=["kader","helin","Sıla"]

sonuc=max(isimler,key=lambda n: len(n))

sonuc=min(isimler,key=lambda n: len(n))

urunler=[
   
    {"title": "iphone x","price":5000},
    {"title": "iphone xr","price":6000},
    {"title": "iphone 11","price":7000},
]

sonuc=min(urunler,key=lambda urun: urun['price'])['title']
print(sonuc)