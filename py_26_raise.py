# Raise: kendi ata esajını oluşturma
# mesela ben kullanıcı 5 harici bir sayı girmesini istiyorum. Eğer 5 girerse arıza versin dersem:

sayi = float(input("5hariç bir sayi giriniz."))

if sayi == 5:
    raise Exception("5 kullanamazsın. Demiştik ama...")