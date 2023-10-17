from csv import list_dialects
from gente.persona import Persona
class Empleado(Persona):
    _numero_empleados=0
    _lista_empleado=[]
    def __init__(self,cedula,nombre,telefono):
        super().__init__(cedula,nombre,telefono)
        self.numero_ventas=0
        self._numero_ventas=0
        Empleado._numero_empleados+=1
        self._numero_asignado=Empleado._numero_empleados
        Empleado._lista_empleado.append(self)
    
    #metodos get
    def getNumero(self):
        return self._numero_asignado
    
    @classmethod
    def getNumero_empleados(cls):
        return Empleado._numero_empleados
    
    def getNumero_ventas(self):
        return self._numero_ventas
    
    @classmethod
    def getListaEmpleado(cls):
        return cls._lista_empleado
    
    #metodos set
    def setNumero_asignado(self,numero_asignado):
        self._numero_asignado=numero_asignado
    
    #otros metodos
    def nuevaVenta(self):
        self._numero_ventas+=1
    
    @classmethod
    def empleado_mas_eficiente(cls):
        ventasporempleado=[]
        for i in Empleado._lista_empleado:
            ventasporempleado.append(i.getNumero_ventas())
        maximo_ventas=max(ventasporempleado)
        for e in range(len(ventasporempleado)):
            if ventasporempleado[e]==maximo_ventas:
                return Empleado._lista_empleado[e]
    
    @classmethod
    def empleado_menos_eficiente(cls):
        ventasporempleado=[]
        for i in Empleado._lista_empleado:
            ventasporempleado.append(i.getNumero_ventas())
        minimo_ventas=min(ventasporempleado)
        for e in range(len(ventasporempleado)):
            if ventasporempleado[e]==minimo_ventas:
                return Empleado._lista_empleado[e]
    
    def informacion(self):
        return f"nombre del Empleado: {self._nombre} \ncedula: {self._cedula} \ntelefono: {self._telefono}\nnumero asignado: {self._numero_asignado} \nnumero de ventas: {self._numero_ventas}"
    
    def info_basi(self):
	    return super().informacion()