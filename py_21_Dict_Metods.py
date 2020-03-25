# Sözlükte sıra yoktur.
#_'copy', 'get', 'items', 'keys', 'values'...
sozluk = {  "Home" : "Ev",
            "Book" : "Kitap",
             "Pen" : "Kalem",
                12 : "on iki",
             "One" : 1,
            "computer" : "Bilgisayar"
         }

s= input("İstenilen kelimeyi giriniz : ")

# print(sozluk[s]) # olan item için çalışır olmayanitem için hata verir.
print(sozluk.get(s))    # olan item için çalışır olmayanitem için non der eğer istediğimiz şeyi
                        # Söyletmek istiyorsak
print(sozluk.get(s,"Aranan kelime bulunamadı  :( "))

# tuple halide vereir içeriği
print("\n--------İtems--------")
for i in sozluk.items():
    print(i)

#-------Keys---------")
print("\n", sozluk.keys(), sep="")

#---------Values-------")
print(sozluk.values())

# kopyalamak için = değil .copy() kullanılacak.
sozluk2 = sozluk.copy()
print("\n",sozluk2)



