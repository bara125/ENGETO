import pandas as pd

#df = pd.DataFrame({
    #"ID": [1, 2, 3, 4, 5, 2, 6],
    #"Jmeno": ["LoginTest", "RegistrationTest", "SearchTest", "LogoutTest", "UploadTest", "RegistrationTest", "ProfileUpdateTest"],
    #"Status": ["OK", "Failed", "OK", "Failed", "OK", "Failed", "Failed"],
    #"Doba_behu": [2.3, 4.1, 1.2, 3.5, 2.0, 4.1, 3.7],
    #"Chybova_hlaska": [None, "ValidationError", None, None, None, "ValidationError", None]
#}) zadani do souboru

#df.to_csv("test_data_new.csv", index=False, encoding= "utf-8") export do csv

data_frame = pd.read_csv("test_data_new.csv")

#print(data_frame.info())
#print(data_frame.shape) pocet radku a sloupcu
#print(data_frame.columns)
#print(data_frame.dtypes) typy dat 

#print(data_frame.isnull().sum()) pokud je isnull true sum dava +1 
#print(data_frame[data_frame["Chybova_hlaska"].isnull()]) vypise jen testy kde je chybova hlaska null - neni 

#NAHRADA NULOVE HODNOTY

#data_frame["Chybova_hlaska"] = data_frame["Chybova_hlaska"].fillna("Neznama chyba") # nahradi 

#data_frame.to_csv("test_data_new.csv", index= False, encoding= "utf-8") # ulozi - nazev souboru by mohl byt i jiny

#VYHOZENI DUPLICIT 

#print(data_frame.duplicated().sum()) vytiskne jen pocet duplicitni

#data_frame = data_frame.drop_duplicates() vuhodi duplicity
#data_frame.to_csv("test_data_new.csv", index= False, encoding= "utf-8") zase jen ukladam

#CETNOST HODNOT

#print(data_frame["Status"].value_counts()) #vypise kolik jakych  hodnot ve status 



# SOUHRNNE STATISTIKY

#print(data_frame.groupby("Status")["Doba_behu"].mean()) # jak dlouho trval jaky test prumerne

#print(data_frame.groupby(["Status", "Jmeno"]).size()) # ktere selhaly a ktere byly ok 

