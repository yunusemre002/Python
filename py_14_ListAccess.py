# Birşeyin öğelerine erişirken [] notasyonu kullanılır.

list1 = ["Ali", "Mülteci", 12346, "123456", 45.79, ["asfsd", 12, 34, "Ceylan"]]
print(list1)
print("[0]. eleman   : {}".format(list1[0]))
print("[2]. eleman   : {}".format(list1[2]))
print("[-1]. eleman  : {}".format(list1[-1]))
print("[-1][0].eleman: {}".format(list1[-1][0])) # list1'in son içeiğinin(yeni list) 0. ilk elemanı
print("[-1][2].eleman: {}".format(list1[-1][2])) # list1'in son içeiğinin(yeni list) 2. ilk elemanı

print()
list2 = ["Ali", "Mülteci", 12456, "123789", 45.89, ["asdsd", 12, ["a", "b", "c"], 34,"Ceylan"]]
print(list2)
print(list2[-1])
print(list2[-1][-3])
print(list2[-1][-3][0]) # list1'in son içeiğinin(yeni list) 3. elemanı(list)

print("\nçekosyavaklaştıramadıklarımızdanmısınız?")
kelime ="çekosyavaklaştıramadıklarımızdanmısınız?"
print("1.indis: {}".format(kelime[1]))
