"""
Universidad del Valle de Guatemala
Facultad de Ingeniería
Departamento de Ciencias de la Computación
CC 2005 - Algoritmos y Programación Básica
Daniel Barrera - 231238

                Ejercicio 5 - MEA - Pandas
"""
import pandas as pd
import matplotlib.pyplot as plt
import os

def clear_console(): # limpia pantalla
    if os.name=="nt":
        os.system("cls")
    else:
        os.system("clear")

df=pd.read_csv("video_games_sales.csv")

def EmpAn(): # filtro empresa y año
    print(""" 
    ----Lista de las Top 5 empresas----
        1. Electronic Arts
        2. Nintendo
        3. Sony Computer Entertainment
        4. Activision
        5. Take-Two Interactive

Ingrese el número de la empresa que desee analizar
    """)
    try:
        empresa=int(input("--> "))
        empre_list=["Electronic Arts","Nintendo","Sony Computer Entertainment","Activision","Take-Two Interactive"]
        print("\n Seleccione un año entre 1980 y 2020")
        year=float(input("--> "))  
    except ValueError:
        print("Ingrese un valor por favor.")
        EmpAn()
    if empresa<=len(empre_list) and empresa>=1:
        filtro_empre=df[df["publisher"]==empre_list[empresa-1]][["name","year","global_sales"]]
        if year<= 2020.00 and year>=1980.00:
            filtro_year=filtro_empre[df["year"]==year][["name","global_sales","year"]].reset_index().sort_values(by="global_sales",ascending=False)
            print(filtro_year.head())
        else:
            print("El año ingresado esta fuera de rango")
            EmpAn()
    else:
        print("La opción seleccionada no existe.")
        EmpAn()

def Rango(): # filtro rango año
    try:
        print("\n Seleccione un año entre 1980 y 2020, menor a 2020")
        year_1=float(input("--> "))
        print("\n Seleccione otro año entre {} y 2020".format(int(year_1)))
        year_2=float(input("--> "))
        filtro_rango=(df["year"]>=year_1) & (df["year"]<=year_2)
    except ValueError:
        print("Ingrese un valor por favor.")
        Rango()
    if year_1<= 2020.00 and year_1>=1980.00:
        if year_1<= year_2 and year_2<=2020.00:
            filtro_rangan=df.loc[filtro_rango].groupby("genre")["genre"]
            rangan_graph=filtro_rangan.value_counts().plot(kind="bar")
            plt.show()
        else:
            print("El segundo año ingresado es menor que {:.0f} o es mayor que 2020".format(year_1))
            Rango()
    else:
        print("El año ingresado es menor que 1980 o es mayor que 2020")
        Rango()

def Region(): # filtro región
    print(""" 
    Ingrese la región que desee visualizar 
        1. Norte América
        2. Japón
        3. Europa
        4. Otro
        5. Global  
    """)
    try:
        regi=int(input("--> "))
        regiones=["na_sales","jp_sales","eu_sales","other_sales","global_sales"]
        print("\nIngrese un año entre 1980 y 2020.")
        year=float(input("--> "))
    except ValueError:
        print("Por favor ingrese lo solicitado.")
        Region()
    if regi<=len(regiones) and regi>=1:
        if year<= 2020.00 and year>=1980.00:
            filtro_regi=df[df["year"]==year][["name",regiones[regi-1],"year"]].sort_values(by=regiones[regi-1],ascending=False)
            print(filtro_regi.head())
        else:
            print("El año ingresado esta fuera de rango.")
            Region()
    else:
        print("La opción seleccionada no existe.")
        Region()

def Menu():
    print(""" 
____________________________
            Menu
    1. Filtrar datos
    2. Mostrar gráficas
    3. Encuesta 
    4. Salir
____________________________
    """)

def filtros(): # menu de filtros
    print("""
___________________________________________
    Seleccione el filtro que desee usar

    1. Por región y año
    2. Por rango de años
    3. Por empresa y año

(Ingrese el número de la opción)
___________________________________________
    """)
    try:
        opcion=int(input("--> "))
        if opcion == 1:
            clear_console()
            Region()
        elif opcion == 2:
            clear_console()
            Rango()
        elif opcion==3:
            clear_console()
            EmpAn()
        else:
            clear_console()
            print("La opción ingresada no existe")
            filtros()
    except ValueError:
        print("Ingrese una opción por favor.")
        filtros()

def Encuesta(): # Encuesta de usuario 
    print("""
__________________________________________________
        ¡Bienvenido a la encuesta!
Por favor ingrese los campos que se le soliciten. 
__________________________________________________
""")
    try:
        fav_genre=input("Ingrese el género de su videojuego favorito: ")
        fav_genre=fav_genre.title().strip().replace(" ","")
        consola=input("Ingrese su consola/plataforma que más usa: ")
        consola=consola.title().strip().replace(" ","")
        horas=int(input("Ingrese el número de horas que invierte al día jugando: "))
    except ValueError:
        print("Por favor ingrese su respuesta.")
        Encuesta()
    def horasbool(numero): # comprueba si es entero o no
        try: 
            int(numero)
            return True
        except:
            return False
    def llenaEncuesta(): # llena la encuesta a un csv
        datos_usuario={"fav_genre":fav_genre,"consola_user":consola,"horas_al_dia":horas}
        df_usuario=pd.DataFrame([datos_usuario])
        try: # si ya existe
            pd.read_csv("encuesta_user.csv")
            df_usuario.to_csv("encuesta_user.csv",mode="a",header=False,index=False,na_rep="NaN")
        except: # si no existe 
            df_usuario.to_csv("encuesta_user.csv",header=True,index=False,lineterminator="\n",na_rep="NaN")
    while horasbool(horas)==False:
        print("El número ingresado no es un entero.")
        horas=int(input("Ingrese el número de horas que invierte al día jugando: "))
        if horasbool(horas) == True:
            llenaEncuesta()
    else:
        llenaEncuesta()

def Graph():
    try:
        df_usuario=pd.read_csv("encuesta_user.csv")
        figura=plt.figure("Gráficas",figsize=(10,6))
        figura.subplots_adjust(hspace=0.5,wspace=0.5)
        ax_1=figura.add_subplot(2,2,1)
        ax_2=figura.add_subplot(2,2,2)
        ax_3=figura.add_subplot(2,2,3)
        fav_graph=df_usuario["fav_genre"].value_counts().plot(kind="pie",title="Género de videojuegos favoritos",ylabel="",legend=False,ax=ax_1)
        consola_graph=df_usuario["consola_user"].value_counts().plot(kind="bar",xlabel="Consola",ylabel="Cantidad",title="Consolas favoritas",ax=ax_2)
        horas_graph=ax_3.hist(df_usuario["horas_al_dia"])
        ax_3.set_xlabel("Horas del día")
        ax_3.set_ylabel("Cantidad")
        plt.show()
    except:
        print("La base de datos no existe o esta vacía.")

def init():
    opcion=0
    while opcion!=4:
        Menu()
        try:
            opcion=int(input("--> "))
            if opcion==1:
                clear_console()
                filtros()
            elif opcion==2:
                clear_console()
                Graph()
            elif opcion==3:
                clear_console()
                Encuesta()
            elif opcion==4:
                print("¡Feliz día!")
            else:
                print("opción invalida")
        except ValueError:
            print("Por favor ingrese un valor.")
            init()
init()
    