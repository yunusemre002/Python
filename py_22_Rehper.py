# Sözlük içine sözlük kullanılmıştır. Kişi bulunamadığında string bir ifade olan bulunamadı ifadesi
# dönülüür ve stringler get parametresi almazlar dolayısıyla burası arıza verir.Bu sebeple önce kişi
# var mı diye baktı var ise işleme devam edildi. Yok ise direkt kişinin olmadığı beyan edildi.

rehper = { "kisi1" : { "ev adresi" : "Yesilova mahallesi",
                       "is adresi" : "Kemaalettin mahallesi",
                       "ev telefonu" : "0544 544 54 54",
                       "is telefonu" : "0577 755 85 85",
                       "cep telefonu" : "0570 805 88 99"
                     }
           }

isimler = rehper.keys()

def varmı(name):
    if name in isimler:
        return True
    else:
        return False

isim = input("Aradığınız kişinin ismini giriniz:")
ne = input("İlgili kişinin hangi bilgisi lazım ? ")

if varmı(isim):
    print(rehper.get(isim, "Coudnt find it!").get(ne, "!! Aranan özellik bulunmamaktadır."))
else:
    print(" Rehperde {} isimli kişi bulunmamaktadır.".format(isim))
