# GENEL: Bir yerde : ()iki nokta varsa bir sonraki satırlar girintide yazılır.
# Bu iki nokta ifelse, fonksiyon veya döngülerden sonra olabilir.
# Tab karakteri 4 adet space tuşuna tekabül eder.

sayi = int( input("Sayi giriniz :"))
if sayi == 5:
    print("5 girildi.")
else:
    print("5 girilmedi!")

#--------------------------------------------------------
# bool(x)= false olması için string ise içi 'boş' sayi ise '0' olmasi lazım.
# Bu özelliği hata ayıklamada kullancağız.

x = input("Bir şeyler yazasana : ")

if bool(x):
    print("Girilen şey:", x)
else:
    print("Hiçbir şey girmediniz!")

#-------------------------------------------------------------
# Orta derecede hesap makinası

print("""
============================================
    [1] Toplama
    [2] Çıkarma
    [3] Çarpma
    [4] Bölme
    [5] Üs alma
    [6] Çıkış
    """)

sayi = input("islem seciniz :")

if sayi == "1":
    x = float(input("Birinci sayi:"))
    y = float(input("ikinci sayi:"))
    print("Sonuc:",x+y)

elif sayi == "2":
    x = float(input("Birinci sayi:"))
    y = float(input("ikinci sayi:"))
    print("Sonuc:",x-y)

elif sayi == "3":
    x = float(input("Birinci sayi:"))
    y = float(input("ikinci sayi:"))
    print("Sonuc:",x*y)

elif sayi == "4":
    x = float(input("Birinci sayi:"))
    y = float(input("ikinci sayi:"))
    print("Sonuc:",x/y)

elif sayi == "5":
    x = float(input("Tabanı giriniz :"))
    y = float(input("üssü giriniz :"))
    print("Sonuc:",x**y)                # 2**3=8 ** islemi üs alma islemidir.

elif sayi == "6":
    print("Cikis yapiliyor...")

else:
    print("Yanlis bir secim yaptiniz..")



