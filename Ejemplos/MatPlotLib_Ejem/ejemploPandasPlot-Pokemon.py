import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('pokemon_data.csv')

df[df["Legendary"] == True].reset_index().sort_values("Name").plot(kind = "bar", x="Name", y=["Attack","Defense"])

plt.title("Nivel de ataque y defensa especiales de Pokemones Legendarios")
plt.xlabel("Pokemon")
plt.ylabel("Nivel")
plt.show()


df["Speed"].plot(kind = "hist", bins=20)
plt.title("Frecuencia de nivel de velocidad de los Pokemones")
plt.xlabel("Velocidad")
plt.ylabel("Frecuencia")
plt.show()

df.groupby("Type 1")[["HP","Attack","Defense","Speed"]].mean().plot.bar()

plt.title("Promedio nivel de características de Pokemones según tipo")
plt.xlabel("Tipo")
plt.ylabel("Nivel")
plt.show()

df["Generation"].value_counts().plot.pie(figsize=(6, 6),autopct="%.2f")
plt.title("Porcentaje de Pokemones por generación")
plt.show()