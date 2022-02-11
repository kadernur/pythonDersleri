import random

sayi=random.randint(1,10)
can=int(input('kaç hak kullanmak istersiniz: '))
hak=can
sayac=0
while hak>0:
     hak -=1
     sayac+=1
     tahmin=int(input('tahmin'))
     
     if sayi==tahmin:
         print(f'Tebrikler{sayac}. defada bildiniz. Toplam puanınız: {100-(20)*(sayac-1)}')
         break
     elif sayi>tahmin:
         print('Yukarı')
    
     else:
         print('Aşağı')
         
     if hak==0:
         print(f'Hakkınız bitti. Tutulan sayı: {sayi}')    
