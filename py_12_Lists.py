#Listeler içerisinde hertürden veri barındırabilirler. Bunlar int,str,float
# olabilir aynı anda aynı liste içerisinde de bulunabilirler.
# += ile eklem yapılabilir ama -= ile çıkartma işlemi yapılamaz tıpkı str="abc"
# str -= b  yapılamayacağı gibi

#Dizi gösterimimnin iki türü vardır.
dizi = "ali ata bak"
dizi = str("ali ata bak")

# Liste gösterimininde iki türü vardır.
list1 = []
list2 = list()

list1 = ["ali", 10, 7.8]    # Görüldüğü üzre str, int ve float aynı list içinde
for i in list1:
    print(type(i))

print("\n------------BOOKS-------------")
list2 = ["Yol ayrımı", "50 Soruda yapay zeka", "Hayvan çiftliği", "Ana", "Budala"]
for i in list2:
    print("Book name: {}".format(i))

print()
addbook = input("Enter a book to be added: ")
list2 += [addbook] #!!! EKLEME İŞLEMİ İÇİN [İÇİNDE] YAZMALIYIZ.
print(list2)

# ekleme işlemi += ile ypılırken -= işlemi yapılamaz bunun tamamı bir string olarak
# düşünülebilir nasıl ki str="abc" iken str -= b  yapılamayacağı gibi