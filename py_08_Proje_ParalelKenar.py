# Dikkat sadece Çift sayilarda çalışır.

def sagSlas(adet):
    for i in range(int(adet)):
        print("/", end="")

def solSlas(adet):
    for i in range(int(adet)):
        print("\\", end="")

def space(adet):
    for i in range(int(adet)):
        print(" ", end="")

def altaSatir(adet):
    for i in range(int(adet)):
        print()

def ustKisim(cap):
    baslangicBosluk = cap/2-1
    for i in range(int(cap/2)):
        space(baslangicBosluk-i)
        sagSlas(1)
        space(i*2)
        solSlas(1)
        altaSatir(1)

def altKisim(cap):
    baslangicBosluk= cap-2
    for i in range(int(cap/2)):
        space(i)
        solSlas(1)
        space(baslangicBosluk - i*2)
        sagSlas(1)
        altaSatir(1)

def paralelKenar(cap):
    ustKisim(cap)
    altKisim(cap)


paralelKenar(10)

"""Paralel kenarın ortası çap olarak alınırsa yukarı kadar okadar çap kadar satır aşağı kadar çap kadar atır ilerlemeli
Başlangıç boşluğu çap/2-1 kere olmalı.
"""