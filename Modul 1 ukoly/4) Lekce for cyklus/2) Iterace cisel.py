
cisla = [1, 2, 3, 4, 5, 6, 7, 8]
suda = 0
licha = 0
for cislo in cisla:
    if cislo % 2 == 0:
        suda += cislo #ENGETO - suda = suda + cislo
    else:
        licha += cislo # ENGETO - licha = licha + cislo 
vysledek = abs(suda - licha)
print("Rozdil je: ", vysledek)
