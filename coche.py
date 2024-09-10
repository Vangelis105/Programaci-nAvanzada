class Coche:
    marca = ""
    modelo = ""
    año = 0
    

    #Método constructor 
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        
    #Primer Método
    def mostrar_informacion(self):
        print("Marca: ", self.marca)
        print("Modelo: ", self.modelo)
        print("Año: ", self.año)

    def calcular_edad_del_coche(self):
        self.edad = (2024 - self.año)
        print("El coche tiene ", self.edad ," años")