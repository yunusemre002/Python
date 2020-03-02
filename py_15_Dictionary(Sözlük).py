# Anahtar değer ilişkisi vardır. Bir sıralaması yok! İndex no'su yok dolayısıyla
# [0] vs. diyerek erişim sağlayamayız. Erişimi anahtar vererek sağlarız değeri
# alırız. İki şekilde tanımlama mümkündür. Aşağıdaki gibi
# sozluk = dict()
# sozluk = {}

sozluk = {  "Home" : "Ev",
            "Book" : "Kitap",
             "Pen" : "Kalem",
                12 : "on iki",
             "One" : 1
         }
print(sozluk) #denildiğinde sıralamanın her defadında değiştiği görülmektedir.
print(sozluk["Home"])
print(sozluk["Pen"])
print(sozluk[12])
print()

#-----------------------VURULMA OYUNU-------------------------------
karakter1 = {   "Ad"    : "Yunus Emre",
                "Güç"   : 100,
                "Silah" : "G3",
                "Can"   :  100
            }

karakter2 = {   "Ad"    : "Said",
                "Güç"   : 70,
                "Silah" : "G3",
                "Can"   :  100
            }

def vur(vuran:dict, vurulan:dict):
    silinecek = vuran["Güç"]
    vurulan["Can"] -= silinecek

def yazdir(person:dict):
    print("\nKarakter Adı   : {}".format(person["Ad"]))
    print("Karakter Gücü  : {}".format(person["Güç"]))
    print("Karakter Silahı: {}".format(person["Silah"]))
    print("Karakter Canı  : {}".format(person["Can"]))

yazdir(karakter1)
yazdir(karakter2)
vur(karakter1, karakter2)
vur(karakter2, karakter1)
print("\n-------İkiside Vurulduktan Sonra---------")
yazdir(karakter1)
yazdir(karakter2)


