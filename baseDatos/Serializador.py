import pickle

from gente.cliente import Cliente
from gente.empleado import Empleado
from gente.gerente import Gerente
from restaurante.ingredientes import Ingredientes
from restaurante.caja import Caja
from restaurante.orden import Orden


class Serializador:
    @classmethod
    def serializar(cls,tipo):
        if tipo=="Cliente":
            pickfile = open("baseDatos/temp/Cliente.txt", "wb")
            serializa = Cliente._lista_socio
            pickle.dump(serializa, pickfile,)
            pickfile.close

        elif tipo=="Empleado":
            pickfile = open("baseDatos/temp/Empleado.txt", "wb")
            serializa = Empleado._lista_empleado
            pickle.dump(serializa, pickfile)
            pickfile.close
        
        elif tipo=="Gerente":
            pickfile = open("baseDatos/temp/Gerente.txt", "wb")
            serializa = Gerente._list_gerente
            pickle.dump(serializa, pickfile)
            pickfile.close
        
        elif tipo=="ingredientes":
            pickfile = open("baseDatos/temp/ingredientes.txt", "wb")
            serializa = Ingredientes.getListaIngredientes()
            pickle.dump(serializa, pickfile)
            pickfile.close
        
        elif tipo=="NumEmple":
            pickfile = open("baseDatos/temp/NumEmple.txt", "wb")
            serializa = Empleado.getNumero_empleados()
            pickle.dump(serializa, pickfile)
            pickfile.close

        elif tipo == "Caja":
            pickfile = open("baseDatos/temp/Caja.txt","wb")
            serializa = Caja.getCajas()
            pickle.dump(serializa,pickfile)
            pickfile.close
        
    def SerializarTodo():
        Serializador.serializar("Cliente")
        Serializador.serializar("Empleado")
        Serializador.serializar("Gerente")
        Serializador.serializar("ingredientes")
        Serializador.serializar("NumEmple")
        Serializador.serializar("Caja")
      
