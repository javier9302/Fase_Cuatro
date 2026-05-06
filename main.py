#Importar la clase Cliente del archivo cliente para usarla en el programa
from cliente import Cliente
from excepciones import ErrorValidacion
clientes=[]

#*****IMPORTANTE*******
#La siguiente sección se puede eliminar, son solamente pruebas del módulo clientes
#Los encargados de Main y de logs lo pueden usar para realizar pruebas


#Pruebas para crear listas de clientes y probar errores comunes.

#Datos correctos
try: 
    clientes.append(Cliente("Pedro",10123456,"pedro@sucorreo.com"))
except ErrorValidacion as e:
    print("Error:", e)


#Campo nombre vacío
try: 
    clientes.append(Cliente("",10123.457,"pedro2@sucorreo.com"))
except ErrorValidacion as e:
    print("Error:", e)

#Campo correo no cumple con requisitos
try:
    clientes.append(Cliente("Pedro",10123458,"pedro3sucorreo.com"))
except ErrorValidacion as e:
    print("Error:", e)

print(clientes[0])

#Hasta acá se puede eliminar
#Termina pruebas de cliente