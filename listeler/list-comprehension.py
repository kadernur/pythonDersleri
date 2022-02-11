liste=[10,4,7,9,70]


sayilar =[]

for i in range(10):
    i*=2
    sayilar.append(i)
    
#[expression for item in list]
#sayilar =[i for i in range(10)]

#sayilar=[i*2 for i in liste]

isim="Ahmet"
sonuc=[c.upper() for c in isim]

print(sonuc)