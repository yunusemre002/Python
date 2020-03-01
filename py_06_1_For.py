alfabe="abcçdefgğhıijklmnoöprsştuüvyz"
sayi=0

for x in alfabe:
    print(x, end=" ")
    sayi+=1

print("  /alfabe dizisinde", sayi, "kadar harf vardir.")


print("\n0 dan 12 ye kadar yazdıracak")
for a in range(0,13): # 0 dahil 13 dahil değil
    print(a, end=" ")

print("\n\n0 dan 6 ya kadar : ")
for b in range(7):  # 0 dahil 7 dahil değil
    print(b,end=" ")

print("\n\n0 dan 19 a kadar 5 er 5 er: ")
for c in range(0,20,5): # 0 dahil 13 dahil değil
    print(c, end=" ")

print("\n\nWhile 10 a kadar")
k=0
while k<=10:
    print(k, end=" ")
    k +=1
