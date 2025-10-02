separator = "-" * 40
print("Scitani: '+', ",
      "Odcitani: '-', ",
      sep= "\n")
print(separator)
while True:
    operace = input("Vyber si operaci:")
    if operace != "+" and operace != "-":
        print("Nezadali jste platny operator, zkuste to znovu")
        print(separator)
        continue
    else:
        cislo_1 = int(input("Zadej prvni cislo:"))
        cislo_2 = int(input("Zadej druhe cislo:"))
        vysledek = 0
        if operace == "+":
            vysledek = cislo_1 + cislo_2
        elif operace == "-":
            vysledek = cislo_1 - cislo_2
        print(cislo_1, operace, cislo_2, " = ", vysledek)
        pokracovani = input("Chcete provést další operaci?('a' pro ano, jakákoliv jiná klávesa pro ne):")
        if pokracovani != "a":
            print("Ukoncuji kalkulacku")
            break
# Dle operátoru proveď výpočet a vypiš ho - verze s f stringem
    #if operation == '+':
       # print(f'{number_1} + {number_2} = {number_1 + number_2}')
    #elif operation == '-':
        #print(f'{number_1} - {number_2} = {number_1 - number_2}')
        #khrfkjsdhfkjhsd)
        #osuhdrflshdjlfkjlskd
        #owhdrofwjheoirjiepow