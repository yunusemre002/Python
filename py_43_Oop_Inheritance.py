class Tasit():                                      # PARENT
    def __init__(self, tekerSayisi, kapi):
        self.tekerSayisi = tekerSayisi
        self.kapi = kapi

    def kapiAc(self):
        print("Kapi açıldı.")

class Araba(Tasit):                               # CHILD
    pass                                          # Tasittan tüm niteliklerini miras aldım

class Tır(Tasit):                                 # CHILD
    def __init__(self, tekerSayisi, kapi, turboSayisi):
        super().__init__(tekerSayisi, kapi)         # self.tekerSayisi = tekerSayisi \n # self.kapi = kapi  # Böylede yazabilirdim OVERRİDE olurdu # Ama usul bu değildir.
        self.turboSayisi = turboSayisi

    def dorseBirak(self):
        print("Dorse birakıldı.")


car1 = Araba(4, 4)
print("car1 nesnemizin kapi sayısı :{}'tür".format(car1.kapi))
tir1 = Tır(8, 2, 5)
print("tir1 nesnemizin teker sayisi:{} \tkapi sayısı :{} \t turbo sayisi :{}".format(tir1.tekerSayisi, tir1.kapi, tir1.turboSayisi))
tir1.dorseBirak()