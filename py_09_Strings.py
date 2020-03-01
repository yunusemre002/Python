#---------------Kötü bir örnek------------
bas = "Baslangic kısmı "
son = "son kisim"
string = "orta kısım "
newString = bas + string + son
print(newString)

#---------------"String".format()----------------------
# {} süslü parazntezler konulan kısmını .format metoduyla yerleştiriyoruz
cumle = """
English = Hello World!
Turkish = {} {}
""".format("Merhaba","Dünya")
print(cumle)
#------------
krt = "abcçdef"
for i in krt:
    print("Basatırılan karakter {}".format(i))
