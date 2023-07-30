"""
Universidad del Valle de Guatemala
Algortimos y programación básica


                    Actividad 12

Daniel Barrera 231238
"""

import pandas as pd

pokemon=pd.read_csv("pokemon_data.csv")

print("\nLa base de datos tiene las siguientes dimensiones {}.\n".format(pokemon.shape))
print("La base de datos tiene {} datos.".format(len(pokemon)))
print("La base de datos tiene las siguientes columnas:\n",pokemon.columns)
print("La base de datos tiene las siguientes filas: \n",pokemon.index)
print("La base de datos tiene los siguientes tipo de datos:\n",pokemon.dtypes)

print("\nLas primeras 10 filas:\n", pokemon.head(10))
print("\nLas últimas 10 filas:\n", pokemon.tail(10))

print("\nPokemon con identificador #50: \n",pokemon.iloc[50])

print("\nPokemones Tipo 1, Fuego\n",pokemon[pokemon["Type 1"]=="Fire"].groupby(["Name","Type 1"])["Type 1"].count())

print("\n Mejor aguante de Hit Points\n",pokemon[["Name","HP"]].sort_values(by="HP",ascending=False).head(10))

print("\n Cantidad de pokemon según su Tipo 1\n: ",pokemon["Type 1"].value_counts())

print("\n Agrupación de pokemones por Tipo 1 y si son legendarios:\n ",pokemon.groupby(["Type 1","Legendary"])["Legendary"].count())