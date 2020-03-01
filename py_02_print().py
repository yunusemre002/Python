#print() : bir fonksiyondur. Birileri tarafından ekrana cıktı vermesi icin yazılmıstır.
#Arka planda bir cok islem yapip ekrana yazı yazdirir.
#print fonk. bazi parametreler alir.
    #SEP : (seperate) normalde , demek bosluk demekti ama sep parametresiyle bunu degistirebiliriz.
    #Aslında printin sonunda gizli bir sep=" " var. Default olarak
print("T", "B","M","M")
print("T", "B","M","M", sep=".")
print("T", "B","M","M", sep="---")
print("T", "B","M","M", sep="")

print("Yunus", "Emre")
print("Yunus", "Emre", sep="_-_-_")

    #END : print fonksiyonu default olarak bir alt satıra iner ama bunu degistirmek bizim elimizde
    #Yani aslında printin sonunda gizli bir  end="\n" var.
print()
print("Yunus", "Emre", end="\n")
print("T", "B","M","M")

print("Yunus", "Emre", end="")
print("T", "B","M","M")

print("Yunus", "Emre", end=" - ")
print("T", "B","M","M")

