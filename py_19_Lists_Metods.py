#   'append', 'clear', 'copy', 'count', 'extend'(Birleştir/ekle), 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
#   list.copy != '='
def yaz(liste):
    for i in liste:
        print(i)

list1 = ["ince memed", "Araba Sevdası", "Felatun bey ve ragıp efendi", "Ana", "1984", "hayvan çifliği"]
print(list1)
list1.append("Yaban")
list1.append("Yeni köşk")
list1.append("Ana")
print(list1)
list1.remove("Felatun bey ve ragıp efendi")
print(list1)
print("'Ana'  kitabı sayısı   : {} ".format(list1.count("Ana")))
print("'Araba Sevdası' sayısı : {} ".format(list1.count("Araba Sevdası")))

# .copy
list2 = list1 # Aslında list 1 bir pointerdır yaratılan nesneyi point eder.
              # Böyle diyince list2 de aynı nesneyi point etmiş olur. Dolayısıyla
              # birisinde yapılan değişiklikler kisinde de yapılmış olur.
              # Eğer list1 ve point edilen yeri kopyalamak istiyorsak .copy
              # metodunu ullanmalıyız.
list3 = list1.copy()

print("\n-------İlk durum--------")
print(list1 , list2, list3, 30*"-", sep="\n")

list1.append("Hanımağa")
list1.append("kalaycı")
list2.remove("Ana")
list3.remove("ince memed")
list3.append("Pejmürde halim")

print("\n-------ikinci durum--------")
print(list1 , list2, list3, 30*"-", sep="\n")

print("list1, hayvan çifliği indexi : ", list1.index("hayvan çifliği"))
print("list1, ince memed indexi : ", list1.index("ince memed"))

#   .extend() ATAMAYA GER YOK!
list1.extend(list3)
print("list1.extend(list3) : ", list1)

# .sort() ATAMAYA GERKE YOK!
list4 = [4,5,1,7,2,3,8]
print("\n",list4,sep="")
list4.sort()
print(list4)

print("\n",list3, sep="")
list3.insert(1, "Cehennem")
print("1. sıraya insert ettim kaydırdım",list3, sep="\n")