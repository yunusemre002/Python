
sifreler = {"elif": "132465",
            "emre": "987645"}

names = sifreler.keys()

user_name = input("Kullanıcı adını giriniz : ")

if user_name in names:
    print("Hoşgeldin {}'cim".format(user_name))
    pwd = input("Parola : ")
    if pwd == sifreler[user_name]:
        print("Giriş yapabilirsiniz...")
    else:
        print("Wrong password")
else:
    print("Bu isimde bir kullanıcı yok!")