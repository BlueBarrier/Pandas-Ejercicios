import csv
with open("sport_skills.csv",mode="r") as deportes:
    dict_deport=csv.DictReader(deportes,delimiter=",")
    lst_deport=list(dict_deport)
def menu(): #funcion para hacer el menu
    print(""" 
        ______________
        Seleccione una opción
        1. Consultar la dificultad de algun deporte
        2. Ingresar encuesta
        3. Mostrar reporte de la encuesta
        4. Salir
        ______________
    """)
def deportes():
    print("""Lista de deportes
    Basketball
    Martial Arts
    Baseball/Softball
    Soccer
    Volleyball
    Skateboarding
    Table Tennis
    Tennis
    Swimming: Sprints
    Bowling""")


lst_encuesta=[] # iterar lista con diccionario para sacar la cantidad de estudiantes, el deporte que mas se practica y el que mas se quiere aprender 
with open("encuesta_sports.csv",mode="w") as encu:
    header=["Carnet","Estudiante","Carrera","Practica Favorita","Practica Gustaria"]
    writer=csv.DictWriter(encu,fieldnames=header,delimiter=",",lineterminator="\n")
    writer.writeheader()
def encuesta():
    favo=["Basketball","Martial Arts","Baseball/Softball","Soccer","Volleyball","Skateboarding","Table Tennis","Tennis","Swimming: Sprints","Bowling"]
    carnet = int(input("Ingrese su numero de carnet: "))
    nombre = input("¿Cuál es su nombre?  ")
    carrera = input("¿Qué carrera estudia?  ")
    deportes()
    deporte_fav = ""
    while deporte_fav not in favo:
        deporte_gusta = input("De la lista anterior, ingresa el deporte que mas te gusta practicar, ingresa el nombre como aparece en la lista ")
        deporte_fav = deporte_gusta.strip().capitalize()
        deportes()
        deporte_new = ""
    while deporte_new not in favo:
        deporte_nuevo = input("De la lista anterior, ingresa el deporte que mas desearias practicar, ingresa el nombre como aparece en la lista ")
        deporte_new = deporte_nuevo.strip().capitalize()
    with open("encuesta_sports.csv",mode="a") as encu:
        header=["Carnet","Estudiante","Carrera","Practica Favorita","Practica Gustaria"]
        writer=csv.DictWriter(encu,fieldnames=header,delimiter=",",lineterminator="\n")
        writer.writerow({"Carnet":carnet,"Estudiante":nombre,"Carrera":carrera,"Practica Favorita":deporte_fav,"Practica Gustaria":deporte_gusta})
def MostraHabilidades(): 
    favo=["Basketball","Martial Arts","Baseball/Softball","Soccer","Volleyball","Skateboarding","Table Tennis","Tennis","Swimming: Sprints","Bowling"]
    indicadores=["ENDURANCE","STRENGTH","POWER","SPEED","AGILITY","FLEXIBILITY","NERVE","DURABILITY","HAND-EYE","ANALYTIC"]
    for i in lst_deport:
        temp_indi=[]
        if i["SPORT"] in favo:
            for j in range(len(indicadores)):
                temp_indi.append([i[indicadores[j]],indicadores[j]])
            temp_indi.sort(reverse=True)
            print(""" 
                    {}:
                    {}: {}
                    {}: {}
                    {}: {}
                    {}: {}
                    {}: {}
                """.format(i["SPORT"],temp_indi[0][1],temp_indi[0][0],temp_indi[1][1],temp_indi[1][0],temp_indi[2][1],temp_indi[2][0],temp_indi[3][1],temp_indi[3][0],temp_indi[4][1],temp_indi[4][0]))
    
def MostraEncuesta():
    try:
        with open("encuesta_sports.csv",mode="r") as encuread:
            encuesta=csv.DictReader(encuread)
            lst_encuesta=list(encuesta)
        fav_depo=[depo["Practica Favorita"] for depo in lst_encuesta]
        gus_depo=[depo["Practica Gustaria"] for depo in lst_encuesta]
        favo_max=0
        gus_max=0
        for i in range(len(fav_depo)):
            cota_temp=fav_depo.count(fav_depo[i])
            if cota_temp>favo_max:
                favo_max=cota_temp
                depo_fav=fav_depo[i]
        for i in range(len(gus_depo)):
            cota_temp=fav_depo.count(gus_depo[i])
            if cota_temp>gus_max:
                gus_max=cota_temp
                depo_gus=gus_depo[i]
        contador=[estu["Estudiante"] for estu in lst_encuesta]
        print("{} estudiantes realizarón la encuesta.".format(len(contador)))
        print("El deporte que más practican es {}.".format(depo_fav	))
        print("El deporte que más les gustaría practicar es {}.".format(depo_gus))
    except:
        print("No se ha hecho la encuesta")

opcion = 0
while opcion != 4: #menu
    menu()
    opcion=int(input("--> "))
    if opcion == 1:
        MostraHabilidades()
    elif opcion == 2:
        encuesta()
    elif opcion == 3:
        MostraEncuesta()
    elif opcion== 4:
        print("Feliz dia")