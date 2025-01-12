vysledek = list()
start = 3
stop = 9 
delitel = 3 
if isinstance(start, int) \
    and isinstance(stop, int) \
    and isinstance(delitel, int) == True:
        print("Zadany rozsah: ", "<",start, ", ",stop, ">") # sep = ""
        for cislo in range(start, stop + 1):
            if cislo % int(delitel) == 0:
                vysledek.append(cislo)
        print("Cisla delitelna ", delitel, ":", vysledek)
else: 
    print("Zadane vstupy musi byt cisla.") 
