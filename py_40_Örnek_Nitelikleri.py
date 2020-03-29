class Asker1():
    kabiliyetler = []

muhammet = Asker1()
kemal = Asker1()
muhammet.kabiliyetler += ["Çok pis format atar"]
kemal.kabiliyetler += ["Sunucu kurmak"]

print(muhammet.kabiliyetler)
print(kemal.kabiliyetler)
print()

# Yukarıdaki istenmeyen bir durum. Yani örneğin nitelikleri ayrı ayrı
# olması lazımken olmadı. Bunu düzeltmek için kabiliyetler isimli niteliği Sınıf niteliğinden çıkartıp bir
# örnek niteliği yapmamaız lazım.

class Asker():

    print("Class Niteliği")         # Bu kısım ise class niteliğidir. # Class tanımlanırken direkt okunur.
    def __init__(self,isim, guc):   # Örnek niteliği tanımlamış olduk. Bu kısım sadece örnek tanımlandıktan sonra çalışır.
        self.isim = isim            # Aslında burası bildiğimimiz Constructur ilklendirme yani :)
        self.guc = guc
        self.kabiliyet = []

yasin = Asker("Yasin", 100)
mesut = Asker("Mesut", 70)
yasin.kabiliyet += ["Çok pis format atar"]
mesut.kabiliyet += ["Sunucu kurmak"]

print(yasin.isim, yasin.guc, yasin.kabiliyet, sep="\t")
print(mesut.isim, mesut.guc, mesut.kabiliyet, sep="\t")


