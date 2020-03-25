str = "Kuzey Deniz Saha Komutanlığı Kasımpaşa"
print(str)

print(str.replace("a","A"))  # Küçük a ları büyük A yapar.
print(str.split())           # Default olarak boşluklardan böler ve list olarak yazar.
print(str.split("a"))        # a'lardan böldük a'ları siler, sağını solunu yazar. dikkat boşluklar var
print(str.split(" ",1))      # Boşluktan böl ama ilk 1 taneyi böl, bırak.  // 2. parametre ile söyledik.
print(str.rsplit(" ",1))     # Boşluktan böl ama son 1 taneyi böl, bırak.  // r ile sağdan başla dedik.
print(str.lower())
print(str.upper())

str1 = """Python 3 ile Programlamayı En Temelden En İleri Düzeye Kadar Gerçek Projeler Yaratarak Öğrenin!
Bu kursta Python dilinin hızlı uygulama geliştirmeye yönelik avantajını kullanarak hemen her bölümde 
uygulamalar geliştirerek Python dilini tümüyle kavrayacağız. Yalnızca Python dilinin içerdiği kodları
değil programlama kültürünü de öğreneceğiz.
"""
print(str1.splitlines())
#-------------------STR.COUNT("LALE")--------------------------
print("Python kelime sayısı :", str1.count("Python"))
print("deneme".count("e"))
#-------------------STR.FIND("LALE")--------------------------
print("lale kelimesi var mı? :", str1.find("lale"))
print("lale kelimesi var mı? :", str1.find("ile"))              # Varsa indisini verir yoksa -1
print()

# ------------JOİN : Split edilmiş bir metni şöyle birleştir demek-------------
print("------------------------JOİN---------------------------")
bolunmus = "Kuzey Deniz Saha Komutanlığı Kasımpaşa".split()     # SPLİT ETTİK.
print(bolunmus)
string = " ".join(bolunmus)                                     # " " 1 boşluk ile birleştirdik.
print(string)

string1 ="--".join(bolunmus)                                    # "--" tire ile birleştirdik.
print(string1)

