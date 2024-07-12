import random
import csv

Trabajadores=['Juan Perez','Maria Garcia','Carlos Lopez','Ana Martinez','Pedro Rodriguez','Laura Hernandez',
              'Miguel Sanchez','Isabel Gomez','Francisco Diaz','Elena Fernandez']
Sueldos=[]
Asignar_Sueldos=[]
menores800Mil=[]
mayores2millones=[]
entre800Mily2m=[]

def Sueldos_Aleatorios():
    for i in range(0,(len(Trabajadores))):
        sueldo=random.randint(300000,2500000)
        Sueldos.append(sueldo)
        Asignar_Sueldos.append([Trabajadores[i],sueldo])
    return Asignar_Sueldos
def clasificar_sueldo():
    if not Asignar_Sueldos:
        print("No existen sueldos asignados")
    else:
        for i in range(0,(len(Sueldos))):
            if (Asignar_Sueldos[i][1]<800000):
                menores800Mil.append(Asignar_Sueldos[i])
            elif (Asignar_Sueldos[i][1]>=800000 and Asignar_Sueldos[i][1]<=2000000):
                entre800Mily2m.append(Asignar_Sueldos[i])
            elif (Asignar_Sueldos[i][1]>2000000):
                mayores2millones.append(Asignar_Sueldos[i])
        TotalSueldo=sum(Sueldos)
        print(f"Sueldos menores a $800.000 TOTAL: {(len(menores800Mil))} ")
        print(f"Nombre Empleado\t|sueldo")
        for i in range (len(menores800Mil)):
            print(f"{menores800Mil[i]}")
        print(f"Sueldos entre $800.000 y $2.000.000 TOTAl: {(len(entre800Mily2m))} ")
        print(f"Nombre Empleado\t|sueldo")
        for i in range (len(entre800Mily2m)):
            print(f"{entre800Mily2m[i]}")
        print(f"Sueldos superiores a $2.000.000 TOTAL: {(len(mayores2millones))} ")
        print(f"Nombre Empleado\t|sueldo")
        for i in range (len(mayores2millones)):
            print(f"{mayores2millones[i]}")
            print("")
        print(f"TOTAL SUELDOS: ${TotalSueldo}")
        print("="*45)
        
def ver_estadisticas():
    pass

def reporte_sueldo():
    pass

def salir_programa():
    print("Finalizando Programa....")
    print("Desarrolladora Darleen Ortiz.\nRut: 21.969.732-5")
    
print("Bienvenidooooooooo!!")
print("="*45)
while True:
    print("Menu")
    print("1.- Asignar sueldos")
    print("2.- Clasificar sueldos")
    print("3.- Ver estadísticas ")
    print("4.- Reporte de sueldos")
    print("5.- Salir del programa")
    opc=input("=>")
    print("="*45)
    match opc:
        case "1":
            asignarsueldo=Sueldos_Aleatorios()
            print(asignarsueldo)
        case "2":
            clasificar_sueldo()
        case "3":
            pass
        case "4":
            pass
        case "5":
            salir_programa()
            break
print("="*45)