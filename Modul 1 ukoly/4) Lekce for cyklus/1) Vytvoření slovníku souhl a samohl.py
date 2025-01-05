#vysledek = {"souhlasky": list(pismeno) for pismeno in veta.lower() if pismeno in samohlasky }


veta = "Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu"
samohlasky = "aeiouáéíóú"
souhlasky = "bcčdďfghjklmnňprřsštťvzžcdž"
vysledek = {"souhlasky": [], 
            "samohlasky": []}

for pismeno in veta:
    if pismeno.isalpha():
        if pismeno.lower() in samohlasky:
            vysledek["samohlasky"].append(pismeno)
        elif pismeno.lower() in souhlasky:
             vysledek["souhlasky"].append(pismeno)
print("Pocet samohlasek: ", len(vysledek["samohlasky"]), "|", "Pocet souhlasek: ", len(vysledek["souhlasky"]),)

