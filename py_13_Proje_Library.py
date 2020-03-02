
booksList = list()

menu = """
------------------------
[1] Kitapları Listele.
[2] Kitap Ekle.
[3] Kitap sil.
[q] Çıkış yap.
-----------------------
"""

def listele(listname):
    for i in listname:
        print("     * Book name: {}".format(i))
    print()
    input("Ana menüye dönme için entere basınız...")

def ekle(bookname, listname):
    listname += [bookname]                              # [] koymayı unutma!
    print("İşleminiz başarıyla tamamlandı.")
    input("Ana menüye dönmek için entere basınız.")

def sil(bookname, listname):
    pass

def cikis():
    print("Çıkış yapılıyor...")
    exit()

while True:
    print(menu)
    x = input("Bir işelem seçiniz...")

    # iflerin içindeki sayıları"içinde" yazdım çünkü        #input fonks. str alır unutma!!!
    if  x=="1":
        listele(booksList)
    elif x=="2":
        nameofbook = input("Enter book name to b added: ")
        ekle(nameofbook, booksList)
    elif x=="3":
        nameofbook = input("Enter book name to b deleted: ")
        sil(nameofbook,booksList)
    elif x=="q":
        cikis()
    else:
        print("Yanlış bir seçim yaptınız.")
        input("Ana menüye dönmek için entere basınız...")

