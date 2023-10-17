import tkinter as tk
import os
import pathlib
from tkinter import Button, Frame, messagebox
from tkinter import ttk
from turtle import width
import turtle
import ventana_inicio

from gente.empleado import Empleado
from gente.gerente import Gerente
from restaurante.ingredientes import Ingredientes
from restaurante.orden import Orden
from restaurante.caja import Caja

from excepciones.erroaplicacion import ErrorAplicacion
from excepciones.errorformato import *
from fieldframe import FieldFrame

path = os.path.join(pathlib.Path(__file__).parent.absolute())

#ventana principal, donde se ejecuta el programa
class Ventana_principal_gerente(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ventana_principal_gerente")
        self.geometry("1360x720")
        self.configure(bg="LightSteelBlue")

        #este frame(frame_0) corresponde al de la parte superior

        self.frame_0=tk.Frame(self,bg="RoyalBlue",height=80)
        self.frame_0.pack(side="top",fill="x")

        #una etiqueta que contiene al titulo del nombre del software

        self.titulo=tk.Label(self.frame_0,text=" software para un restaurante ")
        self.titulo.config(fg="white",bg="RoyalBlue",font=("italic",30,"italic"))
        self.titulo.pack(anchor="c")

        #este frame(frame_1) corresponde a la zona de menus

        self.frame_1=tk.Frame(self,bg="gray",height=80)
        self.frame_1.pack(side="top",fill="x")

        #se muestra una ventana de dialogo con la descripcion del software
        def descripcion_software(): 
            messagebox.showinfo("Descripcion del sistema","Este software se encarga de la gestion de un restaurante a nivel general, es decir, con el software para un restaurante se podran administrar diferentes aspectos como lo son ventas, nomina e inventario")
    
        #se muestra una ventana de dialogo con los nombres de los autores del software
        def autores_software(): 
            messagebox.showinfo("Autores del software","Autor 1:Juan David Billamizar Gelves\nAutor 2:Jorge Andres Higuita Monsalve\nAutor 3:Juan Sebastian echeverri Zapata")

        #en este frame(frame_2) se encuentra lo relacionado con los procesos y consultas
        self.frame_2=tk.Frame(self,bg="LightSteelBlue",height=700)
        self.frame_2.pack(side="top",fill="both")
        

       
        #frame de la parte de abajo, es meramente decorativo 
        self.frame_abajo=tk.Frame(self,bg="RoyalBlue",height=70)
        self.frame_abajo.pack(side="bottom",fill="both")

        #frames, botones de empleados ----------------------------------------------------------------------------------------------------------------------------------------------


        self.titl_label = tk.Label(self, text='Ver empleados', font=('Italic', 20))
        self.desp_frame = tk.Frame(self, bg= 'LightSteelBlue', height= 80, width= 1360)
        self.desp_exp = tk.Label(self.desp_frame, text = 'En esta ventana podremos visualizar la informacion de los empleados y despedir al que queramos,\nel despido inteligente despide al empleado menos eficiente, ademas podremos ver a nuestro mejor empleado.')


        self.despido = Button(self.frame_2, text='Despedir', width=15)
        self.info_emp = 'Aqui aparecera la informacion de los distintos empleados.'
        self.num_emp = 0
        self.textemp = tk.Text(self.frame_2, border= False, font=('Italic', 20))
        self.textemp.insert(tk.END, self.info_emp)
        self.textemp.configure(state='disabled')
        self.sig_emp = Button(self.frame_2, text='Siguiente', width=15)
        self.atr_emp = Button(self.frame_2, text='Anterior', width=15)
        self.desp_int = Button(self.frame_2, text='Despido inteligente', width=15)
        self.mas_ef = Button(self.frame_2, text= 'Mas eficiente',width=15)

        #widgets de contratar empleado---------------------------------------------------------------------------------------------------------------------------------------------
        self.titl_con = tk.Label(self, text='Contratar empleado', font=('Italic', 20))
        self.desp_con = tk.Frame(self, bg= 'LightSteelBlue', height= 80, width= 1360)
        self.desp_exp_con = tk.Label(self, text='En esta ventana podremos contratar a un nuevo empleado, al aceptar podremos verlo en la ventana "Ver y despedir empleados"')

        self.frame_3=tk.Frame(self,bg="LightSteelBlue",height=700)
        self.field_con = FieldFrame(self.frame_3, "Caracteristica", ["Cedula", "Nombre", "Telefono"], "valores")
        
        #frames, botones de inventario --------------------------------------------------------------------------------------------------------------------------------------------
        self.titl_inv1 = tk.Label(self, text='Ver Inventario', font=('Italic', 20))
        self.desp_inv1 = tk.Frame(self, bg= 'LightSteelBlue', height= 80, width= 1360)
        self.desp_exp_inv1 = tk.Label(self, text="Usando los botones de Anterior y Siguiente podremos ver la informacion de los ingredientes")

        self.sig_inv = Button(self.frame_2, text='Siguiente', width=15)
        self.atr_inv = Button(self.frame_2, text='Anterior', width=15)
        self.info_inv = 'Aqui aparecera la informacion de los distintos ingredientes.'
        self.num_inv = 0
        self.textinv = tk.Text(self.frame_2, border= False, font=('Italic', 20))
        self.textinv.insert(tk.END, self.info_inv)
        self.textinv.configure(state='disabled')
        #widgets de añadir o aumentar ingredientes----------------------------------------------------------------------------------------------------------------------------------------------
        self.titl_agg = tk.Label(self, text='Anadir/aumentar ingrediente', font=('Italic', 20))
        self.desp_agg = tk.Frame(self, bg= 'LightSteelBlue', height= 80, width= 1360)
        self.desp_exp_agg = tk.Label(self, text="En esta ventana podremos anadir nuevos ingredientes, si estos ya existian se aumentara la cantidad de estos y adicionalmente\nen este caso no es necesario ingresar el precio de compra")

        self.field_agg = FieldFrame(self.frame_3, "Caracteristica", ["Tipo", "Cantidad", "Precio de compra"], "valores")


        # Widgets arqueo de caja-----------------------------------------------------------------------------------------------------------------------------------------------------
        self.titl_arq = tk.Label(self, text='Arqueo de caja', font=('Italic', 20))
        self.desp_arq = tk.Frame(self, bg= 'LightSteelBlue', height= 80, width= 1360)
        self.desp_exp_arq = tk.Label(self, text="Aqui podremos ver las distintas entradas y salidas de caja y el valor final ")
        self.textarq = tk.Text(self.frame_2, border= False, font=('Italic', 20))
        self.info_arq = 'Dale "mostrar" para ver las distintas entradas y salidas de caja'
        self.textarq.insert(tk.END, self.info_arq)
        self.textarq.configure(state='disabled')
        self.mostrar_arq = Button(self.frame_2, text='Mostrar', width=15)
        
        # ver empleado ------------------------------------------------------------------------------------------------------------
        def buscar_empleado(event):
            x = Empleado.getListaEmpleado()
            if self.info_emp == 'Aqui aparecera la informacion de los distintos empleados.':
                self.num_emp = 0
                try:
                    self.info_emp = x[self.num_emp].informacion()
                    self.textemp.configure(state='normal')
                    self.textemp.delete('1.0', 'end-1c')
                    self.textemp.insert(tk.END,self.info_emp)
                    self.textemp.configure(state='disabled')
                except:
                    messagebox.showwarning(title="Aviso",message=ExcepcionEmpleado('').mensaje_error)

            elif self.num_emp >= len(x)-1:
                self.num_emp = 0
                try:
                    self.info_emp = x[self.num_emp].informacion()
                    self.textemp.configure(state='normal')
                    self.textemp.delete('1.0', 'end-1c')
                    self.textemp.insert(tk.END,self.info_emp)
                    self.textemp.configure(state='disabled')
                except:
                    messagebox.showwarning(title="Aviso",message=ExcepcionEmpleado('').mensaje_error)

            else:
                self.num_emp += 1
                try:
                    self.info_emp = x[self.num_emp].informacion()
                    self.textemp.configure(state='normal')
                    self.textemp.delete('1.0', 'end-1c')
                    self.textemp.insert(tk.END,self.info_emp)
                    self.textemp.configure(state='disabled')
                except:
                    messagebox.showwarning(title="Aviso",message=ExcepcionEmpleado('').mensaje_error)


        def atras_empleado(event):
            x = Empleado.getListaEmpleado()
            if self.info_emp == 'Aqui aparecera la informacion de los distintos empleados.':
                self.num_emp = len(x)
                try:
                    self.info_emp = x[self.num_emp].informacion()
                    self.textemp.configure(state='normal')
                    self.textemp.delete('1.0', 'end-1c')
                    self.textemp.insert(tk.END,self.info_emp)
                    self.textemp.configure(state='disabled')
                except:
                    messagebox.showwarning(title="Aviso",message=ExcepcionEmpleado('').mensaje_error)

            elif self.num_emp == 0:
                self.num_emp = len(x)-1
                try:
                    self.info_emp = x[self.num_emp].informacion()
                    self.textemp.configure(state='normal')
                    self.textemp.delete('1.0', 'end-1c')
                    self.textemp.insert(tk.END,self.info_emp)
                    self.textemp.configure(state='disabled')
                except:
                    messagebox.showwarning(title="Aviso",message=ExcepcionEmpleado('').mensaje_error)

            else:
                self.num_emp -= 1
                try:
                    self.info_emp = x[self.num_emp].informacion()
                    self.textemp.configure(state='normal')
                    self.textemp.delete('1.0', 'end-1c')
                    self.textemp.insert(tk.END,self.info_emp)
                    self.textemp.configure(state='disabled')
                except:
                    messagebox.showwarning(title="Aviso",message=ExcepcionEmpleado('').mensaje_error)
        
        def despido_emp(event):
            for i in Empleado.getListaEmpleado():
                 if i.informacion() == self.info_emp:
                    Gerente.despedir_Empleado(i.getNumero())
                    self.info_emp = 'Enhorabuena, despediste al empleado:\n\n' + self.info_emp + '\n\nAhora no tendras que verlo nunca mas'
                    self.textemp.configure(state='normal')
                    self.textemp.delete('1.0', 'end-1c')
                    self.textemp.insert(tk.END,self.info_emp)
                    self.textemp.configure(state='disabled')

        def desp_int(event):
            try:
                self.info_emp = 'Enhorabuena, despediste al empleado:\n\n' + Empleado.empleado_menos_eficiente().informacion() + '\n\nAhora no tendras que verlo nunca mas'
                Gerente.despido_inteligente()
            except:
                messagebox.showwarning(title="Aviso",message=ExcepcionEmpleado('').mensaje_error)
            self.textemp.configure(state='normal')
            self.textemp.delete('1.0', 'end-1c')
            self.textemp.insert(tk.END,self.info_emp)
            self.textemp.configure(state='disabled')

        def emp_efic(event):
            try:
                w = Empleado.empleado_mas_eficiente()
                self.info_emp = 'Nuestro mejor empleado es:\n\n' + w.informacion() + '\n\n deberias aumentarle el salario a este buen trabajador. '
                self.textemp.configure(state='normal')
                self.textemp.delete('1.0', 'end-1c')
                self.textemp.insert(tk.END,self.info_emp)
                self.textemp.configure(state='disabled')
            except:
                messagebox.showwarning(title="Aviso",message=ExcepcionEmpleado('').mensaje_error)

        self.sig_emp.bind('<ButtonRelease-1>',buscar_empleado)
        self.atr_emp.bind('<ButtonRelease-1>',atras_empleado)
        self.despido.bind('<ButtonRelease-1>', despido_emp)
        self.desp_int.bind('<ButtonRelease-1>', desp_int)
        self.mas_ef.bind('<ButtonRelease-1>',emp_efic)
        def show_empleados():
            self.frame_abajo.pack_forget()
            self.frame_2.pack_forget()
            self.titl_inv1.pack_forget()
            self.desp_inv1.pack_forget()
            self.desp_exp_inv1.pack_forget()
            self.textinv.place_forget()
            self.titl_con.pack_forget()
            self.desp_con.pack_forget()
            self.desp_exp_con.pack_forget()
            self.field_con.pack_forget()
            self.frame_3.pack_forget()
            self.titl_agg.pack_forget()
            self.desp_agg.pack_forget()
            self.desp_exp_agg.pack_forget()
            self.field_agg.pack_forget()
            self.titl_arq.pack_forget()
            self.desp_arq.pack_forget()
            self.desp_exp_arq.pack_forget()
            self.textarq.place_forget()
            self.mostrar_arq.place_forget()
            self.titl_label.pack(pady = 10)
            self.desp_frame.pack(anchor='n')
            self.desp_exp.pack(pady= 10)
            self.frame_2.pack(side="top",fill="both")
            self.despido.place(relx = 0.4, rely = 0.9, anchor = 'c')
            self.desp_int.place(relx = 0.6,rely=0.9, anchor='c')
            self.textemp.place(relx=0.5,rely=0.5,relheight=0.6, relwidth= 0.6, anchor= 'c')
            self.sig_emp.place(relx = 0.7, rely = 0.9, anchor = 'c')
            self.atr_emp.place(relx = 0.3, rely = 0.9, anchor = 'c')
            self.mas_ef.place(relx = 0.5, rely = 0.9, anchor = 'c')
            
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        #contratar empleado

        def contratar(entry):
            x = self.field_con.aceptar()
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
            
            Gerente.contratar_Empleado(cedula, nombre, telefono)
            messagebox.showinfo(title='Aviso', message='Empleado contratado correctamente, puedes verlo en la opcion "Ver y despedir empleados"')
            
            
                
        self.field_con.botonAceptar.bind("<ButtonRelease-1>", contratar)
        def contratar_empleado():
            self.frame_abajo.pack_forget()
            self.frame_2.pack_forget()
            self.titl_inv1.pack_forget()
            self.desp_inv1.pack_forget()
            self.desp_exp_inv1.pack_forget()
            self.textinv.place_forget()
            self.frame_abajo.pack_forget()
            self.frame_2.pack_forget()
            self.titl_label.pack_forget()
            self.desp_frame.pack_forget()
            self.desp_exp.pack_forget()
            self.frame_3.pack_forget()
            self.despido.place_forget()
            self.desp_int.place_forget()
            self.textemp.place_forget()
            self.sig_emp.place_forget()
            self.atr_emp.place_forget()
            self.mas_ef.place_forget()

            self.sig_inv.place_forget()
            self.atr_inv.place_forget()

            self.titl_agg.pack_forget()
            self.desp_agg.pack_forget()
            self.desp_exp_agg.pack_forget()
            self.field_agg.pack_forget()

            self.titl_arq.pack_forget()
            self.desp_arq.pack_forget()
            self.desp_exp_arq.pack_forget()
            self.textarq.place_forget()
            self.mostrar_arq.place_forget()

            self.titl_con.pack(pady = 10)
            self.desp_con.pack(anchor = 'n')
            self.desp_exp_con.pack(pady = 10)
            self.frame_3.pack(side="top",fill="both")
            self.field_con.pack(pady = 40)

        ##---------------------------------------------------------------------------------------------------------------------------------
        #aqui va la parte de el inventario
        
        def buscar_inv(event):
            x = Ingredientes.getListaIngredientes()
            if self.info_inv == 'Aqui aparecera la informacion de los distintos ingredientes.':
                self.num_inv = 0
                try:
                    self.info_inv = x[self.num_inv].info()
                    self.textinv.configure(state='normal')
                    self.textinv.delete('1.0', 'end-1c')
                    self.textinv.insert(tk.END,self.info_inv)
                    self.textinv.configure(state='disabled')
                except:
                    messagebox.showwarning(title="Aviso",message=ExcepcionInv('').mensaje_error)

            elif self.num_inv >= len(x)-1:
                self.num_inv = 0
                try:
                    self.info_inv = x[self.num_inv].info()
                    self.textinv.configure(state='normal')
                    self.textinv.delete('1.0', 'end-1c')
                    self.textinv.insert(tk.END,self.info_inv)
                    self.textinv.configure(state='disabled')
                except:
                    messagebox.showwarning(title="Aviso",message=ExcepcionInv('').mensaje_error)

            else:
                self.num_inv += 1
                try:
                    self.info_inv = x[self.num_inv].info()
                    self.textinv.configure(state='normal')
                    self.textinv.delete('1.0', 'end-1c')
                    self.textinv.insert(tk.END,self.info_inv)
                    self.textinv.configure(state='disabled')
                except:
                    messagebox.showwarning(title="Aviso",message=ExcepcionInv('').mensaje_error)


        def atras_inv(event):
            x = Ingredientes.getListaIngredientes()
            if self.info_inv == 'Aqui aparecera la informacion de los distintos ingredientes.':
                self.num_inv = len(x)
                try:
                    self.info_inv = x[self.num_inv].info()
                    self.textinv.configure(state='normal')
                    self.textinv.delete('1.0', 'end-1c')
                    self.textinv.insert(tk.END,self.info_inv)
                    self.textinv.configure(state='disabled')
                except:
                    messagebox.showwarning(title="Aviso",message=ExcepcionInv('').mensaje_error)

            elif self.num_inv == 0:
                self.num_inv = len(x)-1
                try:
                    self.info_inv = x[self.num_inv].info()
                    self.textinv.configure(state='normal')
                    self.textinv.delete('1.0', 'end-1c')
                    self.textinv.insert(tk.END,self.info_inv)
                    self.textinv.configure(state='disabled')
                except:
                    messagebox.showwarning(title="Aviso",message=ExcepcionInv('').mensaje_error)

            else:
                self.num_inv -= 1
                try:
                    self.info_inv = x[self.num_inv].info()
                    self.textinv.configure(state='normal')
                    self.textinv.delete('1.0', 'end-1c')
                    self.textinv.insert(tk.END,self.info_inv)
                    self.textemp.configure(state='disabled')
                except:
                    messagebox.showwarning(title="Aviso",message=ExcepcionInv('').mensaje_error)
        
        self.sig_inv.bind('<ButtonRelease-1>',buscar_inv)
        self.atr_inv.bind('<ButtonRelease-1>',atras_inv)
        def show_inv():
            self.frame_abajo.pack_forget()
            self.frame_2.pack_forget()
            self.titl_label.pack_forget()
            self.desp_frame.pack_forget()
            self.desp_exp.pack_forget()
            self.frame_2.pack_forget()
            self.despido.place_forget()
            self.desp_int.place_forget()
            self.textemp.place_forget()
            self.sig_emp.place_forget()
            self.atr_emp.place_forget()
            self.mas_ef.place_forget()

            self.titl_con.pack_forget()
            self.desp_con.pack_forget()
            self.desp_exp_con.pack_forget()
            self.field_con.pack_forget()
            self.frame_3.pack_forget()

            self.titl_agg.pack_forget()
            self.desp_agg.pack_forget()
            self.desp_exp_agg.pack_forget()
            self.field_agg.pack_forget()

            self.titl_arq.pack_forget()
            self.desp_arq.pack_forget()
            self.desp_exp_arq.pack_forget()
            self.textarq.place_forget()
            self.mostrar_arq.place_forget()

            self.titl_inv1.pack(pady = 10)
            self.desp_inv1.pack(anchor='n')
            self.desp_exp_inv1.pack(pady= 10)
            self.frame_2.pack(side="top",fill="both")
            self.textinv.place(relx=0.5,rely=0.5,relheight=0.6, relwidth= 0.6, anchor= 'c')
            self.sig_inv.place(relx = 0.6, rely = 0.9, anchor = 'c')
            self.atr_inv.place(relx = 0.4, rely = 0.9, anchor = 'c')
        #anadir nuevos ingredientes al catalogo
        def nuev_ingred(entry):
            x = self.field_agg.aceptar()

            try:
                cant = int(x[1])
            except:
                messagebox.showwarning(title='Aviso', message=ExcepcionEnteroString('Cantidad').mensaje_error)
            for i in Ingredientes.getListaIngredientes():
                if i.getTipo() == x[0]:
                    i.anadirCantidad(cant)
                    messagebox.showinfo(title='Aviso', message='Cantidad anadida con exito, puede comprobarlo en "Ver inventario"')
                    break
                if Ingredientes.getListaIngredientes()[-1].getTipo() == i.getTipo():
                    try:
                        pre = int(x[2])
                        Ingredientes(pre, cant, x[0])
                        messagebox.showinfo(title='Aviso', message='Nuevo ingrediente con exito, puede comprobarlo en "Ver inventario"')
                        break
                    except:
                        messagebox.showwarning(title='Aviso', message=ExcepcionEnteroString('Precio de compra').mensaje_error)
        self.field_agg.botonAceptar.bind('<ButtonRelease-1>', nuev_ingred)
        def new_ingredient():
            self.frame_abajo.pack_forget()
            self.frame_2.pack_forget()
            self.titl_label.pack_forget()
            self.desp_frame.pack_forget()
            self.desp_exp.pack_forget()
            self.frame_2.pack_forget()
            self.despido.place_forget()
            self.desp_int.place_forget()
            self.textemp.place_forget()
            self.sig_emp.place_forget()
            self.atr_emp.place_forget()
            self.mas_ef.place_forget()

            self.titl_con.pack_forget()
            self.desp_con.pack_forget()
            self.desp_exp_con.pack_forget()
            self.field_con.pack_forget()
            self.frame_3.pack_forget()

            self.sig_inv.place_forget()
            self.atr_inv.place_forget()
            self.titl_inv1.pack_forget()
            self.desp_inv1.pack_forget()
            self.desp_exp_inv1.pack_forget()

            self.titl_arq.pack_forget()
            self.desp_arq.pack_forget()
            self.desp_exp_arq.pack_forget()
            self.textarq.place_forget()
            self.mostrar_arq.place_forget()

            self.titl_agg.pack(pady = 10)
            self.desp_agg.pack(anchor='n')
            self.desp_exp_agg.pack(pady= 10)
            self.frame_3.pack(side="top",fill="both")
            self.field_agg.pack(pady = 40)
        

        #arqueo de caja ----------------------------------------------------------------------------------------------------------------------------------------------------------
        def show_arqueo(event):
            x = Orden.getCaja()[0].getIngresos()
            self.info_arq = ''
            for i in range(len(x)):
                self.info_arq = self.info_arq + f'Ingreso {i+1}:  {x[i]}\n'
            self.info_arq = self.info_arq + f'\n  Total: {Orden.getCaja()[0].getEfectivo()}'
            self.textarq.configure(state='normal')
            self.textarq.delete('1.0', 'end-1c')
            self.textarq.insert(tk.END,self.info_arq)
            self.textarq.configure(state='disabled')
                
        self.mostrar_arq.bind('<ButtonRelease-1>', show_arqueo)
        def arq_caja():
            self.frame_abajo.pack_forget()
            self.frame_2.pack_forget()
            self.titl_label.pack_forget()
            self.desp_frame.pack_forget()
            self.desp_exp.pack_forget()
            self.frame_2.pack_forget()
            self.despido.place_forget()
            self.desp_int.place_forget()
            self.textemp.place_forget()
            self.sig_emp.place_forget()
            self.atr_emp.place_forget()
            self.mas_ef.place_forget()

            self.titl_con.pack_forget()
            self.desp_con.pack_forget()
            self.desp_exp_con.pack_forget()
            self.field_con.pack_forget()
            self.frame_3.pack_forget()

            self.sig_inv.place_forget()
            self.atr_inv.place_forget()
            self.titl_inv1.pack_forget()
            self.desp_inv1.pack_forget()
            self.desp_exp_inv1.pack_forget()

            self.titl_agg.pack_forget()
            self.desp_agg.pack_forget()
            self.desp_exp_agg.pack_forget()
            self.field_agg.pack_forget()

            self.titl_arq.pack(pady = 10)
            self.desp_arq.pack(anchor= 'n')
            self.desp_exp_arq.pack(pady = 10)
            self.frame_2.pack(side="top",fill="both")
            self.textarq.place(relx=0.5,rely=0.5,relheight=0.6, relwidth= 0.6, anchor= 'c')
            self.mostrar_arq.place(relx=0.5, rely= 0.9, anchor ='c')

        #esta funcion ejecuta las opciones del combobox de Archivo
        def opciones_Archivo(event):
            if self.Archivo.get()=="Aplicacion":
                self.Archivo.set("Archivo")
                descripcion_software()
                
            elif self.Archivo.get()=="Salir":
                self.Archivo.set("Archivo")
                self.ventana_inicio()


        
        
            
        #esta funcion ejecuta las opciones del combobox de opciones_p_y_C(todavia faltan por definir bien las funciones)
        def opciones_p_y_c(event):
            if self.p_y_c.get()=="Ver y despedir empleados":
                show_empleados()
                self.p_y_c.set("Procesos y consultas")

            elif self.p_y_c.get()=="Ver inventario":
                show_inv()
                self.p_y_c.set("Procesos y consultas")

            elif self.p_y_c.get()=="Contratar empleado":
                contratar_empleado()
                self.p_y_c.set("Procesos y consultas")

            elif self.p_y_c.get()=="Anadir/aumentar ingrediente":
                new_ingredient()
                self.p_y_c.set("Procesos y consultas")

            elif self.p_y_c.get()=="Arqueo de caja":
                arq_caja()
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
        self.p_y_c = tk.ttk.Combobox(self.frame_1,values=["Ver y despedir empleados","Contratar empleado", "Ver inventario", 'Anadir/aumentar ingrediente', 'Arqueo de caja'],textvariable=valorDefecto_p_y_c,state="readonly")
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
