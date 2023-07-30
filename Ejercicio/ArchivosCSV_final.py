import csv,os

with open("Ejercicio/sport_skills.csv",mode="r") as deportes:
    dict_deport=csv.DictReader(deportes,delimiter=",")
    lst_deport=list(dict_deport)

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

os.chdir("/Ejercicio")
with open("encuesta_sports.csv","w") as archi_depo:
    headers=["SPORT","ENDURANCE","STRENGTH","POWER","SPEED","AGILITY","FLEXIBILITY","NERVE","DURABILITY","HAND-EYE","ANALYTIC","TOTAL"]
    favo=["Basketball","Martial Arts","Baseball/Softball","Soccer","Volleyball","Skateboarding","Table Tennis","Tennis","Swimming: Sprints","Bowling"]
    writer=csv.DictWriter(archi_depo,fieldnames=headers,lineterminator="\n")
    writer.writeheader()
    for i in lst_deport:
        if i["SPORT"] in favo:
            writer.writerow({"SPORT":i["SPORT"],"ENDURANCE":i["ENDURANCE"],"STRENGTH":i["STRENGTH"],"POWER":i["POWER"],"SPEED":i["SPEED"],"AGILITY":i["AGILITY"],"FLEXIBILITY":i["FLEXIBILITY"],"NERVE":i["NERVE"],"DURABILITY":i["DURABILITY"],"HAND-EYE":i["HAND-EYE"],"ANALYTIC":i["ANALYTIC"],"TOTAL":i["TOTAL"]})

lst_encuesta=[]
def encuesta():
    favo=["Basketball","Martial Arts","Baseball/Softball","Soccer","Volleyball","Skateboarding","Table Tennis","Tennis","Swimming: Sprints","Bowling"]
    carnet = int(input("Ingrese su numero de carnet"))
    nombre = input("¿Cual es su nombre?")
    carrera = input("¿Que carrera estudia?")
    deportes()
    deporte_fav = ""
    while deporte_fav not in favo:
        deporte_gusta = input("De la lista anterior, ingresa el deporte que mas te gusta practicar, ingresa el nombre como aparece en la lista")
        deporte_fav = deporte_gusta.strip().capitalize()
    deportes()
    deporte_new = ""
    while deporte_new not in favo:
        deporte_nuevo = input("De la lista anterior, ingresa el deporte que mas desearias practicar, ingresa el nombre como aparece en la lista")
        deporte_new = deporte_nuevo.strip().capitalize()
    lst_encuesta.append({})