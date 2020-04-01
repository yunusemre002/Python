import sqlite3

db = sqlite3.connect("kitaplar.sqlite")
imlec = db.cursor()

# Önceki kodda bir tablo oluşturmuş ve içini doldurmuştuk.
imlec.execute("SELECT * FROM 'kitaplik_tablosu'")     # Verilerei sorguladık ama daha bişi yapmadık

# veri1 = imlec.fetchone()        # Sadece ilk veriyi seçer.
# veriMany = imlec.fetchmany(2)   # 3 tane veri seçer // syı ayarlanabilir.

veriler = imlec.fetchall()        # Sorgulanan tüm verileri, veriler isimli listeye atar.
for veri in veriler:
    print(veri)

print("\n--------------WHERE yazar='Platon' olanı yazdır------------------")
imlec.execute("SELECT * FROM 'kitaplik_tablosu' WHERE yazar='Platon' ")
veriler = imlec.fetchall()        # Sorgulanan tüm verileri, veriler isimli listeye atar.
for veri in veriler:
    print(veri)

db.close()