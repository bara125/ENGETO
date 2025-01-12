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

user = input("Username:")
password = input("Password:")
print("-"*40)
check_hesla = registered_users.get(user)
if check_hesla == password:
    print("Welcome to the app, ", user, "\n"
          "We have 3 texts to be analyzed.")
#ODDELOVAC/////////////////////////////////////



else:
    print("Unregistered user, terminating the program.")
