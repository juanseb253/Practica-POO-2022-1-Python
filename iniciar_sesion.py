import tkinter as tk
import os
import pathlib
from tkinter import messagebox
from tkinter import ttk
import ventana_inicio
import ventana_principal_empleado
import ventana_principal_gerente

path = os.path.join(pathlib.Path(__file__).parent.absolute())

#ventana principal, donde se ejecuta el programa
class Inicio_sesion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ventana_inicio_sesion")
        self.geometry("1360x720")
        self.configure(bg="white")

        #este frame(frame_0) corresponde al de la parte superior

        self.frame_0=tk.Frame(self,bg="red",height=80)
        self.frame_0.pack(side="top",fill="x")

        #una etiqueta que contiene al titulo del nombre del software

        self.titulo=tk.Label(self.frame_0,text=" elija una opcion ")
        self.titulo.config(fg="white",bg="red",font=("italic",30,"italic"))
        self.titulo.pack(anchor="c")

        #este frame(frame_1) corresponde a la zona de arriba, es meramente decorativo

        self.frame_1=tk.Frame(self,bg="gray",height=40)
        self.frame_1.pack(side="top",fill="x")
        
        #en este frame(frame_inicio) se encuentran los botones relacionados con el inicio de sesion
        self.frame_inicio=tk.Frame(self,bg="white",height=650)
        self.frame_inicio.pack(side="top",fill="both")
        
        #inicio de sesion como empleado

        self.boton_1_sesion = tk.Button(self.frame_inicio,text="iniciar sesion como_empleado",command=self.ventana_empelado)

        self.boton_1_sesion.place(x=620,y=100,width=300, height=80)

        #inicio de sesion como gerente

        self.boton_2_sesion = tk.Button(self.frame_inicio,text="iniciar sesion como gerente",command=self.ventana_gerente)

        self.boton_2_sesion.place(x=620,y=200,width=300, height=80)

        #regresar, vuelve al menu principal

        self.boton_3_sesion = tk.Button(self.frame_inicio,text="volver ",command=self.volver)

        self.boton_3_sesion.place(x=620,y=300,width=300, height=80)
        
        #frame de la parte de abajo, es meramente decorativo 
        self.frame_abajo=tk.Frame(self,bg="red",height=80)
        self.frame_abajo.pack(side="bottom",fill="both")

        self.mainloop()

    #cuando se da click en el boton de iniciar sesion como empleado
    def ventana_empelado(self):
        self.destroy()
        ventana_principal_empleado.Ventana_principal_empleado()

    #cuando se da click en el boton de iniciar sesion como gerente
    def ventana_gerente(self):
        self.destroy()
        ventana_principal_gerente.Ventana_principal_gerente()

    #cuando se da click en el boton volver
    def volver(self):
        self.destroy()
        ventana_inicio.Ventana_inicio()