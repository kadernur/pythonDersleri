#iterable?


#iterator?
sayilar=[ 1,2,3,4,5]
for i in sayilar:
    print(i)
    
print(dir(sayilar))



def my_for(iterable,func):
    iterator=iter(iterable)


    while True:
     try:
        sayi=next(iterator)
        print(sayi)
     except StopIteration:
        break


my_for(sayilar,print)