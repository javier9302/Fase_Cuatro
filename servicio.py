class Servicio:
    def __init__(self, nombre, costo, disponibilidad,estado,id, descripcion):
        self.nombre = nombre
        self.costo = costo
        self.disponibilidad = disponibilidad
        self.estado = estado
        self.id = id
        self.descripcion = descripcion

class Sala(Servicio):
    def __init__(self,nombre,costo, disponibilidad,estado,id, descripcion, capacidad,proyector,tipo):
        super().__init__(nombre, costo, disponibilidad,estado,id, descripcion)
        self.capacidad = capacidad
        self.proyector = proyector
        self.tipo = tipo

class 