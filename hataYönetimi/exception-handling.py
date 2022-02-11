while True:
    try:
        x=int(input('x: '))
        y=int(input('y: '))
        print(x/y)
    except(ZeroDivisionError,ValueError) as e:
        print('hata oluştu.')
    except Exception as e:
        print('bilinmeyen bir hata oluştu.')
        print(e)
        
    else:
        break
    finally:
        print("Finally bloğu çalıştı.")