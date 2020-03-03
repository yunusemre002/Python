#   Demetler List gibidir içine her türden şey alabilir. Yalnız listden ayrılan yanı ise
#   demetlerede ekleme çıkarma işlemi yapılamamasıdır. Demetler sadece bir kez tanımlanır
#   ve değiştirilemezler.Peki  neden kullanalım denirse Ddemetlerin çalışma hızlı > List
#   (Çok hızlı yani). Özetle  boş demet yaratmak saçmalıktır. --DEMET = TUPLE--

list1 = ["a"]
list1 += ["b"]
print("Listede ekleme yapmak mümkündür : ", list1)

tuple0 = ("sifirinci")  # elemandan sonra bir virgül koymazsak parantezleri işlem önceliği gibi algılar
                        # So, tuple1 deki gibi son elemandan sonra bir virgül bırakılmalı tuple olduğunu anlatmak için
                        #veya tuple2 deki tanımlama yapılabilir.
tuple1 = ("birinci","b", "c", "d",)
tuple2 = tuple("a")
print("tuple0 : ", type(tuple0), tuple0)
print("tuple0 : ",type(tuple1), tuple1)
print("tuple0 : ",type(tuple2), tuple2)