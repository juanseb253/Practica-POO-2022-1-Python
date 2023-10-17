import tkinter as tk
import os
import pathlib
from tkinter import messagebox
from tkinter import ttk
from restaurante.platillo import Platillo
import ventana_inicio
import iniciar_sesion
import fieldframe

from gente.empleado import Empleado
from restaurante.ingredientes import Ingredientes
from restaurante.orden import Orden
from gente.cliente import Cliente

from excepciones.erroaplicacion import ErrorAplicacion
from excepciones.errorformato import *

path = os.path.join(pathlib.Path(__file__).parent.absolute())

#ventana principal, donde se ejecuta el programa
class Ventana_principal_empleado(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ventana_principal_empleado")
        self.geometry("1360x720")
        self.configure(bg="white")

        #este frame(frame_0) corresponde al de la parte superior

        self.frame_0=tk.Frame(self,bg="red",height=80)
        self.frame_0.pack(side="top",fill="x")

        #una etiqueta que contiene al titulo del nombre del software

        self.titulo=tk.Label(self.frame_0,text=" software para un restaurante ")
        self.titulo.config(fg="white",bg="red",font=("italic",30,"italic"))
        self.titulo.pack(anchor="c")

        #este frame(frame_1) corresponde a la zona de menus

        self.frame_1=tk.Frame(self,bg="gray",height=80)
        self.frame_1.pack(side="top",fill="x")

        #se muestra una ventana de dialogo con la descripcion del software
        def descripcion_software(): 
            messagebox.showinfo("Descripcion del sistema","Este software se encarga de la gestion de un restaurante a nivel general, es decir, con el software para un restaurante se podran administrar diferentes aspectos como lo son ventas, nomina e inventario")
    
        #se muestra una ventana de dialogo con los nombres de los autores del software
        def autores_software(): 
            messagebox.showinfo("Autores del software","Autor 1:Juan David Villamizar Gelves\nAutor 2:Jorge Andres Higuita Monsalve\nAutor 3:Juan Sebastian echeverri Zapata")
        
        #en este frame(frame_2) se encuentra lo relacionado con los procesos y consultas
        self.frame_2=tk.Frame(self,bg="white",height=650)
        self.frame_2.pack(side="top",fill="both")
        
        #frame de la parte de abajo, es meramente decorativo 
        self.frame_abajo=tk.Frame(self,bg="red",height=80)
        self.frame_abajo.pack(side="bottom",fill="both")

        #esta funcion ejecuta las opciones del combobox de Archivo
        def opciones_Archivo(event):
            if self.Archivo.get()=="Aplicacion":
                self.Archivo.set("Archivo")
                descripcion_software()
                
            if self.Archivo.get()=="Salir":
                self.Archivo.set("Archivo")
                self.ventana_inicio()
        
        #esta funcion se ejecuta al seleccionar la opcion agragar socio del combobox de p y c
        def agregar_socio():

            self.titulo_tomar_orden.place_forget()

            self.descripcion_tomar_orden.place_forget()

            self.boton_anadir_platillo.place_forget()

            self.boton_retirar_platillo.place_forget()

            self.boton_terminar_orden.place_forget()

            self.boton_cancelar_orden.place_forget()

            self.titulo_anadir_socio.place(x=690,y=10,width=100,height=40)

            self.descripcion_anadir_socio.place(x=400,y=60,width=700,height=40)

            self.a.place(x=520,y=150,width=500,height=160)

        #esta funcion se ejecuta al seleccionar la opcion tomar orden del combobox de p y c

        #funcionalidades de tomar orden

        def tomar_orden():
            self.b.place_forget()

            self.t.place_forget()

            self.boton_volver.place_forget()

            self.titulo_anadir_socio.place_forget()

            self.descripcion_anadir_socio.place_forget()

            self.titulo_tomar_orden.place(x=730,y=10,width=100,height=40)

            self.descripcion_tomar_orden.place(x=540,y=70,width=500,height=40)

            self.boton_anadir_platillo.place(x=640,y=120,width=300,height=50)

            self.boton_retirar_platillo.place(x=640,y=180,width=300,height=50)

            self.boton_terminar_orden.place(x=640,y=240,width=300,height=50)

            self.boton_cancelar_orden.place(x=640,y=300,width=300,height=50)

            self.a.place_forget()
        
        #cosas de anadir socio

        self.titulo_anadir_socio = tk.Label(self.frame_2,text=" anadir socio ")

        self.titulo_anadir_socio.place(x=10,y=10,width=100,height=40)

        self.titulo_anadir_socio.place_forget()

        self.descripcion_anadir_socio = tk.Label(self.frame_2,text=" esta funcion se encarga de registrar a los clientes a una lista de socios, los cuales tienen acceso a beneficios ")

        self.descripcion_anadir_socio.place(x=10,y=10,width=100,height=40)

        self.descripcion_anadir_socio.place_forget()

        #formularios

        #formulario para anadir a un nuevo socio

        self.a=fieldframe.FieldFrame(self.frame_2,"datos",["cedula","nombre","telefono"],"valor")

        self.a.place(x=520,y=100,width=500,height=100)

        self.a.place_forget()

        #formulario para anadir un nuevo platillo

        self.b=fieldframe.FieldFrame(self.frame_2,"ingredientes",["ingrediente 1","ingrediente 2"],"nombres")

        self.b.place(x=520,y=100,width=500,height=100)

        self.b.place_forget()

        #funcion que sirve para agregar platillos

        def agregando_pl(entry):
            y = self.b.aceptar()
            platillo=Platillo()
            if y[0] == '' and y[1] == '':
                messagebox.showwarning(title="Aviso",message='platillo sin ingredientes, agregue por lo menos un ingrediente')  
            elif y[0] == '' and y[1] != '':
                for i in Ingredientes._listaIngredientes:
                    if i.getTipo()==y[1]:
                        if i.getCantidad()==0:
                            messagebox.showwarning(title="Aviso",message=platillo.anadirIngrediente(i))
                            break
                        else:
                            platillo.anadirIngrediente(i)
                            Platillo._Lista_platillo.append(platillo)
                            messagebox.showwarning(title="Aviso",message="platillo creado con exito")
                            break
                    elif i == Ingredientes._listaIngredientes[-1]:
                        messagebox.showwarning(title="Aviso",message="atencion, el ingrediente que ha ingresado no existe")
            elif y[1] == "" and y[0] != '':
                for i in Ingredientes._listaIngredientes:
                    if i.getTipo()==y[0]:
                        if i.getCantidad()==0:
                            messagebox.showwarning(title="Aviso",message=platillo.anadirIngrediente(i))
                            break
                        else:
                            platillo.anadirIngrediente(i)
                            Platillo._Lista_platillo.append(platillo)
                            messagebox.showwarning(title="Aviso",message="platillo creado con exito")
                            break
                    elif i == Ingredientes._listaIngredientes[-1]:
                        messagebox.showwarning(title="Aviso",message="atencion, el ingrediente que ha ingresado no existe")
            else:
                prueba = False
                for i in Ingredientes._listaIngredientes:
                    if i.getTipo()==y[0]:
                        if i.getCantidad()==0:
                            messagebox.showwarning(title="Aviso",message=platillo.anadirIngrediente(i))
                            break
                        else:
                            platillo.anadirIngrediente(i)
                            prueba = True
                            break
                    elif i == Ingredientes._listaIngredientes[-1]:
                        messagebox.showwarning(title="Aviso",message="atencion, el ingrediente que ha ingresado no existe")  
                if prueba:
                    for i in Ingredientes._listaIngredientes:
                        if i.getTipo()==y[1]:
                            if i.getCantidad()==1:
                                messagebox.showwarning(title="Aviso",message=platillo.anadirIngrediente(i))
                                break
                            else:
                                platillo.anadirIngrediente(i)
                                Platillo._Lista_platillo.append(platillo)
                                messagebox.showwarning(title="Aviso",message="platillo creado con exito")
                                
                                break
                        elif i == Ingredientes._listaIngredientes[-1]:
                            messagebox.showwarning(title="Aviso",message="atencion, el ingrediente que ha ingresado no existe")
        self.b.botonAceptar.bind("<ButtonRelease-1>", agregando_pl)

        def agregando(entry):
            x = self.a.aceptar()
            if x[0] == '':
                messagebox.showwarning(title="Aviso",message='No hay cedula, por favor agrege la cedula')
            try:
                cedula = int(x[0])
            except:
                messagebox.showwarning(title="Aviso",message=ExcepcionEnteroString('Cedula').mensaje_error)
            if x[1] == '':
                messagebox.showwarning(title="Aviso",message='No hay nombre, por favor agrege el nombre')
            else:
                nombre = x[1]
            if x[2] == '':
                messagebox.showwarning(title="Aviso",message='No hay telefono, por favor agrege el telefono')
            try:
                telefono = int(x[2])
            except:
                messagebox.showwarning(title="Aviso",message=ExcepcionEnteroString('Telefono').mensaje_error)
            
            cl=Cliente(cedula, nombre, telefono)
        
            Cliente. addSocio(cl)

            messagebox.showinfo(title='Aviso', message="el cliente fue agregado exitosamente a la lista de clientes")
                 
        self.a.botonAceptar.bind("<ButtonRelease-1>", agregando)

        self.b.place(x=520,y=100,width=500,height=100)

        self.b.place_forget()
        

        #un boton para volver despues de añadir un platillo

        self.boton_volver = tk.Button(self.frame_2,text="volver",command=tomar_orden)

        self.boton_volver.place(x=520,y=100,width=500,height=100)

        self.boton_volver.place_forget()

        #un formulario para terminar orden

        self.t=fieldframe.FieldFrame(self.frame_2,"pago",["monto de dinero"],"total")

        self.t.place(x=520,y=100,width=500,height=100)

        self.t.place_forget()

        #funcionalidades para los botones de tomar orden

        def añadiendo_platillo():
            self.boton_volver.place(x=520,y=300,width=200,height=60)

            self.b.place(x=520,y=100,width=500,height=100)

            self.boton_anadir_platillo.place_forget()

            self.boton_retirar_platillo.place_forget()

            self.boton_terminar_orden.place_forget()

            self.boton_cancelar_orden.place_forget()

            self.titulo_tomar_orden.place_forget()

            self.descripcion_tomar_orden.place_forget()

            #print("añadiendo_platillo")

        def retirando_platillo():
            if len(Platillo._Lista_platillo)>=1:
                Platillo._Lista_platillo.pop(len(Platillo._Lista_platillo.pop)-1)
            else:
                messagebox.showwarning(title="Aviso",message="no hay platillos para retirar")

        def terminando(entry):
            z = self.t.aceptar()
            if z[0] == '':
                messagebox.showwarning(title="Aviso",message='debe ingresar un valor')
            try:
                valor = int(z[0])
            except:
                messagebox.showwarning(title="Aviso",message=ExcepcionEnteroString('valor').mensaje_error)
            
            orden=Orden()
            for i in Platillo._Lista_platillo:
                orden.anadirPlatillos(i)
            texto=orden.comprobar(valor)
            messagebox.showwarning(title="Aviso",message=texto)
        self.t.botonAceptar.bind("<ButtonRelease-1>", terminando)


        def terminando_orden():
            self.boton_anadir_platillo.place_forget()

            self.boton_retirar_platillo.place_forget()

            self.boton_terminar_orden.place_forget()

            self.boton_cancelar_orden.place_forget()

            self.titulo_tomar_orden.place_forget()

            self.descripcion_tomar_orden.place_forget()

            self.t.place(x=520,y=100,width=500,height=100)

            self.boton_volver.place(x=520,y=300,width=200,height=60)

            #orden=Orden()
            #orden.comprobar()

        def cancelando_orden():
            Platillo._Lista_platillo=[]
            messagebox.showwarning(title="Aviso",message="se ha cancelado la orden")
        
        #botones de tomar orden

        self.titulo_tomar_orden = tk.Label(self.frame_2,text=" tomar orden ")

        self.titulo_tomar_orden.place(x=10,y=10,width=100,height=40)

        self.titulo_tomar_orden.place_forget()

        self.descripcion_tomar_orden = tk.Label(self.frame_2,text=" esta funcion se encarga de la gestion de los pedidos a nivel general")

        self.descripcion_tomar_orden.place(x=10,y=10,width=100,height=40)

        self.descripcion_tomar_orden.place_forget()

        self.boton_anadir_platillo = tk.Button(self.frame_2,text="anadir platillo",command=añadiendo_platillo)

        self.boton_retirar_platillo = tk.Button(self.frame_2,text="retirar platillo",command=retirando_platillo)

        self.boton_terminar_orden = tk.Button(self.frame_2,text="terminar orden",command=terminando_orden)

        self.boton_cancelar_orden = tk.Button(self.frame_2,text="cancelar orden",command=cancelando_orden)

        ############################################################################

        self.boton_anadir_platillo.place(x=10,y=10,width=100,height=40)

        self.boton_retirar_platillo.place(x=10,y=20,width=100,height=40)

        self.boton_terminar_orden.place(x=10,y=40,width=100,height=40)

        self.boton_cancelar_orden.place(x=10,y=50,width=100,height=40)

        ############################################################################

        self.boton_anadir_platillo.place_forget()

        self.boton_retirar_platillo.place_forget()

        self.boton_terminar_orden.place_forget()

        self.boton_cancelar_orden.place_forget()
               
        #esta funcion ejecuta las opciones del combobox de opciones_p_y_C(todavia faltan por definir bien las funciones)
        def opciones_p_y_c(event):
            if self.p_y_c.get()=="agregar socio":
                agregar_socio()
                self.p_y_c.set("Procesos y consultas")

            elif self.p_y_c.get()=="tomar orden":
                tomar_orden()
                self.p_y_c.set("Procesos y consultas")   
        
        #esta funcion ejecuta las opciones del combox de ayuda
        def opciones_ayuda(event):
            if self.Ayuda.get()=="acerca de":
                self.Ayuda.set("Ayuda")
                autores_software()


        #Archivo
        valorDefecto_archivo = tk.StringVar(value='Archivo')
        self.Archivo = tk.ttk.Combobox(self.frame_1,values=["Aplicacion","Salir"],textvariable=valorDefecto_archivo,state="readonly")
        self.Archivo.grid(row=0,column=0)
        self.Archivo.bind("<<ComboboxSelected>>",opciones_Archivo)


        #Procesos y consultas
        valorDefecto_p_y_c = tk.StringVar(value='Procesos y consultas')
        self.p_y_c = tk.ttk.Combobox(self.frame_1,values=["tomar orden","agregar socio"],textvariable=valorDefecto_p_y_c,state="readonly")
        self.p_y_c.grid(row=0,column=1)
        self.p_y_c.bind("<<ComboboxSelected>>",opciones_p_y_c)

        #Ayuda
        valorDefecto_ayuda = tk.StringVar(value='Ayuda')
        self.Ayuda = tk.ttk.Combobox(self.frame_1,values=["acerca de"],textvariable=valorDefecto_ayuda,state="readonly")
        self.Ayuda.grid(row=0,column=2)
        self.Ayuda.bind("<<ComboboxSelected>>",opciones_ayuda)
        self.mainloop()

    #vuelve a la ventana de inicio   
    def ventana_inicio(self):
        self.destroy()
        ventana_inicio.Ventana_inicio()
    