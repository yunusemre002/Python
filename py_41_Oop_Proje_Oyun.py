import random

class Dusman():
    def __init__(self):
        self.sagmi = True
        self.saglik = random.randint(30, 70)
        self.kalkan = random.randint(0, 10)
        self.guc = random.randint(20, 50)

    def vur(self, player):
        damage = self.guc - player.kalkan
        player.saglik -= damage
        if player.saglik <= 0:
            player.sagmi = False


class Player():
    def __init__(self):
        self.sagmi = True
        self.saglik = 500
        self.kalkan = 20
        self.guc = 55


    def vur(self, dusman):
        damage = self.guc - dusman.kalkan
        dusman.saglik -= damage
        if dusman.saglik <= 0:
            dusman.sagmi = False
            enemies.remove(dusman)


enemies= list()
for i in range(10):
    enemies.append(Dusman())

oyuncu = Player()

while True:
    print("****Oyuncu sağlık  :{}\t\tKalkan :{}\t\tGüç :{}\t\t Sağ mı? :{}".format(oyuncu.saglik, oyuncu.kalkan,
                                                                                   oyuncu.guc, oyuncu.sagmi))
    for i in enemies:
        print(" {}. Düşman sağlık  :{}\t\tKalkan :{}\t\tGüç :{}\t\t Sağ mı? :{}".format(enemies.index(i), i.saglik,
                                                                                        i.kalkan, i.guc, i.sagmi))
    if oyuncu.sagmi == False:
        print("Game Over! :(")
        quit()

    if not enemies:
        print("Tebrikler!")
        quit()

    secim = int(input("Düşman seçin :"))
    dusman = enemies[secim]
    oyuncu.vur(dusman)

    if enemies:
        saldıran = enemies[ random.randint(0, len(enemies)-1)]
        saldıran.vur(oyuncu)

















