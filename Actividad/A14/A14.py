import pandas as pd
import scipy
import matplotlib.pyplot as plt

df=pd.read_csv("top50.csv")

# Canciones bailables
# tipo_m=df[["TrackName","Danceability","Liveness","Acousticness","Popularity"]].sort_values(by="Popularity",ascending=False).plot(kind="box")
# print(tipo_m)
# plt.show()

# # Similitudes
# tipo_n=df[["TrackName","Danceability","Liveness","Acousticness","Popularity"]].head(5).sort_values(by="Popularity",ascending=False)
# print(tipo_n.describe())
# tipo_n.plot(kind="barh",x="TrackName")
# plt.show()

# Promedio de duración según su género
# tiempo=df.groupby("Genre")["Length"].mean().plot(kind="bar")
# plt.show()
# print(tiempo"%.2f")
fig=plt.figure()
ax1= fig.add_subplot(2,2,1)
ax2=fig.add_subplot(2,2,2)
ax3=fig.add_subplot(2,2,3)
beats=df.groupby("Genre")["BeatsPerMinute"].mean().plot(kind="bar",ax=ax1)
energy=df.groupby("Genre")["Energy"].mean().plot(kind="bar",ax=ax2)
loud=df.groupby("Genre")["LoudnessdB"].mean().plot(kind="bar",ax=ax3)
plt.show()
