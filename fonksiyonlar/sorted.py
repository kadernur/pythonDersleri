sayilar=[1,53,45,67,97,5,7]

#sayilar.sort()
#sonuc daki bilgiden sonra orjinal dizi değişmez.
sonuc=sorted(sayilar)

#büyükten küçüğe sıralama işlemini yapar.

sonuc=sorted(sayilar,reverse=True)


print(sayilar)



users=[
    
    {"username": "sadıkturan","tweets":["twwet1","tweet2"]},
     {"username": "cinarturan","tweets":[]},
      {"username": "sedaturan","tweets":["twwet1"],"name": "","phone":"43256556"},
    
]

sonuc=sorted(users,key=len)
sonuc=sorted(users,key=len,reverse=True)

sonuc=sorted(users,key=lambda user: user["username"])
sonuc=sorted(users,key=lambda user: len(user["tweets"]))
print(sonuc)
