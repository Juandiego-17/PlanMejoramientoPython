# Aquí se crearán las listas de aprendices junto con sus edades
aprendices = []
edades = []

# Solicitar los nombres y edades de los aprendices en la formación
while True:
    nomAprendiz = input("Inserta el nombre del aprendiz ('end' para terminar de ingresar): ")
    if nomAprendiz.lower() == 'end':
        break

    edadAprendiz = int(input(f"Inserta la edad del aprendiz {nomAprendiz}: "))

    # Agregar el nombre y la edad a las respectivas listas
    aprendices.append(nomAprendiz)
    edades.append(edadAprendiz)

# Imprimir las listas de los nombres y edades de los aprendices
print("Los nombres de los aprendices en formación son: ", aprendices)
print("Las edades de los aprendices en formación son: ", edades)

# Encontrar el aprendiz con la mayor edad en la formación
if len(edades) > 0:
    maxEdad = edades.index(max(edades))
    mayorEdad = aprendices[maxEdad]
    edadMaxima = max(edades)
    print(f"El aprendiz con la mayor edad es {mayorEdad} con {edadMaxima} años de edad")
else:
    print("No se ingresaron edades, por lo que no se puede determinar al aprendiz con la mayor edad")

# Solicitar el nombre de la instructora y agregarlo a la lista de aprendices en la posición 1.
instructora = input("Nombre de la instructora: ")
aprendices.insert(1, instructora)

# Contar cuántos aprendices tienen 18 años en la lista de edades.
conteoEdad = edades.count(18)
print(f"Hay {conteoEdad} aprendices que tienen 18 años.")

# Agregar el nombre 'andres' a la lista de aprendices.
aprendices.append("andres")

# Eliminar el nombre de la instructora de la lista de aprendices, si existe.
if instructora in aprendices:
    aprendices.remove(instructora)

# Solicitar un dato para buscar en la lista de aprendices y mostrar si se encuentra o no.
datoBusqueda = input("Dato a buscar en la lista de aprendices: ")
if datoBusqueda in aprendices:
    print("El dato", datoBusqueda, "se encuentra en la lista de aprendices.")
else:
    print("El dato", datoBusqueda, "no se encuentra en la lista de aprendices.")

# Mostrar los primeros 10 aprendices de la lista.
print("Los primeros 10 aprendices de la lista son:", aprendices[:10])

# Mostrar los 10 últimos aprendices de la lista.
print("Los 10 últimos aprendices de la lista son:", aprendices[-10:])

# Mostrar los aprendices desde el elemento 10 hasta el elemento 19 de la lista.
print("Los aprendices del elemento 10 al elemento 20 son:", aprendices[9:19])