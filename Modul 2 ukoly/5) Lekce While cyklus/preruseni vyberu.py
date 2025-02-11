ovoce = "jablko","banan","citron","pomeranc"
print(*ovoce, sep=", ") #* UNPACKING OPERATOR

while True: 
    vyber = input("vyber z dostupneho ovoce: ".upper())
    if vyber not in ovoce:
        print("Ovoce neni v nabidce")
    else:
        print("Bezva, toto ovoce je v nabidce")
        break

