from excepciones.erroaplicacion import ErrorAplicacion
class ErrorFormato(ErrorAplicacion):

    def __init__(self, mensaje):
        self.mensaje_error_fromato = " Error por formato " + mensaje 
        super().__init__(self.mensaje_error_fromato)

class ExcepcionStringNumero(ErrorFormato):
    def __init__(self,valor):
        self.mensaje_error = f"la entrada {valor} tiene digitos y deberia estar compuesta por una cadena de texto."
        super().__init__(self.mensaje_error)

class ExcepcionEnteroString(ErrorFormato):
    def __init__(self,valor):
        self.mensaje_error=f"\n{valor} es un texto, por favor modifiquelo a un numero entero." 
        super().__init__(self.mensaje_error)

class ExcepcionEmpleado(ErrorFormato):
    def __init__(self,valor):
        self.mensaje_error = f'\n{valor} no hay empleados, por favor agrege nuevos empleados desde la seccion "contratar"'

class ExcepcionInv(ErrorFormato):
    def __init__(self,valor):
        self.mensaje_error = f'\n{valor} no hay ingredientes, por favor agrege nuevos ingredientes desde la seccion "agregar ingredientes"'
