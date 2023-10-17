import ventana_inicio 
import os
from gente.empleado import Empleado
from baseDatos.Serializador import Serializador
from baseDatos.Deserializador import Deserializador
from restaurante.ingredientes import Ingredientes
from gente.cliente import Cliente
from gente.gerente import Gerente
from restaurante.orden import Orden
from restaurante.orden import Caja
import pathlib

#Comprobanmos si existen objetos creados anteriormente
Vacio=True
path = os.path.join(pathlib.Path(__file__).parent.absolute())
dirtemp = path + "\\baseDatos\\temp"
for filename in os.listdir(dirtemp):
    f = os.path.join(dirtemp, filename)
    if os.stat(f).st_size == 0:
        Vacio = True
    else:
        Vacio = False
'''if Vacio == True: # Si alguna de las carpetas esta vacia
    p1 = Empleado(1, "Juan", 123)
    p2 = Empleado (2, "Villa", 456)
    ing1 = Ingredientes(2, 30, 'carne de res')
    ing2 = Ingredientes(2, 30, 'leche')
    g1 = Gerente(10, "Jorge", 4820249, 1111)
    c1 = Cliente(20, "Franlo el jefe", 318383)
    caja = Caja(0)
    Orden.setCaja(Caja.getCajas()[0])
    emp1 = Empleado(1, "andres", 23)
    emp2 = Empleado(3, "sofia", 4)
    emp3 = Empleado(7, "t", 3)
    emp4 = Empleado(8, "david", 2)
    or1 = Orden().getCaja()[0]
    or1.setEfectivo(70000)
    or1.nuevoIngreso(3000)
    or1.nuevoIngreso(17000)
    or1.nuevoIngreso(50000)
    print("Instanciando objetos")'''
    

    # Se cargan los objetos guardados
Deserializador.DeserializarTodo()
Orden.setCaja(Caja.getCajas()[0])

ventana_inicio.Ventana_inicio()
Serializador.SerializarTodo()

