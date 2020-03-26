
print("|-8| :", abs(-8))
print("89/7 bölüm,kalan :", divmod(89,7))


dizi = ["Kuzey", "Deniz", "Saha", "Komutanlığı", "Kasımpaşa"]
dizi2 = [5, 8, 9 ,10, 55, 500, 1, 45, 3, 78]
print("\n",dizi, "\n", dizi2)

print("dizi2 max :",max(dizi2))
print("dizi max :",max(dizi, key=len))  # 2 parametre senin referansın ne?

print("dizi2 max :",min(dizi2))
print("dizi max :",min(dizi, key=len))  # 2 parametre senin referansın ne?

print(sum(dizi2))
print(sum(dizi2,100))   # toplam+100