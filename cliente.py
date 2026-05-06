#Importar librería para validar patrones. Usada en el email
import re
#Importar errores desde
from excepciones import ErrorEmailInvalido, ErrorNombreInvalido, ErrorIdInvalido

#Creación de la clase cliente
class Cliente:
    def __init__(self, nombre, id, email):
        #Todos los atributos son privados
        self.__nombre=nombre
        self.__id=id
        self.__email=email


    #Creacion de getters y setters usando @property

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,valor):
        #Validar que el valor ingresado sea solamente texto
        if not isinstance(valor, str):
            raise ErrorNombreInvalido("El nombre debe ser texto")

        #Método strip para remover espacios, saltos de línea y/o tabulaciones
        valor = valor.strip()

        #Validar que el campo no esté vacío
        if not valor:
            raise ErrorNombreInvalido("El nombre no puede estar vacío")
        #Validar la longitud del nombre
        if len(valor)<2:
            raise ErrorNombreInvalido("El nombre es demasiado corto")
        
        self.__nombre=valor
        
    @property    
    def id(self):
        return self.__id
    
    @id.setter
    def id(self,valor):
        if not isinstance(valor, int):
            #Validar que sea un entero
            raise ErrorIdInvalido("El ID debe ser un número sin puntos ni comas ni letras")
        if len(valor) <=5 or len(valor)>10:
            #Validar que tenga el campo no sea vacío y tenga la cantidad de dígitos correcta
            raise ErrorIdInvalido("El ID debe tener entre 5 y 10 dígitos")
        
        self.__id=valor

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self,valor):
        #Validar que se use texto en el campo email
        if not isinstance(valor, str):
            raise ErrorEmailInvalido("El email debe ser texto")
        
        #Validar que el campo no esté vacío
        valor=valor.strip().lower()
        if not valor: 
            raise ErrorEmailInvalido("El email no puede estar vacío")
        
        #Validar que el email tenga un formato válido palabra@email.com
        patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(patron,valor):
            raise ErrorEmailInvalido("Formato de email inválido")
        
        self.__email=valor

       
        
    
    
 
    