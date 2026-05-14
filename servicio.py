class Servicio:
    def __init__(self, nombre, costo, disponibilidad,estado,id, tipo, descripcion):
        self.nombre = nombre
        self.costo = costo
        self.disponibilidad = disponibilidad
        self.estado = estado
        self.id = id
        self.tipo = tipo
        self.descripcion = descripcion
        

class Sala(Servicio):
    def __init__(self,nombre,costo, disponibilidad,estado,id,tipo, descripcion, capacidad,proyector):
        super().__init__(nombre, costo, disponibilidad,estado,id,tipo, descripcion)
        self.capacidad = capacidad
        self.proyector = proyector
        

class Equipo(Servicio):
    def __init__(self,nombre,costo, disponibilidad,estado,id, descripcion, tipo, marca, serial, cantidad,):
        super().__init__(nombre, costo, disponibilidad,estado,id, descripcion, tipo )    
        self.marca=marca
        self.serial=serial
        self.cantidad=cantidad
        

class Asesoria(Servicio):
    def __init__(self, nombre,costo, disponibilidad,estado,id, descripcion, tipo, modalidad,duracion,asesor):
        super().__init__(nombre, costo, disponibilidad,estado,id, descripcion, tipo)
        self.modalidad = modalidad
        self.duracion = duracion
        self.asesor = asesor