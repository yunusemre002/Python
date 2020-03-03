# Kümeler set() diye tanımlanır. İçine integer hariç herşey alır.
# Bir kümeye aynı eleman sadece bir kez eklenebilir. (a zaten varsa birdaha ekleyemezsin.)
"""
[]  List
{}  Dict
()  Tuple
""  String
10  integer
"""
kume = set() # Bos küme tanımı
kumel = set(["a","b","c","d"]) # List alır.
kumed = set({"1","2","veli","lale"}) # Dict alır.
kumet = set(("1","10","a",)) # tuple alır
kumes = set("asdasdsasdasdasd") # String alır
#kumesa = set(12) olmaz
print(type(kume), kume )
print(type(kumel),kumel)
print(type(kumed),kumed)
print(type(kumet),kumet)
print(type(kumes),kumes)


nebu = {"ali", 12, "yirmi", 25}  #Dict görünümlü ama : açıklama yok so this is küme
print(type(nebu))

#-------------------------------KUME METODLARI----------------------------------
# add, remove, discard, difference, intersect...

a = set([1,2,3,4,5])
b = set([2,3,4,5,6,7,8,9])
for i in dir(a):    # Kumenin aldığı metodlar....
    if "__" not in i:
        print(i)

print("a : ", a)
print("b : ", b)
print(30*"-")
a.add(40)
print("a : ", a)
a.discard(40)
print("a : ", a)
a.remove(5)
print("a : ", a)
a.discard(5)    # Discart ile olmayan nesneyi çıkartmaya çalışırsan sorun çıkmaz.
                # Ama remove ile yapamazsın sorun çıkartır.
print("a : ", a)

print("a/b  :", a.difference(b))
print("a kesişim b : ", a.intersection(b) )
b.difference_update(a)
print("b : ", b, "       #b.different_update(a) yapıldı.Sonuç b ")



