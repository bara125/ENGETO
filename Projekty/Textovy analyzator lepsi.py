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
separator = "-" * 40 
check_password = registered_users.get(user)
if check_password == password:   
    print("Welcome to the app, ", user, "\n"
      "We have 3 texts to be analyzed.\n",
      separator)
    text_nr = input("Enter a number btw. 1 and 3 to select:")
    if text_nr.isnumeric() and int(text_nr) in range(1, 4):
        words = TEXTS[int(text_nr)-1].replace(",", "").replace(".", "").split()
        print("There are ", len(words), " words in the selected text.")
        titlecase = list()
        uppercase = list()
        lowercase = list()
        numbers = list()
        for word in words: 
            if word.isdigit():
                numbers.append(int(word))
            if word.isupper() and len(word) >= 2 and word.isalpha():
                uppercase.append(word)
            if word.istitle():
                titlecase.append(word)
            if word.islower():
                lowercase.append(word)
        print("There are ", len(titlecase), " titlecase words.")
        print("There are ", len(uppercase), " uppercase words.")
        print("There are ", len(lowercase), " lowercase words")
        print ("There are ", len(numbers), " numeric strings.")
        print("The sum of all the numbers ", sum(numbers), "\n", separator)
        word_count = {}
        for word_ in words: 
            word_length = len(word_)
            if word_length in word_count:
                word_count[word_length] += 1
            else:
                word_count[word_length] = 1
        print("LEN | OCCURRENCES | NR.")
        print("-" * 40)
        for length in sorted(word_count.keys()):
            count = word_count[length]
            print(f"{length:3} | {'*' * count: <12} | {count}")
    else: 
        print("Zadana spatna hodnota")
else:
    print("Unregistered user, terminating the program.")
