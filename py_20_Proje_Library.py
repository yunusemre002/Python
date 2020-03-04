import os
# kitap = (name , author) tipinde bir tuple olacak çümkü sabit değişken değil.
# liste ise: Elemanları tuple olan bir liste olacak.
bookList = list()

menu ="""[-------------------------*
[1] Kitapları Listele.
[2] Kitap Ekle.
[3] Kitap al.
[q] Çıkış.
[--------------------------*
"""
def listele(liste:list):
    for i in liste:
        print("{} --> {}".format(i[0],i[1]))
    input("Ana menü için entere basınız...")

def ekle(bookName:tuple, liste:list):
    liste.append(bookName)
    print("Kitap eklendi...")
    input("Ana menü için entere basınız...")

def varmı(bookName:tuple, liste:list):
    if bookName in liste:              # for i in liste: if i[0] ==bookName[0] and i[1] ==bookName[1]:
        return True
    else:
        return False

def al(bookName:tuple, liste:list):
    if varmı(bookName,liste):     # so if it return true
        liste.remove(bookName)
        print("Başarılı!")
    else:
        print("almak istediğini kitap kütüphanemimde na mevcut!")

while True:
    os.system("cls")    # Windowsta komut ekranını temizler.
    print(menu)

    x = input("Lütfen yapacağınız işlemi seçiniz : ")

    if x=="1":
        listele(bookList)
        pass
    elif x=="2":
        book_name = input("Enter the book name : ")
        book_author = input("Enter the author    : ")
        book = (book_name, book_author)
        ekle(book, bookList)
        pass
    elif x=="3":
        book_name = input("Enter the book name : ")
        book_author = input("Enter the author    : ")
        book = (book_name, book_author)
        al(book, bookList)
        pass
    elif x=="q":
        print("İyi günler efenim...")
        quit()
    else:
        print("Yanlis bir secim yaptiniz...")
        pass