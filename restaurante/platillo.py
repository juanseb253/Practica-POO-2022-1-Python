class Platillo():
    _Lista_platillo=[]
    def __init__(self, ingredientes = None):
        if ingredientes is None:
            ingredientes = []
        self._ingredientes = ingredientes
        self._precio = 0
        for i in self._ingredientes:
            self._precio += i.getPrecioCompra()*2
            i.retirarCantidad(1)
    #metodos get
    def getIngredientes(self):
        return self._ingredientes
    def getPrecio(self):
        return self._precio
    #metodos
    def anadirIngrediente(self, ingrediente):
        if ingrediente.verificar_inventario() == True:
            ingrediente.retirarCantidad(1)
            self._ingredientes.append(ingrediente)
            self._precio += ingrediente.getPrecioCompra()*2
            return f"Ingrediente {ingrediente} anadido con exito"
        else:
            return "No hay existencias de este ingrediente"
    def retirarIngrediente(self, ingrediente):
        for i in self._ingredientes:
            if i == ingrediente:
                self._ingredientes.remove(ingrediente)
                ingrediente.anadirCantidad(1)
                self._precio -= ingrediente.getPrecioCompra()*2
                return f"Ingrediente {ingrediente} retirado con exito"
        return f"Este ingrediente no se encuentra anadido"
    
