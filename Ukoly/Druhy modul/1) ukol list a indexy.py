zamestnanci = [
    "Frantisek", "Bruno",
    "Anna", "Jakub", 
    "Klara", "Anezka", 
    "Anezka", "Anezka"
               ]

posledni_index = len(zamestnanci) - 1
print("Na indexu 2 je: ", zamestnanci [2])
print("Na", posledni_index, "indexu je: ", zamestnanci[posledni_index])
print("V intervalu od 2 do 5 je: ", zamestnanci [2:6])
print("Kazdy treti clen je: ", zamestnanci[0:8:3]) #kratsi [::3]