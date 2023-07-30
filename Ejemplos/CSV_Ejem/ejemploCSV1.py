import csv

with open('cumpleañosClase.csv') as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Los nombres de las columnas son {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} estudia la carrera de {row[1]}, y su cumpleaños es el {row[2]}.')
            line_count += 1
    print(f'Líneas {line_count} procesadas.')