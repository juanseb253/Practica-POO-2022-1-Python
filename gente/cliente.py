from gente.persona import Persona
class Cliente(Persona):
	_lista_socio=[]
	def __init__(self,cedula,nombre,telefono):
		super().__init__(cedula, nombre,telefono)
	
	#metodos get

	@classmethod
	def getListaSocios(cls):
		return cls._lista_socio

	#otros metodos
	@classmethod
	def addSocio(cls,cliente):
		cls._lista_socio.append(cliente)
	
	def informacion(self):
		return f"nombre del cliente: {self._nombre} \ncedula: {self._cedula} \ntelefono: {self._telefono}"