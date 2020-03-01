#INTEGER
x = 10
y = 5
print("5 + 10 + 1000 : ", x+y+1000)

#---------------------------------------------------------------------------
#FLOAT
a = 10.5
b  = 20.8
print("10.5 + 20.8 : ", a+b)

print(type(x)) #int
print(type(a)) #float

# / Normal bir bolumun sonucu javanin aksine floattır.
# // taban bolması yapar. 2 int isleme girerse sonuc int. Herhangi bir float
# isleme girerse sonuc float olur ama sonu hep .0 olur cunku taban bolme bu.
print()
print("10/5 : " , 10/5)
print("10//5 : " , 10//5)
print("10.8/5 : " , 10.8/5)
print("10.8//5 : " , 10.8//5)

#---------------------------------------------------------------------------
#STRING
name = "Yunus"
lname = "Demir"
x=7

print()
print(name+lname)
print(7*name) # ama x ile name toplanamaz :)
#ama 3 ü string olarak alirsak bunu name ile birlestirebiliriz.

x ="7"
print(x+name)

#---------------------------------------------------------------------------
#TIP DONUSUNLERI
print()
sayi = 7.8
print("sayi" , sayi)

int_sayi=int(sayi)
print("int(sayi) : ", int_sayi)

str_sayi = str(sayi)
print("str(sayi) : ", str_sayi)

isim = "987654"
print("int(isim)" , int(isim) )

#---------------------------------------------------------------------------
#BOOLEN
# string de 'bos' iken, sayilarda '0' iken False aksi taktirde true değerini alır.
print()
a = 10
b = -1
c = 0.0001
d = 0
print("bool(10) :  " , bool(a))
print("bool(-1) : " , bool(b))
print("bool(0.0001) : " , bool(c))
print("bool(0) : " , bool(d))

e = "laleler"
f =  ""
print("bool(laleler) : " , bool(e))
print("bool("") : " , bool(f))
