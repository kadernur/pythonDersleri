benzinFiyat=6.69
dizelFiyat=5.86
ortalamaYakıtTuketimi= float(input('100 km deki ortalama yakıt tüketimi: '))
gidilecekYol=float(input('gidilecek yol kaç km: '))
yakitTipi= input('yakıt tipiniz nedir: ')
toplamYakitTuketimi= gidilecekYol * (ortalamaYakıtTuketimi/100)

if(yakitTipi=='benzin'):
 toplamYakıtUcreti= benzinFiyat * toplamYakitTuketimi
 
else:
 toplamYakıtUcreti=dizelFiyat*toplamYakitTuketimi

print(toplamYakıtUcreti)