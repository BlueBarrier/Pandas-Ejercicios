import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

michelin=pd.read_csv("michelin_my_maps.csv")

sushi= michelin[michelin["Cuisine"].str.contains("Sushi",case=False)].groupby("Award")[["Name","Cuisine","Award"]].count() # cantidad de restaurantes que tienen "Sushi" y sus variantes como especialidad
# además se agrupan por las distinciones obtenidas, de las cuales notamos que solo dos restaurantes, de sushi, tienen tres estresllas Michelin.
print("\n Sushi:\n",sushi)
sushi_3_stars=michelin.loc[(michelin["Award"]=="3 MICHELIN Stars") & (michelin["Cuisine"].str.contains("Sushi",case=False)),["Name","Cuisine","Award","Location"]] # se usa el método loc para filtrar con varios filtros y poder indexar
print("\n",sushi_3_stars) # Se muestran los tres restaurantes de Sushi con 3 estrellas Michelin

italy=michelin[michelin["Cuisine"].str.contains("Italian",case=False)].groupby("Award")[["Name","Cuisine","Award"]].count() # repetir pero con comida italiana
print("\n Italiana:\n",italy)
italy_3_stars=michelin.loc[(michelin["Award"]=="3 MICHELIN Stars") & (michelin["Cuisine"].str.contains("Italian",case=False)),["Name","Cuisine","Award","Location"]] # repetir pero con comida italiana
print("\n",italy_3_stars)

awards_ristorante=michelin.groupby("Award")["Award"].value_counts() # agrupamos, filtramos y contamos
print("\n Cantidad de restaurantes por \"Award\":\n",awards_ristorante) # mostramos

# Para ver que países tienen más restaurantes con estrellas Michelin, hacemos un mapa con las longitudes y latitudes de cada restaurante

# michemap= gpd.GeoDataFrame(michelin,geometry=gpd.points_from_xy(michelin.Longitude,michelin.Latitude)) # leemos coordenadas
# counts = michemap.groupby('Location').size().reset_index(name='count') # agrupamos por coordenadas
# gdf_counts = michemap.merge(counts, on='Location', how='left') # juntamos la ciudad con las coordenadas
# gdf_counts.plot.scatter(x='Longitude', y='Latitude', s=gdf_counts['count'], alpha=0.5) # configuramos la visualización y la distancia del plotting
# plt.show() # mostramos el mapa

# restaurantes con menor y mayor precio en euros
precio_EUR=michelin.loc[(michelin["Currency"]=="EUR"),["Name","MaxPrice","MinPrice","Currency","Location"]]
print("Min:\n",min(precio_EUR["MinPrice"]))

# Cantidad de restaurantes por moneda
restaurantes_curren=michelin.groupby("Currency")["Currency"].count().mean()
print("Media de restaurantes por tipo de moneda: ",restaurantes_curren)

# Restaurantes por tipo de cocina
risto_cusine=michelin.groupby("Cuisine")["Cuisine"].count().mean()
print("Media de restaurantes por tipo de comida: ",risto_cusine)

# Tipo de comida que más premian
print("Comida que más premian",michelin.groupby("Cuisine")["Cuisine"].value_counts().idxmax())

# Precio razonable
# razon=michelin[michelin["Award"]=="2 MICHELIN Stars"]["MinPrice"].mean()
# print(razon)