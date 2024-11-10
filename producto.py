from excepciones import CantidadInvalidaException, PrecioInvalidoException, ProductoInvalidoException



class Producto:
    nombre: str
    precio: float
    cantidad: int
    
    def __init__(self, nombre:str, precio:float, cantidad:int):
        if nombre=="":
            raise ProductoInvalidoException("El nombre del producto no puede estar vacío.")
        if precio <= 0:
            raise PrecioInvalidoException("El precio debe ser mayor a cero.")
        if cantidad < 0:
            raise CantidadInvalidaException("La cantidad no puede ser negativa.")
    
        
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        
    def calcular_valor_total(self):
        valor_total = self.precio*self.cantidad
        return valor_total
    
    def mostrar_detalles_producto(self, valor_total):
        detalles = f"""DETALLES DEL PRODUCTO
        Nombre: {(self.nombre).upper()}
        Precio: ${self.precio}
        Cantidad en inventario: {self.cantidad}
        Valor total: ${valor_total}
        """
        
        return detalles
                       
        
        