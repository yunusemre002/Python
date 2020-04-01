import sqlite3

db = sqlite3.connect("kitaplar.sqlite")
imlec = db.cursor()

menu ="""
[1] Yazar Ara
[2] Kitap Ara
[Q] Çıkış
"""
while True:
    print(menu)
    islem = input(" İşleminiz :")

    if islem == "1":
        isim = input("Aranan yazar adı :")
        sorgu = "SELECT * FROM 'kitaplik_tablosu' WHERE yazar='{}'".format(isim)
        imlec.execute(sorgu)
        veriler = imlec.fetchall()
        for veri in veriler:
            print(veri)

    elif islem == "2":
        isim = input("Aranan kitap adı :")
        sorgu = "SELECT * FROM 'kitaplik_tablosu' WHERE kitap='{}'".format(isim)
        imlec.execute(sorgu)
        veri = imlec.fetchall()
        for i in veri:
            print(i)

    elif islem == "Q":
        quit()
    else:
        print("Yanlış bir seçim taptınız Bayım!")

db.close()