from tkinter import *
from tkinter import messagebox
import tkinter as tk

class FieldFrame(Frame):
    def __init__(self,ventana,tituloCriterios,criterios,tituloValores):
        self.entradas = {} # Diccionario desde donde se podrá acceder a la entrada asociada a cada criterio
        self.valor_entradas =[] # Lista que contendra el valor de las entradas pasadas por el usuario
        super().__init__(ventana)
        self.tituloCriterios=tituloCriterios
        self.criterios=criterios
        self.tituloValores=tituloValores

        self.labeltituloCriterios=tk.Label(self,text=tituloCriterios)
        self.labeltituloCriterios.grid(row=0,column=0)
        self.labeltituloValores=tk.Label(self,text=tituloValores)
        self.labeltituloValores.grid(row=0,column=1)
        a=1
        for i in self.criterios:
            self.labelcriterios=tk.Label(self,text=i)
            self.labelcriterios.grid(row=a,column=0)
            self.entryvaloresentrada=tk.Entry(self)
            self.entryvaloresentrada.grid(row=a,column=1)
            self.entradas[i] = self.entryvaloresentrada
            a+=1
        #Boton aceptar
        self.botonAceptar = Button (self, width=10, text='Aceptar',command=self.aceptar)
        self.botonAceptar.grid(row = a+1, column = 0, ipadx=20, padx=30, pady = 6)
        #command=self.aceptar

        #Boton borrar
        self.botonBorrar = Button(self, width=10, text='Borrar',command = self.borrarValores)
        self.botonBorrar.grid(row = a+1, column = 1, ipadx=20, padx=30, pady = 5)
        #command = self.borrarValores)
    
    def aceptar(self):
        self.valor_entradas=[]
        for criterio in self.entradas:
            self.valor_entradas.append(self.getValue(criterio))
        return self.valor_entradas
    
    def borrarValores(self):
        for criterio in self.entradas:
            entrada = self.entradas[criterio]
            entrada.delete(0, "end")

    def getValue(self, criterio):
        entrada = self.entradas[criterio]
        return entrada.get()