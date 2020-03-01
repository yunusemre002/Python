# Aitlik operatörü "in"------------------------------------------------------
dizi = 'abcdfgh'

if 'a' in dizi:
    print("A harfi dizide var!")
else:
    print("A harfi dizide yok!")

if 'f' not in dizi:
    print("Dizide f yok")
else:
    print("f vardır.")

passwd = input("_ içereren bir parola giriniz.")
if '_' not in passwd:
    print("_ Kulanamalısın!")
else:
    print("Başarılı şekilde oluştu.")

# Birde is var ama onu bilmesende olur hatta bilme kull-anama.

