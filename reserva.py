#Importar clases necesarias
from cliente import Cliente
from servicio import Servicio

#Importar librería para validar fechas
from datetime import datetime

#Importar errores personalizados
from excepciones import (
    ErrorIdInvalido,
    ErrorOpcionInvalida,
    ErrorValorTiempo
)

#Creación de la clase Reserva
class Reserva:

    def __init__(self, id_reserva, cliente,
                 servicio, fecha, duracion, estado, cantidad):

        #Todos los atributos son privados
        self.id_reserva = id_reserva
        self.cliente = cliente
        self.servicio = servicio
        self.fecha = fecha
        self.duracion = duracion
        self.estado = estado
        self.estado = cantidad
    #Creación de getters y setters usando @property

    @property
    def id_reserva(self):
        return self.__id_reserva

    @id_reserva.setter
    def id_reserva(self, valor):

        #Validar que el ID sea texto
        if not isinstance(valor, str):
            raise ErrorIdInvalido(
                "El ID de reserva debe ser texto"
            )

        #Eliminar espacios innecesarios
        valor = valor.strip()

        #Validar que no esté vacío
        if not valor:
            raise ErrorIdInvalido(
                "El ID de reserva no puede estar vacío"
            )

        #Validar que sea alfanumérico
        if not valor.isalnum():
            raise ErrorIdInvalido(
                "El ID debe ser alfanumérico"
            )

        self.__id_reserva = valor

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, valor):

        #Validar que el objeto sea tipo Cliente
        if not isinstance(valor, Cliente):
            raise ErrorOpcionInvalida(
                "Debe ingresar un cliente válido"
            )

        self.__cliente = valor

    @property
    def servicio(self):
        return self.__servicio

    @servicio.setter
    def servicio(self, valor):

        #Validar que el objeto sea tipo Servicio
        if not isinstance(valor, Servicio):
            raise ErrorOpcionInvalida(
                "Debe ingresar un servicio válido"
            )

        self.__servicio = valor

    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, valor):

        #Validar que la fecha sea texto
        if not isinstance(valor, str):
            raise ErrorValorTiempo(
                "La fecha debe ser texto"
            )

        valor = valor.strip()

        #Validar formato YYYY-MM-DD
        try:
            datetime.strptime(valor, "%Y-%m-%d")

        except ValueError:
            raise ErrorValorTiempo(
                "La fecha debe tener formato YYYY-MM-DD"
            )

        self.__fecha = valor

    @property
    def duracion(self):
        return self.__duracion

    @duracion.setter
    def duracion(self, valor):

        #Validar que duración sea numérica
        if not isinstance(valor, (int, float)):
            raise ErrorValorTiempo(
                "La duración debe ser numérica"
            )

        #Validar que sea positiva
        if valor <= 0:
            raise ErrorValorTiempo(
                "La duración debe ser mayor a 0"
            )

        self.__duracion = valor

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, valor):

        #Validar que el estado sea texto
        if not isinstance(valor, str):
            raise ErrorOpcionInvalida(
                "El estado debe ser texto"
            )

        valor = valor.strip().lower()

        #Lista de estados válidos
        estados_validos = [
            "pendiente",
            "confirmada",
            "cancelada",
            "finalizada"
        ]

        #Validar que el estado exista
        if valor not in estados_validos:
            raise ErrorOpcionInvalida(
                f"Estado inválido. Opciones: {estados_validos}"
            )

        self.__estado = valor

    #Método especial para representación en texto del objeto
    def __str__(self):

        return (
            f"Reserva {self.id_reserva} | "
            f"{self.cliente.nombre} | "
            f"{self.servicio.nombre} | "
            f"{self.fecha}"
        )

    def calcular_total(self):

        return self.servicio.calcular_costo(
            self.duracion
        )