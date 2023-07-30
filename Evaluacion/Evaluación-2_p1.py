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

D2021=pd.read_csv("Visitas_2021.csv") # lee 2021
D2022=pd.read_csv("Visitas_2022.csv") # lee 2022

TempDf=pd.concat([D2021,D2022]) # Junta los DataFrame
TempDf.to_csv("visitas_db.csv",index=False) # Escribre el csv nuevo

df=pd.read_csv("visitas_db.csv") # Lee el csv nuevo

def ModData(datos):
    filtro=((df["Origen"] == datos["origen"]) & (df["Tipo"] == datos["tipo"]) & (df["Jornada"] == datos["jornada"] & df["Anio"] == datos["anio"]))
    mod=df.loc[filtro,:]
    mod["Enero":"Diciembre"]=datos["visitas"]

def NewData():
    data={}
    origen=input("Ingrese el origen: ")
    tipo=input("Ingrese el tipo (Hombre, Mujer, Ninio(a)): ")
    jornada=input("Ingrese la joranada: ")
    anio=int(input("Ingrese el año: "))
    print("""
    Ingrese las visitas de enero a diciembre separados por una coma
    Ejemplo: 1,2,3,4,5,6,7,8,9,10,11,12
    """)
    visitas=input("--> ")
    visitas.rsplit(sep=",")
    try:
        visitas= [ int(i) for i in visitas]
    except:
        print("Las visitas ingresadas no son correctas")
        NewData()
    origen=origen.capitalize()
    tipo=tipo.capitalize()
    jornada=jornada.capitalize()
    data["origen"]=origen
    data["tipo"]=tipo
    data["jornada"]=jornada
    data["anio"]=anio
    data["visitas"]=visitas
    try:
        ModData(data)
        print("Datos modificados")
    except:
        global df
        df_new={"Origen":data["origen"],"Tipo":data["tipo"],"Jornada":data["jornada"],"Anio":data["anio"],"Enero":data["anio"][0],"Febrero":data["anio"][1],"Marzo":data["anio"][2],"Abril":data["anio"][3],"Mayo":data["anio"][4],"Junio":data["anio"][5],"Julio":data["anio"][6],"Agosto":data["anio"][7],"Septiembre":data["anio"][8],"Octubre":data["anio"][9],"Noviembre":data["anio"][10],"Diciembre":data["anio"][11]}
        df_new=pd.DataFrame(df_new,index=False)
        df=pd.concat([df,df_new])
        df.to_csv("visitas_db.csv",index=False)
        df=pd.read_csv("visitas_db.csv")
        print("Datos agregados")

def RepoAnio():
    anio=int(input("Ingrese año: "))
    repo_an=df.loc[df["Anio"]==anio,:].groupby(["Origen","Tipo"])[["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]].sum().sum(axis=1)
    print(repo_an)

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
        4. Salir
""")
    

op=0
while op!=4:
    menu()
    op=int(input("--> "))
    if op==1:
        NewData()
    elif op==2:
        RepoAnio()
    elif op==3:
        RepoTipo()
    else:
        print("Feliz día")
