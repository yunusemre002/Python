#--------------Default Hali----------------
d1 = "Yunus"
d2 = "Demir"

ifade1 = "{} {}".format(d1, d2)  # değişkenleri sırasıyla yerleştirir.
ifade2 = "{} {}".format(d2, d1)  # değişkenleri sırasıyla yerleştirir.
print(ifade1, "\n", ifade2, "\n", sep="")

#----------Konumları Belirleme--------------
ifade1 = "{0} {1}".format(d1, d2) # d1 =0. değişken d2=1. değişkendir.
ifade2 = "{1} {0}".format(d2, d1) # d1 =0. değişken d2=1. değişkendir.
print(ifade1 ,"\n", ifade2, "\n", sep="")

#--------------Sözcük Atama-----------------
ifade1 = "{ad} {soyad}".format(ad=d1, soyad=d2) #
print("sözcük atama :", ifade1 , "\n", sep="")

#-------Sağa/ Sola Yaslama/ Ortala----------
# || ifadeleri daha net görmek için konuldu.
ifade1 = "|{:>20}|".format(d1) # 20 krt yer aç. Yunus'u sağa yasla. 15 krt boş kalır.
ifade2 = "|{:<20}|".format(d2) # 20 krt yer aç. Yunus'u sola yasla. 15 krt boş kalır.
ifade3 = "|{:^20}|".format(d1) # 20 krt yer aç. Yunus'u ortala. 7,5 sağ+sol boşluklar.
print(ifade1 ,"\n", ifade2, "\n", ifade3, "\n",  sep="")

#-----------Yalnıca String/int--------------
ifade1 = "{:s}".format(d1) # :s Yalnızca String alır.
ifade2 = "{:d}".format(200) # :d Yalnızca decimal(sayı) alır.
print(ifade1 ,"\n", ifade2, "\n",  sep="")

#-------------- Çevirmeler -----------------
ifade1 = "binary(20) = {:b} ".format(20) # :b Verilen sayıyı binary' ye çevirir.
ifade2 = "ASCII 65   = {:c} ".format(65) # :c ASCII tablosundaki yeri
ifade3 = "{:,}".format(51464246067) # Sayıları basamaklarıa ayırma
print(ifade1 ,"\n", ifade2, "\n", ifade3,  sep="")

