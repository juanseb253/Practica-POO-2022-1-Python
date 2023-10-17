from gente.persona import Persona
from gente.empleado import Empleado
class Gerente(Persona):
	_list_gerente=[] #una lista que contiene al gerente
	def __init__(self,cedula,nombre,telefono,contrasena):
		super().__init__(cedula,nombre,telefono)
		self._contrasena=contrasena
		if len(Gerente._list_gerente)==1:
			Gerente._list_gerente[0]=self
		else:
			Gerente._list_gerente.append(self)

	#metodos get

	def getContrasena(self):
		return self._contrasena
	
	#metodos set
	
	def setContrasena(self,contrasena):
		self._contrasena=contrasena

	#otros metodos
	@classmethod
	def contratar_Empleado(cls,cedula,nombre,telefono):
		Empleado(cedula,nombre,telefono)
	
	@classmethod
	def despedir_Empleado(cls,numero_empleado):
		n=1
		if numero_empleado<=len(Empleado._lista_empleado) and numero_empleado>0:
			info=Empleado._lista_empleado[numero_empleado-1].informacion()
			Empleado._lista_empleado.pop(numero_empleado-1)
			
			for i in Empleado._lista_empleado:
				i.setNumero_asignado(n)
				n+=1
			Empleado._numero_empleados-=1
			return "se despidio al empleado con la siguiente informacion: \n"+info
		else:
			return "error este empleado no esta en la lista de empleados"
	@classmethod
	def despido_inteligente(cls):
		return Gerente.despedir_Empleado(Empleado.empleado_menos_eficiente().getNumero())
	
	def informacion(self):
		return f"nombre del Gerente: {self._nombre} \ncedula: {self._cedula} \ntelefono: {self._telefono}"