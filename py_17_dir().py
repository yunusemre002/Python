# Dir tiplerin hangi metodlara sahip old. bizlere söyler.

print(dir(list)) #or
for i in dir(list): # liste ait metodları gördük.
    print(i)

list1 = ["elma", "armut", "kivi"]
print(list1)

list1.append("muz")
print(list1, "   muz eklendi...")

list1.remove("elma")
print(list1, "   elma çıkartıldı.")