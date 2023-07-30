"""
Universidad del Valle de Guatemala
Facultad de Ingeniería
Departamento de Ciencias de la Computación
CC 2005 - Algoritmos y Programación Básica
Daniel Barrera - 231238

                Evaluación Individual 2 

Recursos: 
     - Unir los dataframe: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html
"""
import pandas as pd
import matplotlib.pyplot as plt

D2021=pd.read_csv("Visitas_2021.csv") # lee 2021
D2022=pd.read_csv("Visitas_2022.csv") # lee 2022

TempDf=pd.concat([D2021,D2022]) # Junta los DataFrame
TempDf.to_csv("visitas_db.csv",index=False) # Escribre el csv nuevo
df=pd.read_csv("visitas_db.csv") # Lee el csv nuevo

def ModData(datos):
    filtro=((df["Origen"] == datos["origen"]) & (df["Tipo"] == datos["tipo"]) & (df["Jornada"] == datos["jornada"]) & (df["Anio"] == datos["anio"]))
    print(filtro)
    df.loc[filtro,"Enero":"Diciembre"]=datos["visitas"]
    df.to_csv("visitas_db.csv",index=False)


def NewData():
    global df
    data={}
    origen=["Local","Extranjero"]
    tipo=["Hombre","Mujer","Ninio(a)"]
    jornada=["Matutina","Nocturna","Vespertina"]
    print("""
    Seleccione un origen: 
        1. Local
        2. Extranjero
""")
    try:
        Op_origen=int(input("--> "))
    except ValueError:
        NewData()
    try:
        origen=origen[Op_origen-1]
    except IndexError:
        print("Opción no valida")
        NewData()
    print("""
    Seleccione un Tipo: 
        1. Hombre
        2. Mujer
        3. Ninio(a)
""")
    try:
        Op_tipo=int(input("--> "))
    except ValueError:
        NewData()
    try:
        tipo=tipo[Op_tipo-1]
    except IndexError:
        print("Opción no valida")
        NewData()
    print("""
    Seleccione una jornada: 
        1. Matutina
        2. Nocturna
        3. Vespertina
""")
    try:
        Op_jornada=int(input("--> "))
    except ValueError:
        NewData()
    try:
        jornada=jornada[Op_jornada-1]
    except IndexError:
        print("Opción no valida")    
        NewData()
    try:
        anio=int(input("Ingrese el año: "))
    except ValueError:
        NewData()
    print("""
    Ingrese las visitas de enero a diciembre separados por una coma
    Ejemplo: 1,2,3,4,5,6,7,8,9,10,11,12
    """)
    visitas=input("--> ")
    visitas=visitas.rsplit(sep=",")
    if len(visitas)==12:
        try:
            visitas= [ int(i) for i in visitas]
        except:
            print("Las visitas ingresadas no son correctas")
            NewData()    
    else:
        print("Faltan/sobran visitas")
        NewData()
    
    data["origen"]=origen
    data["tipo"]=tipo
    data["jornada"]=jornada
    data["anio"]=anio
    data["visitas"]=visitas
    filtro=((df["Origen"] == data["origen"]) & (df["Tipo"] == data["tipo"]) & (df["Jornada"] == data["jornada"]) & (df["Anio"] == data["anio"]))
    if filtro.any():
            ModData(data)
            print("Datos modificados")
    else:
        df_new={"Origen":data["origen"],"Tipo":data["tipo"],"Jornada":data["jornada"],"Anio":data["anio"],"Enero":data["visitas"][0],"Febrero":data["visitas"][1],"Marzo":data["visitas"][2],"Abril":data["visitas"][3],"Mayo":data["visitas"][4],"Junio":data["visitas"][5],"Julio":data["visitas"][6],"Agosto":data["visitas"][7],"Septiembre":data["visitas"][8],"Octubre":data["visitas"][9],"Noviembre":data["visitas"][10],"Diciembre":data["visitas"][11]}
        df_new=pd.DataFrame([df_new],index=None)
        df=pd.concat([df,df_new])
        df.to_csv("visitas_db.csv",index=False)
        df=pd.read_csv("visitas_db.csv")
        print("Datos agregados")

def RepoAnio():
    try:
        anio=int(input("Ingrese año: "))
        repo_an=df.loc[df["Anio"]==anio,:].groupby(["Origen","Tipo"])[["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]].sum().sum(axis=1)
        print(repo_an)
    except:
        print("Año ingresado incorrectamente")
        RepoAnio()
    
def RepoTipo():
    tipo=input("Ingrese el tipo (Hombre, Mujer, Ninio(a)): ")
    tipo=tipo.capitalize()
    repo=df.loc[df["Tipo"]==tipo,"Enero":"Diciembre"].sum()
    print(repo)

def menu():
    print("""
_______________________________
        Opciones
        1. Agregar datos
        2. Reporte por año
        3. Reporte por tipo
        4. Gráfica de barras
        5. Gráfica de Pie
        6. Salir
""")
    
# Parte 2
def GraphBar():
    anio=int(input("Ingrese el año: "))
    graph=df.loc[df["Anio"]==anio,"Enero":"Diciembre"].sum().plot(kind="bar",xlabel="Meses",ylabel="Visitantes",title=f"Gráfica año {anio}")
    plt.show()

def GraphPie():
    anio=int(input("Ingrese el año: "))
    graph=df.loc[df["Anio"]==anio,:].groupby(["Origen"])[["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]].sum().sum(axis=1).plot.pie(title=f"Gráfica año {anio}",autopct="%.2f")
    plt.show()

op=0
while op!=6:
    menu()
    op=int(input("--> "))
    if op==1:
        NewData()
    elif op==2:
        RepoAnio()
    elif op==3:
        RepoTipo()
    elif op == 4:
        GraphBar()
    elif op == 5:
        GraphPie()
    else:
        print("Feliz día")

"""
Análisis:
Como podemos ver en las gráficas de barras por año, de Abril a Junio y Septiembre son meses donde 
la cantidad de visitantes baja. Por lo que podría considerarse aumentar la publicidad en esos meses o 
incentivar actividades relacionadas con días festivos en esos meses. Además, vemos que el origen de las
visitas es casi mitad de locales y mitad de extranjeros; pero vemos una inclinación hacie el extranjero.
Por lo que se podría iniciar una campaña de publicidad bilingüe para atraer más público extranjero y local.

Además, notamos una tendencia en el tipo y origen de los visitantes:
Para origen extranjero: la mayoria es hombres y niñ@s
Para origen local: la mayoria es mujeres
Se podría enfocar o idear actividades que promuevan otro tipo de visitantes de los diferentes origenes.

El programa se presenta de esa forma para poder analizar de una manera correcta la cantidad de público que entra
al parque. Las gráficas de barras son un buen indicador para las visitas por mes y su tendencia a lo largo de los años.
La gráfica de pie ayudará a verificar el origen de estas visitas y si su tendencia cambia con la publicidad realizada.
"""