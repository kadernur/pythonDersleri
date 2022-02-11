kelime=' Hello World '
sonuc= kelime.strip()
print(sonuc)

kelime='www.sadikturan.com'
sonuc=kelime.strip('w.moc')
kelime='kursAdi'
sonuc=kelime.lower()

kelime='kaaaaader'
sonuc=kelime.count('a')

kelime="www.sadıkturan.com"
sonuc=kelime.startswith('www')
sonuc=kelime.endswith('com')
sonuc=kelime.find('.com')
sonuc=kelime.find('.com',0,10)
kelime='kadier'
sonuc=kelime.isalpha()
sonuc=kelime.isdigit()

kelime='Contents'
sonuc=kelime.center(50,'*')
kelime='kursAdi kader nur tekin'
sonuc=kelime.replace(' ','-')

kelime='Hello World'
sonuc=kelime.replace('World','There')

kelime='kursAdi kader nur tekin'
sonuc=kelime.replace(' ','-')
sonuc=kelime.split()

print(sonuc)