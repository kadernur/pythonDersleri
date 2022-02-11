#faktoriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajlara verin.
# girilen parola içinde türkçe karakter hatası veriniz.

def faktoriyel(x):
    x=int(x)
    if(x<0):
        raise ValueError("Negatif değer")
    sonuc=1
    for i in range(1,x+1):
        sonuc*=i
        
    return sonuc


for i in [5,7,'a',2,-4 ,'10a']:
    try:
        x=faktoriyel(i)
    except ValueError as e:
     print(e)
     continue
    else:
        print(x)
        



def parolaKontrol(parola):
    turkce_karakterler="şçğüöıİ"
    
    for i in parola:
        if i in turkce_karakterler:
            raise TypeError("Parola türkçe karakterler içeremez.")
    print('geçerli parola')    
    
parola=input('parola: ')

try:
    parolaKontrol(parola)
    
except TypeError as e:
    print(e)
#import pdb
#pdb.set_trace()

#l=>list,n=>nextline,p=>print,c=>continue

