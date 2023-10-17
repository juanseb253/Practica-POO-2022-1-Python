class Persona:
    def __init__(self,cedula,nombre,telefono):
        self._cedula=cedula
        self._nombre=nombre
        self._telefono=telefono
    def informacion(self):
        return f"cedula: {self._cedula} nombre: {self._nombre} telefono: {self._telefono}"
    
    #metodos get

    def getCedula(self):
        return self._cedula
    
    def getNombre(self):
        return self._nombre
    
    def getTelefono(self):
        return self._telefono

    #metodos set

    def setCedula(self,cedula):
        self._cedula=cedula
    
    def setNombre(self,nombre):
        self._nombre=nombre
    
    def setTelefono(self,telefono):
        self._telefono=telefono