# Bir sayıyı sıfıra böldüğümüzde sistem otomatikmen:"ZeroDivisionError: float division by zero" arızası verir.
    # Bu arızayı biz veritmek istiyorsak try exception yapısını kullanırız.
    # Program eğer doğru çalışacakca try bloğunu yapar.
    # Arıza alacaksa ilgili exeption bloğuna gidip oradaki işlemleri yapar.
# Genel bir exception da yazabiliriz o zaman exceptiona isim vermeyiz. ve ne arızası alırsa alsın o bloğu yapar.
# Finally bloğuna ise: işlem sonucu  ister try olsun ister exception her halükarda girilen ve yapılan bloktur.

#---------------ZeroDivisionError-------------
bolum = float(input("1. Hangi sayıyı bmleceksiniz : "))
bolen = float(input("   Böleni giriniz(0 gir) : "))

try:
    print("   Sonuç : ", bolum/bolen)
except ZeroDivisionError:
    print("Sıfıra bölemezsin bro!!!")

#---------------TypeError---------------------------------
bolum = float(input("\n2. Hangi sayıyı bmleceksiniz : "))
bolen = input("   Böleni giriniz : ")
try:
    print("   Sonuç : ", bolum/bolen)
except TypeError:
    print("İnputu floata çevir input str alır unutma!!")

#---------------ZeroDivisionError ORGINAL-----------------
bolum = float(input("\n3. Hangi sayıyı bmleceksiniz : "))
bolen = float(input("   Böleni giriniz(0 gir) : "))

try:
    print("   Sonuç : ", bolum/bolen)
except ZeroDivisionError as hata:
    print("Sıfıra bölemezsin bro!!!")
    print("Gerçek hata : \n", hata)
finally:
    print("Finally: Dikkat ben her türlü yerdeyim :)")

#------------EXCEPT------------------------------------
bolum = float(input("\n4. Hangi sayıyı bmleceksiniz : "))
bolen = input("   Böleni giriniz: ")

try:
    print("   Sonuç : ", bolum/bolen)
except:
    print("Hata oluştu ama neden ????? bilemem oldu işte genel bir yakalama bu")  # Hertürlü hatayı yakalar
finally:
    print("Finally: Dikkat ben her türlü yerdeyim :)")
