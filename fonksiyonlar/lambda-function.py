# def fonksiyon tanımlamadan gerekli işlemleri yapmamıza olanak sağlayan bir yapıdır.

def multiply(a):
    return a**2

print(multiply(4))


#sonuc=(lambda a: a**2)(4)

multiply=lambda a: a**2

sonuc=multiply(5)

toplama=lambda a,b,c: a+b+c
sonuc=toplama(1,2,5)

tersCevir=lambda s: s[::-1]
sonuc=tersCevir("kader")

print(sonuc)
