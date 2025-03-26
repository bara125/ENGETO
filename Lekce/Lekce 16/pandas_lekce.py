import pandas as pd
data = pd.Series([10, 20, 30, 40], index = ["Test1", "Test2", "Test3", "Test4"])
print(data) #Series je jako list nebo slovnik - priradi mi hodnoty
#print(["Test1"])
#print(data.mean())
#print(data > 25)
#print(data.max())

df = pd.DataFrame({

    "Jmeno": ["Jan", "Eva", "Petr"],
    "Status": ["OK", "OK", "FAIL"],
    "Doba_behu": [2.3, 4.1, 1.8]
})

#print(df)
#print(df["Status"])
#print(df.loc[1]) # vztiskne index
#print(df.iloc[1]) #vytiskne pozici poradi
#print(df.loc[1, "Jmeno"]) # index a konkretnni hodnota lze i souradnice a druhe taky cislo 
