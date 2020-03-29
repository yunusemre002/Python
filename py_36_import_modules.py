# Herhangi bir python dosyası modüldür. Modüldeki metodları kullanamk iin onları import ederiz.
import os                       # os modülünün tamamını import eder.
from os import system           # os modülünün tamamı değil sadece ilgili metodu lazımsa böyle yapılır.
import os as lale
from os import system as sy     # as ekiyle artık bunu şu isimle kullanacağım demek istiyoruz.

os.system("cls")         #   ikiside
lale.system("cls")       #   aynı

system("cls")            #   ikiside
sy("cls")                #   aynı


#------Aşağıdaki metod diğer dosyada kullanılacak-------
def topla(liste:list):
    top = 0
    for i in liste:
        top += i
    return top
