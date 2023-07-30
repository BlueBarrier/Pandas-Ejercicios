import csv

#Leer el archivo y transformar los datos en una lista de listas
with open('The Top Billionaires.csv', 'r') as archivo:
    lst_reader = csv.reader(archivo)
    lst_datos = list(lst_reader) #Convertir el reader a una lista de listas

print(lst_datos[1][0])


#Leer el archivo y transformar los datos en una lista de diccionarios
with open('The Top Billionaires.csv', 'r') as archivo:
    dict_reader = csv.DictReader(archivo)
    list_de_dict = list(dict_reader) #Convertir el reader a una lista de diccionarios

print(list_de_dict[0]["NAME"],list_de_dict[3]["NAME"])