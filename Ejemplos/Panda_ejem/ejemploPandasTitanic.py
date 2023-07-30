#importar la librería
import pandas as pd

#Leer el contenido del archivo CSV a un DataFrame
df = pd.read_csv("titanic.csv")

#Mostrar las diferentes características de una tabla
print('Dimensiones:', df.shape)
print('Número de elementos:', len(df))
print('Nombres de columnas:', df.columns)
print('Nombres de filas:', df.index)
print('Tipos de datos:\n', df.dtypes)

#Mostrar algunos de los datos del DataFrame
print('Primeras 10 filas:\n', df.head(10))
print('Últimas 10 filas:\n', df.tail(10))

#Mostrar por pantalla los datos del pasajero con identificador 148.
print("\nPasajero en el registro 148:\n",df.iloc[148])

#Mostrar por pantalla los nombres de las personas que iban en primera clase ordenadas alfabéticamente.
print(df[df["Pclass"] == 1]["Name"].sort_values())

#Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron.
print(df["Survived"].value_counts(normalize=True)*100)

#Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase.
print(df.groupby("Pclass")["Survived"].value_counts(normalize=True)*100)

#Eliminar del DataFrame los pasajeros con edad desconocida.
df.dropna(subset=["Age"], inplace = True)
print('Número de elementos:', len(df))

#Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase.
print(df[df["Sex"]=="female"].groupby("Pclass")["Age"].mean())

#Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no.
df["Minor"] = df["Age"] < 18

#Mostrar por pantalla el porcentaje de menores y mayores de edad que sobrevivieron en cada clase.
print(df.groupby(["Pclass", "Minor"])['Survived'].value_counts(normalize = True) * 100)

#Guardar en otro archivo CSV los cambios que se realizaron en el DataFrame.
df.to_csv("titanic_mod.csv",index=False)
