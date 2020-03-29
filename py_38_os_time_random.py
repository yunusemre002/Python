import os
"""
for i in dir(os):           # os'un metodları
    if "__" not in i:
        print(i)
"""
print("os modülü")
bulundugum_dizin = os.getcwd()
print("Now you are here :", bulundugum_dizin)

print("Dizin değişti....")
os.chdir("../../../")
bulundugum_dizin = os.getcwd()
print("Now you are here :", bulundugum_dizin)

ev_dizini = os.path.expanduser("~")
print("Kullanaıcı adı(ev dizini) : ", ev_dizini)

#------------------RANDOM modülü----------------
from random import randint

rastgeleSayi = randint(10,20)
print("\nrastgele sayi : ", rastgeleSayi)

bul = input("10 ile 20 arasında  bir sayı tuttum. Bul bakalım :")
if bul == rastgeleSayi:
    print("Tebrikler")
else:
    print("HAHAHAHA yanlış cevap!")

#---------------------TIME MODULU-------------------------
import time
print("\n-----------Time modülü: ------------")
print("Bu birinci satır.")
time.sleep(2)
print("Bu ikinci satır.")

zaman1 = time.time()
print(zaman1)
time.sleep(2)
zaman2 = time.time()
print(zaman2)
print("|zaman1 - zaman2| :{}".format(zaman2-zaman1))
