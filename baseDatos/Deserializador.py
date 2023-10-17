import pickle

from gente.cliente import Cliente
from gente.empleado import Empleado
from gente.gerente import Gerente
from restaurante.ingredientes import Ingredientes
from restaurante.caja import Caja
from restaurante.orden import Orden




class Deserializador:
    @classmethod
    def deserializar(cls, tipo):
        if tipo == "Cliente":
            pickfile = open("baseDatos/temp/Cliente.txt", "rb")
            Cliente._lista_socio = pickle.load(pickfile)
            pickfile.close

        elif tipo == "Empleado":
            pickfile = open( "baseDatos/temp/Empleado.txt", "rb")
            Empleado._lista_empleado = pickle.load(pickfile)
            pickfile.close

        elif tipo == "Gerente":
            pickfile = open("baseDatos/temp/Gerente.txt", "rb")
            Gerente._list_gerente = pickle.load(pickfile)
            pickfile.close

        elif tipo == "ingredientes":
            pickfile = open("baseDatos/temp/ingredientes.txt", "rb")
            Ingredientes._listaIngredientes = pickle.load(pickfile)
            pickfile.close

        elif tipo == "NumEmple":
            pickfile = open("baseDatos/temp/NumEmple.txt", "rb")
            Empleado._numero_empleados = pickle.load(pickfile)
            pickfile.close

        elif tipo == "Caja":
            pickfile = open("baseDatos/temp/Caja.txt","rb")
            Caja._cajas = pickle.load(pickfile)
            Caja._cajas[0].arqueo()
            pickfile.close

    def DeserializarTodo():
        Deserializador.deserializar("Cliente")
        Deserializador.deserializar("Empleado")
        Deserializador.deserializar("Gerente")
        Deserializador.deserializar("ingredientes")
        Deserializador.deserializar("NumEmple")
        Deserializador.deserializar("Caja")
