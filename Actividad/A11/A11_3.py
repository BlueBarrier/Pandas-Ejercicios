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

listaTaquilla=[]
for movie in list_de_dict:
    listaTaquilla.append([movie["worldwide_box_office"],movie["movie_title"]])

listaTaquilla.sort(reverse=True)
rate=[]
for j in range(5):
    rate.append([listaTaquilla[j][1],input("Película: {}, ingrese su calificación: ".format(listaTaquilla[j][1]))])

with open("mcu_popular.csv", mode="x") as archivo_w:
    lst_writer= csv.writer(archivo_w,delimiter=",",quotechar='"',quoting=csv.QUOTE_MINIMAL,lineterminator="\n")
    for pelicula in rate:
        lst_writer.writerow([pelicula[0],pelicula[1]])

