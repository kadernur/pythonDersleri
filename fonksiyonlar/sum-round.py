sayilar=[34,2,5,7,98]

sonuc=sum(sayilar)
sonuc=sum(sayilar,10)

urunler=[
   
    {"title": "iphone x","price":5000},
    {"title": "iphone xr","price":6000},
    {"title": "iphone 11","price":7000},
]


sonuc=sum([urun["price"] for  urun in urunler])

sonuc=round(10.2)

sonuc=round(10.5)

sonuc=round(1.424242,2)

print(sonuc)