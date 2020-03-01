
print(5+7)
print(5-7)
print(5*7)
print(5/7)

# Stringlerde + ve * işlemi yapılabilir.
print("abc" + "def")
print("3" + "def")
print(3 * "def")    # 3 kere def yaz.

print("2'5 :", 2**5)
print("Normal bölme :", 5/2)
print("Taban bölme :", 5//2)
print("Taban bölme :", 5.9//2.1) # Taban bölmede önce işlem yapılır sonuçtan küsürat silinip 0 Yazılır .
                                 # Yuvarlama işlemi değil yani (Üste yuvarlaaylım)

#Mod işmeli ½ kalanı verir. 10%2=0, mod=0 yani
x = input("Bir sayi giriniz...")
print("x=", x, " iken : ")

if int(x) % 2 == 0: # Neden x i inte cast ettik çünkü input'tan gelen değer Stringdir.
    print("   ", x, " çift bir sayıdır.")
else:
    print("   ",x, " tek bir sayidir.")
#----------------------------------------------------------------------

p = input("Parolayı giriniz.")
parola = "123456"
if p==parola:
    print("    Parola Doğru")
elif p!=parola:
    print("    Parola Yanlış!")

sayi = input("Notunuzu giriniz.")
sayi = int(sayi)
if sayi >=90:
    print("     AA aldiniz.")
elif sayi >=40:
    print("     DC aldiniz.")
else:
    print("     Kaldiniz.")

# and, or, not direkt boyle kullanıyoruz..
x = int(input("Birinci sayi giriniz.."))
y = int(input("İkinci sayiyi giriniz.."))
if x==5 and y==5:
    print("X ve Y 5 tir.")
elif x>=20 or x<=10:
    print("Birinci sayi 10'dan küçük veya 20 dan büyüktür.")

bos = input("Enter diyiniz(Bos karakter yani)")
if not bool(bos): # null sa false olmalı notladık true oldu
    print("        True Bos bir karakter girdiniz")




