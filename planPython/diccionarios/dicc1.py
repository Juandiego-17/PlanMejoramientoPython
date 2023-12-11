
computadores = {
    1 : {
        "ID": 922610128519,
        "Dispositivos": "Cargador y mouse",
        "Ambiente": 1
    },
    2 : {
        "ID" : 922610128501,
        "Dispositivos" : "cargador",
        "Ambiente": 1
    },
    3 : {
        "ID" : 922610128513,
        "Dispositivos" : "mouse",
        "Ambiente": 1
    },
    4 : {
        "ID" : 922610128492,
        "Dispositivos" : "cargador y mouse",
        "Ambiente": 1
    },
    5 : {
        "ID" : 922610128516,
        "Dispositivos" : "mouse",
        "Ambiente": 1
    },
    6 : {
        "ID" : 922610128515,
        "Dispositivos" : "cargador",
        "Ambiente": 1
    },
    7 : {
        "ID" : 922610128522,
        "Dispositivos" : "cargador y mouse",
        "Ambiente": 1
    },
    8 : {
        "ID" : 922610128514,
        "Dispositivos" : "cargador",
        "Ambiente": 1
    },
    9 : {
        "ID" : 922610128517,
        "Dispositivos" : "mouse",
        "Ambiente": 1
    },
    10 : {
        "ID" : 922610128512,
        "Dispositivos" : "cargador y mause",
        "Ambiente": 1
    },
    11 : {
        "ID" : 922610128510,
        "Dispositivos" : "cargador",
        "Ambiente": 1
    },
    12 : {
        "ID" : 922610128511,
        "Dispositivos" : "mouse",
        "Ambiente": 1
    },
    13 : {
        "ID" : 922610128520,
        "Dispositivos" : "cargador y mouse",
        "Ambiente": 1
    },
    14 : {
        "ID" : 922610128521,
        "Dispositivos" : "cargador",
        "Ambiente": 1
    },
    15 : {
        "ID" : 922610128518,
        "Dispositivos" : "mouse",
        "Ambiente": 1
    },
    16 : {
        "ID" : 922610128540,
        "Dispositivos" : "cargador y mouse",
        "Ambiente": 1
    }
}

print(f"{computadores}")
print("-------------------------------------------------------------------------------------------------------------------------------------------")
print()

def agregarNovedad():

    num = int(input("Ingrese el numero del computador: "))
    print()

    fecha = input("Ingresa la fecha de la novedad: ")
    descrip = input("Ingrese la descripcion:")

    computadores[num].update({"Fecha": fecha, "Descripcion": descrip})

    print(f"\nSe añadio la fecha y descripcion al diccionario {num}, {computadores[num]}")
    print()

agregarNovedad()
print("-------------------------------------------------------------------------------------------------------------------------------------------")
print()

def busacarEquipo():

    numId = int(input("Que equipo deseas encontrar por la ID "))

    for pc, idPc in computadores.items():
        
        if idPc["ID"] == numId:
            print(f"el numero del computador es el {pc}: {computadores[pc]}")
        else:
            continue

busacarEquipo()
print("-------------------------------------------------------------------------------------------------------------------------------------------")
print()


def mostrarReportes():

    n = int(input("¿Cual equipo deseas ver? "))

    print(computadores[n])
    print()

mostrarReportes()
print("-------------------------------------------------------------------------------------------------------------------------------------------")
print()


def agregarPC():

    num = int(input("Ingresa el numero del nuevo computador: "))

    numId = int(input("Ingresa la id del computador: "))
    dispo = input("¿Qué tiene el computador teclado o mauseo tienen las 2? ")
    amb = input("¿Cual es el numero del ambiente al que pertenece el pc? ")

    computadores.update({num: {"Id": numId, "Dispositivo": dispo, "Ambiente": amb}})
    print(f"\n{computadores}")

agregarPC()
print("-------------------------------------------------------------------------------------------------------------------------------------------")
print()

def modificar():
  num = int(input(f"Ingrese el numero del computador a modificar: "))

  if num in computadores:
    numID = input("Deseas cambiar el id? (si o no)")
    if numID == 'si':
      n = int(input("Ingresa el nuevo id"))
      computadores[num]["ID"] = n
    else:
      print("No se ha cambiado el ID")

    numDispositivos = input("Deseas cambiar los dispositivos? (si o no)")
    if numDispositivos == 'si':
      n = input("Ingresa los nuevos dispositivos")
      computadores[num]["Dispositivos"] = n
    else:
      print("No se ha cambiado los dispositivos")

    numAmb = (input("Desea cambiar el ambiente (si o no)"))
    if numAmb == 'si':
       n = int(input("Ingresa el numero del nuevo ambiente: "))
       computadores[num]["Ambiente"] = n
    else:
       print("No se cambio el ambiente.")
    print(computadores)
    
  else:
    print("No existe el computador")

modificar()
print("-------------------------------------------------------------------------------------------------------------------------------------------")
print()

def eliminar():
   
   n = int(input("Ingresa el numero del computador que deseas eliminar (debe estar registrado) "))

   eliminado = computadores.pop(n)

   print(f"Se acaba de eliminar el computador numero ({n}) cuyo valor es {eliminado}\n")
   print(computadores)

eliminar()

print("\nGracias por terminar el registro.")