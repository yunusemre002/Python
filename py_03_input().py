# İnput fonksiyonu yalnızca bir parametre alır. print ise 256 parametre alabilir.
# Girdi almak için kullanılır. Kullanıcıdan alınan her değer STRING biciminde alinir.
# Bu yüzden sayı aldığınızda kullanmadan önce integere cast etmemiz lazım.

isim = input("İsminiz : ")
print("Merhaba", isim)

#------------------------------------------------------------------------------------
sayi = input("Bir sayi giriniz : ")
print(sayi, "+ 5 =", ( int(sayi) + 5 )) # aslinda input olarak sayi girildi ama input fonk. tüm
                                        # girdileri string olarak alır bu yuzden int'e cast edildi.

#---------------------------------------------------------------------------------
print()
sayi1 = float( input("Birinci sayi :"))
sayi2 = float( input("İkinci sayi :"))

print("----------------------------------------")
print(sayi1, "+", sayi2, "=", sayi1+sayi2)
print(sayi1, "-", sayi2, "=", sayi1-sayi2)
print(sayi1, "*", sayi2, "=", sayi1*sayi2)
print(sayi1, "/", sayi2, "=", sayi1/sayi2)
print("----------------------------------------")