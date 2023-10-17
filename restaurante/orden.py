from restaurante.platillo import Platillo
from restaurante.caja import Caja
from restaurante.horarios import Horarios
from gente.cliente import Cliente

import datetime as dt

class Orden:

    _cantidad_orden = 0
    _caja = []

    #constructor 
    def __init__(self, platillos = None, cliente = None, propina = 0):
        if platillos is None:
            platillos = []
        x = 0 
        for i in platillos:
            x += i.getPrecio()
        x += propina
        self._platillos = platillos
        self._precio_total = x
        self._cliente = cliente
        self._propina = propina
        self._numero_orden = Orden._cantidad_orden
        Orden._cantidad_orden += 1
    
    #metodos get 
    def getPlatillos(self):
        return self._platillos
    
    def getNumeroOrden(self):
        return self._numero_orden
    
    def getPrecioTotal(self):
        return self._precio_total
    
    def getCliente(self):
        return self._cliente
    
    def getPropina(self):
        return self._propina

    @classmethod
    def getCantidadOrden(cls):
        return cls._cantidad_orden
    
    @classmethod
    def getCaja(cls):
        return cls._caja
    
    #metodos set
    @classmethod
    def setCaja(cls,caja):
        Orden._caja.append(caja)
    def anadirPlatillos(self, platillo):
        self._platillos.append(platillo)
        self._precio_total += platillo.getPrecio()

    def retirarPlatillo(self, platillo):
        for i in self._platillos:
            if i == platillo:
                self._precio_total -= platillo.getPrecio()
                x = platillo.getIngredientes()
                for e in x:
                    platillo.retirarIngrediente(e)
                self._platillos.remove(platillo)
                return "Platillo retirado"
            elif i == self._platillos[-1]:
                return "no existe este platillo"
        else:
            return "no existe tal platillo"
    
    def descuento(self):
        if self._precio_total > 100:
            self._precio_total = int(self._precio_total*0.95)
        if len(self._platillos) > 50:
            self._precio_total = int(self._precio_total*0.9)
        for i in Cliente.getListaSocios():
            if i.getCedula() == self._cliente.getCedula():
                self._precio_total = int(self._precio_total*0.9)
                break

    def cancelar_orden(self):
        for i in self._platillos:
            self.retirarPlatillo(i)
        return "orden cancelada"
    
    def setCliente(self, cliente):
        self._cliente = cliente
    
    def nuevoSocio(self, cliente):
        Cliente.addSocio(cliente)
    
    def duplicar(self, platillo):
        for i in platillo.getIngredientes():
            if i.verificar_inventario():
                if i == platillo.getIngredientes()[-1]:
                    x = Platillo(platillo.getIngredientes())
                    self.anadirPlatillos(x)
                    return "Platillo duplicado"
                return "No se pudo duplicar"
            return "No se pudo duplicar"
        return "No se pudo duplicar"
    
    def comprobar(self, n):
        x = dt.datetime.now().strftime("%A")
        self.descuento()
        if x == "Sunday" or x == "Saturday":
            if Horarios.horario2.value[0] <= int(dt.datetime.now().strftime("%H")) and Horarios.horario2.value[1] >= int(dt.datetime.now().strftime("%H")):
                if n >= self._precio_total:
                    self._estado_pedido = True
                    self._caja.setEfectivo(self._precio_total)
                    self._caja.nuevoIngreso(self._precio_total)
                    d = n - self._precio_total
                    return f"Pedido confirmado, su devuelta es de {d}"
                else:
                    return "dinero insuficiente"
            return "Pedido por fuera de horario"
        else:
            if Horarios.horario1.value[0] <= int(dt.datetime.now().strftime("%H")) and Horarios.horario1.value[1] >= int(dt.datetime.now().strftime("%H")):
                if n >= self._precio_total:
                    self._estado_pedido = True
                    self._caja[0].setEfectivo(self._precio_total)
                    self._caja[0].nuevoIngreso(self._precio_total)
                    d = n - self._precio_total
                    return f"Pedido confirmado, su devuelta es de {d}"
                else:
                    return "dinero insuficiente"
            return "Pedido por fuera de horario"