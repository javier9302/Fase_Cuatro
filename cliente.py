#Creación de la clase cliente
class Cliente:
    def __init__(self, nombre, id, email):
        #Todos los atributos son privados
        self._nombre=nombre
        self._id=id
        self._email=email

    #Creación de setters para los principales atributos 
    def set_nombre(self,nombre):
        self._nombre=nombre

    def set_id(self,id):
        self._id=id

    def set_email(self,email):
        self._email=email

    
    #Creacion de getters

    def get_nombre(self):
        return self._nombre
    
    def get_id(self):
        return self._id
    
    def get_email(self):
        return self._email
    