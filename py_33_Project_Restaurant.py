# Masalar br sözlük şeklinde tutulup maasalar[0] = 0. masa hesabı, masalar[1] = 1. masa hesabı şeklinde olacaktır.
# masalar{ 1 : 0,
#          2 : 0,
#          3 : 0, ...}

masalar = dict()

for i in range(10):  #Masaların hesaplarına sıfır atadım.
    masalar[i] = 0

def masaGoruntule():
    for i in range(10):
        print("Masa {} hesap :{}".format(i,masalar[i]))

def hesapEkle():
    masa = int(input("Hangi masa :"))
    ekle = float(input("Eklenecek hesap :"))
    masalar[masa] += ekle

def hesapSil():
    masa = int(input("Hangi masa :"))
    sil = float(input("Silinecek hesap :"))
    top = masalar[masa] - sil
    if top < 0:
        print("Yanlış bir işlem yaptınız (sonuç - çıkıyor)")
    else:
        masalar[masa] -= sil

def hesapKontrol(filename):
    try:
        dosya = open(filename)
        veriler = dosya.read()  # veriler dosya içinde: 45   //şeklinde alt alta bulunuyor
                                #                       100  // bunu öylece alıp veriler değiişkenine koyduk.
        veri = veriler.split("\n")     # verilerdeki veriler alt alta. So, \n ile ayırıp veriye list olarak  attık.
        veri.pop()                     # Dosyada imleç en altta. So, buradan boş bir string gelecek. pop ile onu sildim.
        dosya.close()  # Önemli! :)
        flag = True
    except FileNotFoundError:
        dosya = open(filename, "w")
        dosya.close()
        print("Belirtilen isimde bir dosya bulunmamaktadır. Yeni bir dosya yaratıldı.")
        flag = False

    if flag:
        for i, eleman in enumerate(veri):       # for index, eleman in enumerate(L)
            masalar[i] = float(eleman)            # burda for i in range(len(veri)): masalar[i] = veri[i]
                                                # de diyebilirdik. ama şaşalı olsun istedik.
    else:
        pass

def kayitGuncelle(filename):
    dosya = open(filename, "w")
    for i in range(10):
        ucret = str(masalar[i])
        dosya.write(ucret + "\n")
    dosya.close()



def main():
    hesapKontrol("kayitlar.txt")
    while True:
        print("""
        [1] Masaları Görüntüle
        [2] Hesap Ekle
        [3] Hesap  Sil
        [Q] Çıkış
        """)

        secim = input("Bir seçim yapınız :")
        if secim == '1':
            masaGoruntule()
            input("Ana menüye dönmek için Enter'a basınız.")
        elif secim == '2':
            hesapEkle()
            input("Ana menüye dönmek için Enter'a basınız.")
        elif secim == '3':
            hesapSil()
            input("Ana menüye dönmek için Enter'a basınız.")
        elif secim == 'Q':
            kayitGuncelle("kayitlar.txt")
            print("Çıkış yaplıyor.")
            exit()
        else:
            print("Yanlış bir seçim yaptınız. Lütfen tekrar seçiniz.")

        kayitGuncelle("kayitlar.txt")

main()