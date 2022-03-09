class Product:
    def __init__(self,name,price):
        self.name=name
        if price>=0:
         self._price=price
        else:
            raise ValueError("ürün fiyatı için negatif değer ataması yapılamaz")
    @property   
    def price(self):
        return self._price

    @price.setter
    def price(self,value):
        if value>=0:
             self._price=value
        else:
            raise ValueError("ürün fiyatı için negatif değer ataması yapılamaz")
     
        
    # def set_price(self,value):
    #         pass
        
        
    # def get_price(self):
    #         return self._price
        
p=Product("iphone",9000)
#print(p.get_price())   

p.price=-9000
print(p.price)   