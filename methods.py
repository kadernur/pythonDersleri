import email


def selamlama():
    print("Merhaba")
    
    
selamlama()

def toplam():
    return  f'toplam: {10+20}'

a=toplam()
print(a)

def selamla(isim):
    return "Merhaba. " + isim

#fonk cağırırken gönderidiğimiz değerler argüman tanımlarken verdiğimiz ise parametredir.

#istediğimiz sayıda parametre göndermemize olanak sağlar.

def toplam(*args):
    sonuc=0
    for i in args:
        sonuc+=i
    return sonuc

# **kwargs dict veri tipindedir.args ise tuple

def displayUser(**kwargs):
    for key,value in kwargs.items():
       print(f"{key}: {value}")
    print("\n")
   
    
    
displayUser(username="sadikturan")
displayUser(username="sadikturan",email="info@sadikturan.com")
displayUser(username="sadikturan",email="info@sadikturan.com",countr="Türkiye")
