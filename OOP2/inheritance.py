class Person:
    def __init__(self,name,surname,age):
        print("person nesnesi türetildi.")
        self.name=name
        self.surname=surname
        self.age=age
    
    def intro(self):
        print(self.name,self.surname,self.age)
        
class Student(Person):
    def __init__(self,name,surname,age,number):
        #Person.__init__(self,name,surname,age)
        super().__init__(name,surname,age)
        self.number=number
        print("student nesnesi türetildi.")

class Teacher(Person):
    pass

p1=Person("Ahmet","Turan",20)

p1.intro()

s1=Student("Ali","Yılmaz",25,101)
print(s1.name,s1.surname,s1.age,s1.number)