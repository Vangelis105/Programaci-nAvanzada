class Materia:
    id: str
    nombre: str
    descripcion: str
    semestre: int
    creditos: int

    def __init__(self, id:str, nombre: str, descripcion:str, semestre:str, creditos:str):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.semestre = semestre
        self.creditos = creditos



