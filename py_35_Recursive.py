def faktoriyel(sayi):
    if sayi == 1:                                       # Durma noktası : 5*4*3*2*1
        return 1
    else:
        return sayi * faktoriyel(sayi - 1)              # İlerleme sitili

print("5! :", faktoriyel(5))
print("10! :", faktoriyel(10))