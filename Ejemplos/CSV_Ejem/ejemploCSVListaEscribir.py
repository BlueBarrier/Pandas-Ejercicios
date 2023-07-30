import csv

#Leer el archivo y transformar los datos en una lista de diccionarios
with open('The Top Billionaires.csv', 'r') as archivo:
    dict_reader = csv.DictReader(archivo)
    list_de_dict = list(dict_reader)

print(list_de_dict)
#Encuesta si conoce los billonarios del mundo
print("¿Conoces a los siguientes billonarios? Escribe 1 = sí o 0 = no.")
for billonario in list_de_dict:
    respuesta = input(billonario["NAME"]+": ")
    billonario["POPULAR"] = respuesta.strip()
    
#Guardar resultados en otro archivo
with open('Top Billionaires Popularity.csv', mode='w') as archivo_w:
    lst_writer = csv.writer(archivo_w,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL,lineterminator='\n')
    for billonario in list_de_dict:
        lst_writer.writerow([billonario["NAME"],billonario["POPULAR"]])
    
