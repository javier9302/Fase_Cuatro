#Creación de la clase cliente
class Cliente:
    def __init__(self, nombre, id, email):
        #Todos los atributos son privados
        self._nombre=nombre
        self._id=id
        self._email=email

