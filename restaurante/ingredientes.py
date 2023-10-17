class Ingredientes:
  _listaIngredientes = []
  def __init__(self, precio_compra, cantidad, tipo):
    if Ingredientes._listaIngredientes == []:
      self._precio_compra = precio_compra
      self._cantidad = cantidad
      self._tipo = tipo
      Ingredientes._listaIngredientes.append(self)
    else:
      for i in Ingredientes._listaIngredientes:
        if not i._tipo == tipo:
          if i == Ingredientes._listaIngredientes[-1]:
            self._precio_compra = precio_compra
            self._cantidad = cantidad
            self._tipo = tipo
            Ingredientes._listaIngredientes.append(self)
  #metodos get
  def getPrecioCompra(self):
    return self._precio_compra
  def getCantidad(self):
    return self._cantidad
  def getTipo(self):
    return self._tipo
  @classmethod
  def getListaIngredientes(cls):
    return Ingredientes._listaIngredientes
  #metodos set
  def setPrecioCompra(self, precio):
    self._precio_compra = precio
  def setCantidad(self, cant):
    self._cantidad = cant
  def setTipo(self, tipo):
    self._tipo = tipo
  def anadirCantidad(self, cant, ing = 0):
    if ing == 0:
      self._cantidad += cant
      return f"Ingrediente {self._tipo} aumentado en {cant}"
    else: 
      for i in Ingredientes._listaIngredientes:
        if i._tipo == ing:
          i._cantidad += cant
          return f"Ingrediente {ing} aumentado en {cant}"
        else:
          return "Ingrediente inexistente"
  def retirarCantidad(self, cantidad):
    self._cantidad -= cantidad
    return f"Ingrediente {self._tipo} aumentado en {cantidad}"
  #metodos
  def verificar_inventario(self):
    if self._cantidad > 0:
      return True
    else: 
      return False
  def info(self):
    return f'Nombre: {self._tipo}\nCantidad: {self._cantidad}\nPrecio: {self._precio_compra*2}'