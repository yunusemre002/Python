def dikUcgenmi(a,b,hipotenus):
    if a**2 + b**2 == hipotenus**2:
        return True
    else:
        return False

print("1, 2, 3 ?", dikUcgenmi(1,2,3))
print("3, 4, 5 ?", dikUcgenmi(3,4,5))


#---------------------LAMBDA-----------------------------
fonk = lambda a,b,hipotenus : a**2 + b**2 == hipotenus**2

print("1, 2, 3 ?", fonk(1,2,3))
print("3, 4, 5 ?", fonk(3,4,5))
