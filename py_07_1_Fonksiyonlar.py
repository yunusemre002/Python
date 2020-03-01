
#---------------Topla Fonksiyonu----------------------
def topla(x, y):
    top=x+y
    return top

print("3 + 5 = ", topla(3, 5))
print("333 + 5555 = ", topla(333, 5555))
print("333 + 777 = ", topla(333, 777))


#--------------Dİk Üçgen Fonksiyonu-------------------
def dikucgen(a, b, hipotenus):
    if a**2 + b**2 == hipotenus**2:
        return "bir Dik Ucgendir."
    else:
        return "Dik Ucgen değildir!"

print("\n3 4 ve 5 üçgeni ", dikucgen(3,4,5))
print("5 6 ve 7 üçgeni ", dikucgen(5,6,7))