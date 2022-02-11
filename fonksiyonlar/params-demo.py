#kendisine gönderilen 2 sayıdan hangisi büyük bulan fonksiyonu yazınız.
# kendisine gönderilen bir stringi bilgi içinde her karakter kaçar kez tekrarlanmış bulunuz.
# kenndisne gönderilen list,command.position ve value bligilerine göre liste üzerinde güncelleme yapınız.
# [1,2,3],("add, remove"),("beginning | end"),value
#list_operation([1,2,3],"remove","beginning")=>[2,3]
#kendisine gönderilen renk isimlerinden içinde "blue"rengi varsa True döndüren fonksiyonu yazınız.

def karsilastirma( a,b):
    if(a>b):
        return "a b den büyüktür."
    elif(a<b):
        return "a b den küçüktür"
    else:
        return"iki sayi eşittir."


sonuc=karsilastirma(a=8,b=3)

def karakterSayisiniBul(string):
    return {letter:string.count(letter) for letter in string}


sonuc=karakterSayisiniBul("kkaaadeerrr")
    
    
def updateList(liste,command,position, value=None):
    if(command=="remove"and position=="end"):
        return liste.pop()
    elif(command=="remove" and position =="beginning"):
        return liste.pop(0)
    elif(command=="add" and position=="end"):
         liste.append(value)
         return liste
    elif(command=="add", position=="beginning"):
        liste.insert(0,value)
        return liste
    
sonuc=updateList([1,2,3],"update","beginning",5)

    
 
 
def containBlue(*args):
    if "blue" in args:
        return True
    return False   

sonuc=containBlue( "yellow" ,"red")
    
print(sonuc)
        
      
    