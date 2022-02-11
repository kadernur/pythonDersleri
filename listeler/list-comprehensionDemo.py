isimler=["Ahmet","ali","Çınar","DeNiz"]
string="Hello 12345 World"
yillar=[1983,1999,2008,1986]
dereceler=[20,5,15,-2,0,-6]

#sonuc =[ i for i in range(1,101) if  i%3==0 if i%4==0]

#sonuc=[ i.lower()[::-1] for i in isimler]

#sonuc= [i for i in string if i.isdigit()]

# import datetime

# simdi=datetime.datetime.now().year

# sonuc =[simdi-yil for yil in yillar]


sonuc=[ i if i>0 else "buzlanma tehlikesi" for i in dereceler]

print(sonuc)