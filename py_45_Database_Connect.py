import sqlite3

db = sqlite3.connect("kitaplar.sqlite")                          # Yoksa yaratır. Varsa açar.

imlec = db.cursor()                                              # Sqlite3 Database içinde bir imleç yarattık.
imlec.execute("CREATE TABLE IF NOT EXISTS kitaplik (yazar,kitap)")             # Normal SQL Sorguları yarattık.
                            # Bunları görmek için önce SQlite yi indirdim pc ye sonra açtım baktım gerçekten yaratmış.
                            # IF NOT EXISTS yazmazsak aynı kodu 2. ye çalıştırdığımızda mevcut isimde bir tablo var
                            # zaten hatası verir biz bu hatayı yok etmek için Eğer tablo mevcut değilse yaarat diyoruz.

imlec.execute("INSERT INTO kitaplik VALUES('George Orwel', '1984')")  # sadece Bunu demek yetmiyor.
db.commit()                                                                      # Databasede işlemesi için commit şart!

db.close()                                                      # Unutmayalım önemli