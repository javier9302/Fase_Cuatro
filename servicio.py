#Importar errores desde excepciones.py
from excepciones import ErrorNombreInvalido, ErrorCosto, ErrorIdInvalido, ErrorValorTiempo, ErrorOpcionInvalida, ErrorTipoInvalido, ErrorDescripcionInvalida, ErrorCantidadInvalida

class Servicio:

    ESTADOS_VALIDOS = ["activo", "mantenimiento", "dañado"]
    MODALIDADES_VALIDAS = ["presencial", "virtual", "hibrida" ]
    
    def __init__(self, nombre, costo, disponible,
                 estado, id_servicio, tipo, descripcion):

        self.nombre = nombre
        self.costo = costo
        self.disponible = disponible
        self.estado = estado
        self.id_servicio = id_servicio
        self.tipo = tipo
        self.descripcion = descripcion

    # ---------------- NOMBRE ----------------

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):

        if not isinstance(valor, str):
            raise ErrorNombreInvalido("El nombre debe ser texto")

        if len(valor.strip()) < 3:
            raise ErrorNombreInvalido("El nombre es demasiado corto")

        if not valor.replace(" ", "").isalpha():
            raise ErrorNombreInvalido(
                "El nombre solo debe contener letras y espacios"
            )

        self._nombre = valor

    # ---------------- COSTO ----------------

    @property
    def costo(self):
        return self._costo

    @costo.setter
    def costo(self, valor):

        if not isinstance(valor, (int, float)):
            raise ErrorCosto("El costo debe ser numérico")

        if valor < 0:
            raise ErrorCosto("El costo no puede ser negativo")

        self._costo = valor

    # ---------------- DISPONIBLE ----------------

    @property
    def disponible(self):
        return self._disponible

    @disponible.setter
    def disponible(self, valor):
        if isinstance(valor, str):

            valor = valor.lower().strip()

            if valor == "si":
                valor = True

            elif valor == "no":
                valor = False
        
        if not isinstance(valor, bool):
            raise ErrorOpcionInvalida("Disponible debe ser 'Si' o 'No'")
        self._disponible = valor

    # ---------------- ESTADO ----------------

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, valor):

        if valor.lower() not in self.ESTADOS_VALIDOS:
            raise ValueError(
                f"Estado inválido. Use: {self.ESTADOS_VALIDOS}"
            )

        self._estado = valor.lower()

    # ---------------- ID ----------------

    @property
    def id_servicio(self):
        return self._id_servicio

    @id_servicio.setter
    def id_servicio(self, valor):

        if not valor:
            raise ErrorIdInvalido("EL ID no puede estar vacío")

        if not valor.isalnum():
            raise ErrorNombreInvalido("El ID no puede contener caracteres especiales")
        
        
        self._id_servicio = valor

    # ---------------- TIPO ----------------

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, valor):

        if not isinstance(valor, str):
            raise ErrorTipoInvalido("El tipo debe ser texto")

        if len(valor.strip()) == 0:
            raise ErrorTipoInvalido("El tipo no puede estar vacío")

        self._tipo = valor

    # ---------------- DESCRIPCIÓN ----------------

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, valor):

        if not isinstance(valor, str):
            raise ErrorDescripcionInvalida("La descripción debe ser texto")

        if len(valor.strip()) < 10:
            raise ErrorDescripcionInvalida(
                "La descripción debe tener al menos 10 caracteres"
            )

        self._descripcion = valor

# ---------------- SERVICIO SALA ----------------
class Sala(Servicio):
    def __init__(self,nombre,costo, disponibilidad,estado,id,tipo, descripcion, capacidad,proyector):
        super().__init__(nombre, costo, disponibilidad,estado,id,tipo, descripcion)
        self.capacidad = capacidad
        self.proyector = proyector
        
    @property
    def capacidad(self):
        return self._capacidad

    @capacidad.setter
    def capacidad(self, valor):

        if not isinstance(valor, int):
            raise ErrorValorTiempo(
                "La capacidad debe ser un número entero"
            )

        if valor <= 0:
            raise ErrorValorTiempo(
                "La capacidad debe ser mayor a 0"
            )

        self._capacidad = valor
    @property
    def proyector(self):
        return self._proyector

    @proyector.setter
    def proyector(self, valor):

        if isinstance(valor, str):

            valor = valor.lower().strip()

            if valor == "si":
                valor = True

            elif valor == "no":
                valor = False

        if not isinstance(valor, bool):
            raise ErrorOpcionInvalida(
                "Proyector debe ser si/no"
            )

        self._proyector = valor

