"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Barbora Pokorná
email: barbora.tuhackova@gmail.com
"""
registered_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123", 
    "liz": "pass123"
}

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

user = input("Username:")
password = input("Password:")
print("-"*40)  # oodelovac vylepsit?????
check_hesla = registered_users.get(user)
if check_hesla == password:
    print("Welcome to the app, ", user, "\n"
          "We have 3 texts to be analyzed.")
    print("-"*40) # oodelovac vylepsit?????
    cislo_textu = input("Enter a number btw. 1 and 3 to select:")
    if cislo_textu.isnumeric() and int(cislo_textu) in range(1, 4):
        slova = TEXTS[int(cislo_textu)-1].replace(",", "").replace(".", "").split()
        print("There are ", len(slova), " words in the selected text.")
        titlecase = list()
        for slovo in slova: 
            if slovo.istitle():
                titlecase.append(slovo)
        print("There are ", len(titlecase), " titlecase words.")
        uppercase = list()
        for slovo in slova:
            if slovo.isupper() and len(slovo) >= 2 and slovo.isalpha():
                uppercase.append(slovo)
        print("There are ", len(uppercase), " uppercase words.")
        lowercase = list()
        for slovo in slova:
            if slovo.islower():
                lowercase.append(slovo)
        print("There are ", len(lowercase), " lowercase words")
        numbers = list()
        for slovo in slova:
            if slovo.isdigit():
                numbers.append(int(slovo))
        print ("There are ", len(numbers), " numeric strings.")
        print("The sum of all the numbers ", sum(numbers))
        print("-"*40) # oodelovac vylepsit?????
        cestnost_slov = {}
        for slovo in slova: 
            delka_slova = len(slovo)
            if delka_slova in cestnost_slov:
                cestnost_slov[delka_slova] += 1
            else:
                cestnost_slov[delka_slova] = 1
        print("LEN | OCCURRENCES | NR.")
        print("-" * 40)
        for delka in sorted(cestnost_slov.keys()):
            cetnost = cestnost_slov[delka]
            print(f"{delka:3} | {'*' * cetnost: <12} | {cetnost}")
    else: 
        print("Zadana spatna hodnota")
else:
    print("Unregistered user, terminating the program.")
