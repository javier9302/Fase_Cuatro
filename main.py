#Importar la clase Cliente del archivo cliente para usarla en el programa
from cliente import Cliente

clientes=[]

#Pruebas para crear listas de clientes y probar errores comunes.

#Datos correctos

clientes.append(Cliente("Pedro",10123456,"pedro@sucorreo.com"))

#Campo nombre vacío
clientes.append(Cliente("",10123.457,"pedro2@sucorreo.com"))

#Campo correo no cumple con requisitos
clientes.append(Cliente("Pedro",10123458,"pedro3sucorreo.com"))


print(clientes[0])