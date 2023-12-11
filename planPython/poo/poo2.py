class coche():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.lecturaOdometro = 0

    def obtenerNombreDescriptivo(self):
        nombreLargo = str(self.ano) + ' ' + self.marca + ' ' + self.modelo
        return nombreLargo.title()
    
    def leerOdometro(self):
        print("Este coche ha recorrido " + str(self.lecturaOdometro) + "Km")

    def actualizarOdometro(self, kilometraje):
        if kilometraje >= self.lecturaOdometro:
            self.lecturaOdometro = kilometraje
        else:
            print("No puedes retroceder el valor del odómetro.")

    def incrementarOdometro(self, kilometros):
        self.lecturaOdometro += kilometros

    def llenarTanqueGas(self):
        print("tanque lleno. ")

class cocheElec(coche):

    def __init__(self, marca, modelo, ano):
        super().__init__(marca,modelo,ano)
        self.kwh = 70
    
    def descripcionBateria(self):
        print("Este coche tiene una bateria de " + str(self.kwh) + "kwh.")

    def llenarTanqueGas(self):
        print("Este coche no necesita un tanque d gasolina.")

miTesla = cocheElec('tesla', 'modelo s', 2022)
print(miTesla.obtenerNombreDescriptivo())
miTesla.descripcionBateria()
miTesla.llenarTanqueGas()

class carro():
    def desplazamiento(self):
        print("Me desplazo utilizando 4 ruedas.")
    
class moto():
    def desplazamiento(self):
        print("Me desplazo utilizando 2 ruedas. ")

class camion():
    def desplazamiento(self):
        print("Me desplazo utilizando 6 ruedas. ")

def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo = camion()

desplazamientoVehiculo(miVehiculo)