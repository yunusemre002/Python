# ------AÇTIPIN DOSYALARI PROGRAM SONUNDA KAPAT!!!!!--------------
# 1. Dosya var olmalı
# 2. Dosya konumum yazılmalı / slaş yönleri / böyle olmalı
# 3. open hiç parametre almazsa otomatikmen mode:"r" olmuş olur
dosya = open("C:/Users/Demir/PycharmProjects/Python_Dersleri/deneme.txt")
print(dosya)  # Dosya bilgilerini vermekte
print("Dosya1 : deneme.txt içi :\n", dosya.read())  # Dosya içeriğini okudum. .read() ile

dosya = open("deneme.txt")
print("\nDosya1 : deneme.txt içi :\n", dosya.readlines())       # Satır satır okur ve liste atar. ama \n lar da var.


# Yazma : Eğer dosya yoksa yeniden yaretır.
#         Eğer aynı isimde bir dosya varsa mevcut dosyayı SİLER yeniden yaratır.
dosya1 = open("deneme2.txt", "w")               # \nBoş bir deneme2.txt yaratıldı.")
doit = "Burada turkce karakter sikinti apti cozmek lazim"
dosya1.write(doit)                              # deneme2.txt içine yazılacaklar adlı string yazıldı.")

dosya.close()
dosya1.close()
