user_email = "marek.parek@gmail.com"
user_1 = {}
user_1 ["name"] = "Marek"
user_1 ["surname"] = "Parek"
user_1 ["email"] = user_email
print("User #01 ", user_1)

#pomoci update
user_email1 = {"email" : "marek.parek@gmail.com"}
user_2 = dict()
user_2 ["name"] = "Marek"
user_2 ["surname"] = "Parek"
user_2.update(user_email1) # tady tam vkladam definovany klic a hodnotu 
print("User #02 ", user_2)