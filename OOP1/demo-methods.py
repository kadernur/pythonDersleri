#BankAccount isminde bir sınıf tanımlayınız.
#üretilen her bir nesne owner isminde bir özelliğe sahip olmalıdırç BankAccount("Sadık Turan")
#üretilen her bir nesne balance isminde bir özelliğe sahip olup baişlangıçta 0.0 değerinde olmalıdır.
#üretilen her bir nesne için deposit metodu oluşturun ve dışarıdan yatırılacak miktar bilgisini alıp balance üzerine ekleyin ve balance miktarını geriye döndürün.
#üretilen her bir nesne için withdraw metodu oluşturun ve dışarıdan çekilecek miktar bilgisini alıp balance değerinden çıkarıp geriye döndürün.

#hesap=BankAccount("Sadık Turan")
#hesap.owner=> Sadık Turan
# hesap.balance=>0.0
#hesap.deposit(1000)=>1000.0
#hesap.withdraw(500)=>500.0

class BankAccount:
    def __init__(self,name):
        self.owner=name
        self.balance=0.0
      
    def getBalance(self):
        return self.balance
    
    def deposit(self,amount):
        self.balance+=amount
        return self.balance
    
    def  withdraw(self,amount):
        self.balance -=amount
        return self.balance
    
hesap= BankAccount("Sadık Turan")

print(hesap.getBalance())

hesap.deposit(1000)

print(hesap.getBalance())

hesap.withdraw(400)
print(hesap.getBalance())
