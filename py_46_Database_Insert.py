import sqlite3

veriler =[
    ("Yılmaz Özdil", "Mustafa kemal"),
    ("Montagne", "Denemeler"),
    ("Platon", "Devlet"),
    ("Franz Kafka", "Dava"),
    ("Dostoyevski", "Budala")]


db = sqlite3.connect("kitaplar.sqlite")
imlec = db.cursor()

imlec.execute("CREATE TABLE IF NOT EXISTS 'kitaplik_tablosu' (yazar,kitap)")

for veri in veriler:
    imlec.execute("INSERT INTO 'kitaplik_tablosu' VALUES(?,?)",veri)
                        # kitap ve yazzar isimleri dict halinde bir dizide tutulurken bunları birer birer değişken
                        # olarak SQL sorgusunun içine verdik ? işaretli kısım ile.


db.commit()
db.close()