class Circulo:
    
    radio = 0
    
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        print("\nRadio del circulo: ",self.radio)
        area = (3.1416) * (self.radio) * (self.radio)
        print("El area del circulo es: ", area)
    
    def calcular_perimetro(self):
        perimetro = 2 * (3.1416) * self.radio
        print("El perimetro es: ", perimetro)
    
