#Creación de la clase cliente
class Cliente:
    def __init__(self, nombre, id, email):
        #Todos los atributos son privados
        self.__nombre=nombre
        self.__id=id
        self.__email=email


    #Creacion de getters usando @property

    @property
    def nombre(self):
        return self.__nombre
    
    @property    
    def id(self):
        return self.__id
    
    @property
    def email(self):
        return self.__email
    
    #Creación de setters usando @property
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre
    
    @id.setter
    def id(self,valor):
        self.__id=valor
    
    @email.setter
    def email(self,email):
        self.__email=email

    