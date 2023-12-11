class perro():
    def __init__(self, nombre, edad): 
        self.nombre = nombre
        self.edad = edad
    
    def sentarse(self):
        print(self.nombre.title() + " Se ha sentado ")
    
    def rodar(self):
        print(self.nombre.title() + " rodó en el piso. ")

miPerro = perro("willie", 6)
tuPerro = perro("Lucy", 3)

print("Mi perro se llama" + miPerro.nombre.title() + ".")
print("Mi perro tiene " + str(miPerro.edad) + "años de edad.")

miPerro.sentarse()
miPerro.rodar()
print()
print("Tu perro se llama" + tuPerro.nombre.title() + ".")
print("Tu perro tiene " + str(tuPerro.edad) + "años de edad.")

tuPerro.sentarse() 
tuPerro.rodar()

