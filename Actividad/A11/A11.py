"""
Universidad del Valle de Guatemala
Algortimos y programación básica


                    Actividad 11

Daniel Barrera 231238
Javier Valladares 23045

"""

import csv

#Leer el archivo y transformar los datos en una lista de diccionarios
with open('mcu_box_office.csv', 'r') as archivo:
    dict_reader = csv.DictReader(archivo)
    list_de_dict = list(dict_reader)

print("¿Que fase quieres ver?")
aw=int(input("--> "))
if aw == 1:
    for fase in list_de_dict:
        if fase["mcu_phase"] == "1":
            print("Fase:{} Película: {} Fecha de lanzamiento: {} Presupuesto: {}".format(fase["mcu_phase"],fase["movie_title"],fase["release_date"],fase["production_budget"]))
elif aw == 2: 
    for fase in list_de_dict:
        if fase["mcu_phase"] == "2":
            print("Fase:{} Película: {} Fecha de lanzamiento: {} Presupuesto: {}".format(fase["mcu_phase"],fase["movie_title"],fase["release_date"],fase["production_budget"]))
elif aw == 3: 
    for fase in list_de_dict:
        if fase["mcu_phase"] == "3":
            print("Fase:{} Película: {} Fecha de lanzamiento: {} Presupuesto: {}".format(fase["mcu_phase"],fase["movie_title"],fase["release_date"],fase["production_budget"]))
elif aw == 4: 
    for fase in list_de_dict:
        if fase["mcu_phase"] == "4":
            print("Fase:{} Película: {} Fecha de lanzamiento: {} Presupuesto: {}".format(fase["mcu_phase"],fase["movie_title"],fase["release_date"],fase["production_budget"]))
