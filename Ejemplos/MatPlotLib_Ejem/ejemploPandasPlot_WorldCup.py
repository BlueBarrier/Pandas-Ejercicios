import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv('world_cup_data.csv')

#Mostrar las diferentes características de una tabla
print('Dimensiones:', df.shape)
print('Número de elementos:', len(df))
print('Nombres de columnas:', df.columns)
print('Nombres de filas:', df.index)
print('Tipos de datos:\n', df.dtypes)

#Plot de numero de partidos en el año
plt.figure(figsize=(10, 5))
plt.plot(df['Year'], df['MatchesPlayed'], color='red')
plt.title('Number of Matches Played by Year')
plt.xlabel('Year')
plt.ylabel('Number of Matches Played')
plt.show()

# Plot de distribucion de goles por los ganadores
plt.figure(figsize=(8, 6))
plt.hist(df['GoalsScored'], bins=10, color='blue', alpha=0.7)
plt.title('Distribution of Goals Scored')
plt.xlabel('Number of Goals Scored')
plt.ylabel('Frequency')
plt.show()