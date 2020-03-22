zirhlar = {"demir": 20, "çelik": 10}

kisiler = {
    "karakter1": {"silah": "kılıç",
                  "güç": 30,
                  "saglik": 100,
                  "zirh": zirhlar["demir"]
                  },
    "karakter2": {"silah": "kılıç",
                  "güç": 30,
                  "saglik": 100,
                  "zirh": zirhlar["çelik"]
                  }
}


def vur(vurulan, vuran):
    guc = vuran["güç"]
    saglik = vurulan["saglik"]
    zirh = vurulan["zirh"]
    damage = guc - zirh
    vurulan["saglik"] = saglik - damage


print("karakter2 sağlik : ", kisiler["karakter2"]["saglik"])

vur(kisiler["karakter2"], kisiler["karakter1"])
print("\nKarakter  vuruldu...")
print("karakter2 sağlik : ", kisiler["karakter2"]["saglik"])

vur(kisiler["karakter2"], kisiler["karakter1"])
print("\nKarakter  vuruldu...")
print("karakter2 sağlik : ", kisiler["karakter2"]["saglik"])
