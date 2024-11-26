kg_lb = 2.20
km_mile = 0.62
l_gal = 0.26

kg_pocet = 80
km_pocet = 54
l_pocet = 5

kg_vysledek = str(kg_pocet * kg_lb)
km_vysledek = str((km_pocet * km_mile))
l_vysledek = str(l_pocet * l_gal)

print(str(kg_pocet) + " kg je " + kg_vysledek + " lb")
print(str(km_pocet) + " km je " + km_vysledek + " mil")
print(str(l_pocet) + " l je " + l_vysledek + " gal")