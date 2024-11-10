
class ProductoInvalidoException(Exception):
  def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
 
class PrecioInvalidoException(Exception):
  def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
 
class CantidadInvalidaException(Exception):
  def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

