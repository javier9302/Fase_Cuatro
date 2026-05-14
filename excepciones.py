class ErrorAplicacion(Exception):
    """Clase base para errores del sistema"""
    
class ErrorValidacion(ErrorAplicacion):
    """Errores relacionados con datos inválidos"""
    pass

class ErrorNombreInvalido(ErrorValidacion):
    pass

class ErrorEmailInvalido(ErrorValidacion):
    pass

class ErrorIdInvalido(ErrorValidacion):
    pass

class ErrorCosto(ErrorValidacion):
    pass

class ErrorValorTiempo(ErrorValidacion):
    pass

class ErrorOpcionInvalida(ErrorValidacion):
    pass

class ErrorTipoInvalido(ErrorValidacion):
    pass

class ErrorDescripcionInvalida(ErrorValidacion):
    pass
class ErrorCantidadInvalida(ErrorValidacion):
    pass