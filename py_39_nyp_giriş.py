# Class ismi büyük harf ile başlar.

class Siparis():
    firma = ''
    miktar = 0
    tarih = ''

gofret = Siparis()
gofret.firma = "Ülker"
gofret.miktar = 20
gofret.tarih = "29.03.2020"

kitap = Siparis()
kitap.firma = "Kırmızı kedi"
kitap.miktar = 5
kitap.tarih = "29.03.2020"

print(gofret.firma)
print(gofret.miktar)
print(gofret.tarih)
print()

print(kitap.firma)
print(kitap.miktar)
print(kitap.tarih)

"""
Ctrl + Alt + L = Yazılan tüm kodu biçimlendirir
Ctrl + Shift + F10 = Yazılan kodu çalıştırır
Ctrl + X = Bulunan satırı keser
Ctrl + D = Bulunan satırın aynısını bir alt satıra kopyalar
"""