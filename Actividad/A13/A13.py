import pandas as pd
import matplotlib.pyplot as plt


# # Parte 1
# df=pd.read_csv("world_cup_data.csv")
# print("Dimensiones Data Set Mundiales")
# print("Dimensiones: ",df.shape)
# print("Tipo de datos: ",df.dtypes)
# Win=df.value_counts("Winner").plot(kind="bar")
# plt.title("Mundiales ganados por países")
# plt.xlabel("Winner")
# plt.ylabel("Mundiales Ganados")
# plt.show()

# Parte 2
# Ama=pd.read_csv("AmazonBooks.csv")
# print("Dimensiones Data Set Amazon Books")
# print("Dimensiones: ",Ama.shape)
# print("Tipo de datos: ",Ama.dtypes)
# sells=Ama.groupby("Year")["Genre"].value_counts()
# print("\n",sells)
# resena=Ama[Ama["Year"]==2020][["Name","Reviews"]].sort_values(by="Reviews",ascending=False).head(10)
# print("\n",resena)
# precio=Ama.groupby("Year")["Price"].max().plot(kind="bar")
# plt.title("Precio máximo de libro por cada año")
# plt.xlabel("Year")
# plt.ylabel("Precio")
# plt.show()
# rating=Ama["User Rating"].plot(kind="hist",bins=5)
# plt.title("Histograma User Rating")
# plt.xlabel("Rate")
# plt.ylabel("Frecuencia")
# plt.show()

# Ejercicio 3
rest=pd.read_csv("restaurantes.csv")
ventas=rest.groupby("Country")["Sales"].sum()
print(ventas)
ventas.plot(kind="bar")
plt.title("Ventas en billones por país")
plt.xlabel("País")
plt.ylabel("Ventas en billones")
# plt.show()
v_rest=rest.groupby("Restaurant")["Sales"].sum()
print(ventas)
v_rest.plot.pie(figsize=(6,6),autopct="%.2f")
plt.title("Ventas en billones por restaurante")
# plt.show()
competir=rest[(rest["Restaurant"]=="Starbucks" & rest["Restaurant"]=="McDonald's")]
pais=competir[(rest["Country"]=="United States"&rest["Country"]=="China"&rest["Country"]=="Japan")][["Restaurant","Country","Sales"]]
print(pais)