# ----------------SERVICIO EQUIPO ----------------
class Equipo(Servicio):
    def __init__(self,nombre,costo, disponibilidad,estado,id, tipo, descripcion, marca, serial, cantidad,):
        super().__init__(nombre, costo, disponibilidad,estado,id, tipo, descripcion)    
        self.marca=marca
        self.serial=serial
        self.cantidad=cantidad
        
     # ---------------- MARCA ----------------

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, valor):

        if not isinstance(valor, str):
            raise ErrorNombreInvalido(
                "La marca debe ser texto"
            )

        if len(valor.strip()) == 0:
            raise ErrorNombreInvalido(
                "La marca no puede estar vacía"
            )

        self._marca = valor

    # ---------------- SERIAL ----------------

    @property
    def serial(self):
        return self._serial

    @serial.setter
    def serial(self, valor):

        if not isinstance(valor, str):
            raise ErrorIdInvalido(
                "El serial debe ser texto"
            )

        valor = valor.strip()

        if len(valor) == 0:
            raise ErrorIdInvalido(
                "El serial no puede estar vacío"
            )

        if not valor.isalnum():
            raise ErrorIdInvalido(
                "El serial debe ser alfanumérico"
            )

        self._serial = valor

    # ---------------- CANTIDAD ----------------

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor):

        if not isinstance(valor, int):
            raise ErrorCantidadInvalida(
                "La cantidad debe ser un número entero"
            )

        if valor < 0:
            raise ErrorCantidadInvalida(
                "La cantidad no puede ser negativa"
            )

        self._cantidad = valor
# ---------------- SERVICIO ASESORIA ----------------
class Asesoria(Servicio):
    def __init__(self, nombre,costo, disponibilidad,estado,id, tipo, descripcion, modalidad,duracion,asesor):
        super().__init__(nombre, costo, disponibilidad,estado,id, tipo, descripcion)
        self.modalidad = modalidad
        self.duracion = duracion
        self.asesor = asesor

    # ---------------- MODALIDAD ----------------

    @property
    def modalidad(self):
        return self._modalidad

    @modalidad.setter
    def modalidad(self, valor):

        if not isinstance(valor, str):
            raise ErrorOpcionInvalida(
                "La modalidad debe ser texto"
            )

        valor = valor.lower().strip()

        if valor not in self.MODALIDADES_VALIDAS:
            raise ErrorOpcionInvalida(
                f"Modalidad inválida. Opciones: {self.MODALIDADES_VALIDAS}"
            )

        self._modalidad = valor

    # ---------------- DURACION ----------------

    @property
    def duracion(self):
        return self._duracion

    @duracion.setter
    def duracion(self, valor):

        if not isinstance(valor, (int, float)):
            raise ErrorValorTiempo(
                "La duración debe ser numérica"
            )

        if valor <= 0:
            raise ErrorValorTiempo(
                "La duración debe ser mayor a 0"
            )

        self._duracion = valor

    # ---------------- ASESOR ----------------

    @property
    def asesor(self):
        return self._asesor

    @asesor.setter
    def asesor(self, valor):

        if not isinstance(valor, str):
            raise ErrorNombreInvalido(
                "El nombre del asesor debe ser texto"
            )

        valor = valor.strip()

        if len(valor) == 0:
            raise ErrorNombreInvalido(
                "El asesor no puede estar vacío"
            )

        if not valor.replace(" ", "").isalpha():
            raise ErrorNombreInvalido(
                "El asesor solo debe contener letras"
            )

        self._asesor = valor