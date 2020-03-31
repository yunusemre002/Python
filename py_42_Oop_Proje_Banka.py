
class Musteri():
    def __init__(self, ID, ISIM, PAROLA):
        self.id = ID
        self.isim = ISIM
        self.parola = PAROLA
        self.bakiye =0

class Banka():
    def __init__(self):
        self.musteriler = list()

    def musteri_ol(self, ID:str, ISIM:str, PAROLA:str):
        self.musteriler.append(Musteri(ID, ISIM, PAROLA))
        print("Bnakamıza kayıt yapıtrdığınız için tteşekkürler")


def main():
    banka = Banka()
    while True:
        print("""
        [1] Banka müşterisiyim
        [2] Banka müşterisi olmak istiyorum.
        """)

        secim = int(input("Seçiminiz :"))

        if secim == 1:                                  #  for i in banka.musteriler: ids += [i.id]
            ids = [i.id for i in banka.musteriler]      # Burada banka.müsteilerdeki tüm  müşteri id'lerini ids
                                                        # adli listeye atmış bulunduk.
            sorId = input("Lütfen müşteri Numaranızı giririniz.")
            if sorId in ids:
                for musteri in banka.musteriler:
                    if sorId == musteri.id: #müşteri bulundu.
                        print("Merhaba {}".format(musteri.isim))
                        parola = input("Parola :")
                        if parola == musteri.parola:
                            print("*******Giriş Başarılı!*******")
                            while True:
                                print("""
                                [1] Bakiye Sorgulama
                                [2] Para Yatır (Kendi hesabıma)
                                [3] Para Yatır (Başkasının hesabına)
                                [4] Para Çek
                                [Q] Çıkış
                                """)
                                secim2 = input("Seçiminiz :")

                                if secim2 == "1":
                                    print("Bakiye :{}".format(musteri.bakiye))
                                    input("Ana menüye dönmek için Entere basınız.")
                                elif secim2 == "2":
                                    yatırpara = int(input("Yatırmak istenen tutar :"))
                                    onay = input("{} TL Yatırmak istiyorsunuz doğru mu?  E/H :".format(yatırpara))
                                    if onay == "E" or "e":
                                        musteri.bakiye += yatırpara
                                        print("Para yatrma işlemi başarılı Şekilde yapılmıştır.\n Mevcut Bakiye :", musteri.bakiye)
                                        input("Ana menüye dönmek için Enter'e basınız.")
                                    elif onay == "H" or "h":
                                        print("İşlem iptal ediliyor....")
                                        input("Ana menüye dönmek için Enter'e basınız.")
                                    else:
                                        input("YANLIŞ BİR SEÇİM YAPTINIZ. \nAna menüye dönmek için Enter'e basınız.")
                                elif secim2 == "3":
                                    baskamusteriId = input("Para yatırmak istediğiniz müşterinin ID'sini giriniz :")
                                    if baskamusteriId in ids:
                                        for baskamusteri in banka.musteriler:
                                            if baskamusteriId == baskamusteri.id:
                                                bpara = int(input("Kaç para Yatırmak istiyorsunuz :"))
                                                bonay = input("{} isimli {} ID'li şahsa {} tl para yatırılacak onaylıyor musunuz?  E/H".format( baskamusteri.isim, baskamusteri.id, bpara))
                                                if bonay == "e" or "E":
                                                    if musteri.bakiye >= bpara:
                                                        baskamusteri.bakiye += bpara
                                                        musteri.bakiye -= bpara
                                                        print("Para yatırma işlemi başarıyla tamamlandı. ")
                                                        input("Ana menüye dönmek için Enter'e basınız.")
                                                    else:
                                                        print("Bakiyeniz yetersiz.")
                                                        input("Ana menüye dönmek için Enter'e basınız.")
                                                elif bonay == "h" or "H":
                                                    print("İşlem iptal ediliyor...")
                                                    input("Ana menüye dönmek için Enter'e basınız.")
                                                else:
                                                    print("Yanlış bir seçim yaptınız.")
                                                    input("Ana menüye dönmek için Enter'e basınız.")
                                    else:
                                        print("Aranan müşteri bulunamadı ID'yi doğru girdiğinizden emin olunuz.")
                                        input("Ana menüye dönmek için Enter'e basınız.")
                                elif secim2 == "4":
                                    cek = int(input("Çekmek istediğiniz parayı yazınız :"))
                                    if musteri.bakiye >= cek:
                                        musteri.bakiye -= cek
                                        input("Para çekme işlemi başarılı. \nAna menüye dönmek için Enter'e basınız.")
                                    else:
                                        print("Bakiyeniz yetersiz.")
                                        input("Ana menüye dönmek için Enter'e basınız.")
                                elif secim2 == "Q" or "q":
                                    print("Çıkış yapılıyor... ")
                                    break
                        else:
                            print("Yanlış parola.. tekrar deneyiniz.")
            else:
                print("Müşteri numaranızı yanlış girdiniz veya müşterimiz değilsiniz.Lütfen tekrar giriniz.")
                input("Ana menüye dönmek için Enter'e basınız.")
        elif secim == 2:
            ID = input("ID :")
            ISIM = input("isminiz :")
            PAROLA = input("Parola :")
            banka.musteri_ol(ID,ISIM,PAROLA)

        else:
            input("Yanlış seçiim.. \n Ana meni için entere bas")

if __name__ == "__main__":
    main()