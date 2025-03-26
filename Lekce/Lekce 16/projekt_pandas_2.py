import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
df = pd.read_csv("test_data_new.csv")

# EXCEL

#df.to_excel("Report.xlsx", index=False) easy export 

nazev = f"Test_report_{datetime.now().strftime("%Y - %m-%d")}.xlsx" # vytvori nazev s datumem
df.to_excel(nazev, index=False)



#GRAFY

#df["Status"].value_counts().plot(kind="bar", title="Prehled stavu testu")

#plt.xlabel("Status")
#plt.ylabel("Pocet testu")
#plt.tight_layout()
#plt.show() 

#df["Doba_behu"].plot(kind="hist", bins=5, title="Prehled stavu testu") # bins ???
#plt.xlabel("Doba behu v s")
#plt.tight_layout()
#plt.show()

