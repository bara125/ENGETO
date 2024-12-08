jmeno = "Marek"
heslo = "1234"
uzivatel = {"Marek" : "1234"}
# pokud get jmeno is heslo 
if uzivatel.get(jmeno) == heslo:
    print("Ahoj ", jmeno, "vitej v apliakci ! Pokracuj...")
else:
    print("Uzivatelske jmeno a heslo nejsou v poradku !")
