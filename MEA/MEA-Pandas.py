import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("video_games_sales.csv")

# Parte 4
G_sales=df.groupby("publisher")["global_sales"].sum().sort_values(ascending=False).head().plot(kind="bar")
na_sales=df.groupby("publisher")["na_sales"].sum().sort_values(ascending=False).head().plot(kind="bar")
eu_sales=df.groupby("publisher")["eu_sales"].sum().sort_values(ascending=False).head().plot(kind="bar")
jp_sales=df.groupby("publisher")["jp_sales"].sum().sort_values(ascending=False).head().plot(kind="bar")
other_sales=df.groupby("publisher")["other_sales"].sum().sort_values(ascending=False).head().plot(kind="bar")
plt.show()

# Parte 5
NAtop_ten=df[df["year"]>=2010][["name","na_sales"]].reset_index().sort_values(by="na_sales",ascending=False).head(10)
EUtop_ten=df[df["year"]>=2010][["name","eu_sales"]].reset_index().sort_values(by="eu_sales",ascending=False).head(10)
JPtop_ten=df[df["year"]>=2010][["name","jp_sales"]].reset_index().sort_values(by="jp_sales",ascending=False).head(10)
OHtop_ten=df[df["year"]>=2010][["name","other_sales"]].reset_index().sort_values(by="other_sales",ascending=False).head(10)
print(NAtop_ten)
print(EUtop_ten)
print(JPtop_ten)
print(OHtop_ten)

# Parte 6
print(G_sales)
ElecArts= df[df["publisher"]=="Electronic Arts"][["name","global_sales"]].sort_values(by="global_sales",ascending=False).head()
Nintendo=  df[df["publisher"]=="Nintendo"][["name","global_sales"]].sort_values(by="global_sales",ascending=False).head()
Sony= df[df["publisher"]=="Sony Computer Entertainment"][["name","global_sales"]].sort_values(by="global_sales",ascending=False).head()
Activ= df[df["publisher"]=="Activision"][["name","global_sales"]].sort_values(by="global_sales",ascending=False).head()
TTInter= df[df["publisher"]=="Take-Two Interactive"][["name","global_sales"]].sort_values(by="global_sales",ascending=False).head()

print(ElecArts)
print(Nintendo)
print(Sony)
print(Activ)
print(TTInter)