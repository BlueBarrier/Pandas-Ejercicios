"""
Universidad del Valle de Guatemala
Algortimos y programación básica


                    Actividad 11 - 2

Daniel Barrera 231238
Javier Valladares 23045

"""

import csv

#Leer el archivo y transformar los datos en una lista de diccionarios
with open('mcu_box_office.csv', 'r') as archivo:
    dict_reader = csv.DictReader(archivo)
    list_de_dict = list(dict_reader)

listaRateTomato=[]
for movie in list_de_dict:
    listaRateTomato.append([movie["tomato_meter"],movie["movie_title"]])
listaRatePeople=[]
for movie in list_de_dict:
    listaRatePeople.append([movie["audience_score"],movie["movie_title"]])
listaRatePeople.sort(reverse=True)
listaRateTomato.sort(reverse=True)
print("\nCalificación Audiencia")
for i in range(5):
    print("Nombre: {} Calificación: {}".format(listaRatePeople[i][1],listaRatePeople[i][0]))
print(""" 
""")
print("Calificación Rotten Tomatoes")
for j in range(5):
    print("Nombre: {} Calificación: {}".format(listaRateTomato[j][1],listaRateTomato[j][0]))
print(" ")