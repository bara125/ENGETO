slova = []

while int(len(slova)) < 3:
    zadej = input("Zadej slovo o ctyrech pismemech:")
    if zadej in slova:
        print("Slovo ulozeno")
    if len(zadej) == 4 and zadej not in slova:
        slova.append(zadej)      
    if len(zadej) != 4:
        print("Slovo neni dlouhe ctyri znaky")
print("Mam ulozena tri slova")

# slo by to i setem a rovnou by si ukladal jen jedinecne hodnoty ma to pak trochu jednodussi kod
# Proměnná, kam budeš ukládat slova
slova = set()

# zadávej slova tak dlouho, dokud proměnná neobsahuje tři hodnoty
while len(slova) != 3:
    slovo = input("zadej slovo ze čtyř: ".upper())

    # .. pokud je již zadané slovo uložené, upozorni uživatele
    if slovo in slova:
        print("Slovo", slovo, "už je uložené")

    # .. pokud má slovo délku 4 znaky, ulož jej do proměnné
    elif len(slovo) == 4:
        slova.add(slovo)

    # .. pokud nemá slovo délku 4 znaky, upozorni uživatele
    else:
        print("Slovo není dlouhé čtyři znaky")

# Jakmile má objekt uložené tři hodnoty, cyklus ukonči a vypiš oznámení
else:
    print("Už mám uložené tři slova.")