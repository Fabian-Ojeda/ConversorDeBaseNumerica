from tkinter import *
import os
import re
from tkinter.ttk import Combobox
from src.Controller.controllerApp import *

class MainView():

    def __init__(self, controllerApp):
        self.controllerApp = controllerApp

    def start(self):
        self.root = Tk()
        self.root.title("Conversor de numeros")
        self.root.geometry("800x500+400+200")
        self.root.resizable(False, False)
        self.varResult= StringVar()
        self.varResult.set("Resultado: ")
        self.__initComponents()
        self.root.mainloop()

    def __initComponents(self):
        self.frame = Frame(height=500,width=750)
        #La siguiente linea es para personalizar el cursor, pero no se cual cursor ponerle XD
        #self.frame.config(cursor="")
        self.frame.grid_propagate(False)
        self.frame.pack(expand=1)

        self.labelTitle = Label(self.frame, text="Conversor de base numerica", fg="Blue", font =("Aero",40),anchor="w", pady=30)
        self.labelTitle.grid(row=1, column=0, columnspan=3)

        self.labelDetails = Label(self.frame, text="Por favor ingrese un numero y seleccione la base original\ny la base a la que desea convertirlo", fg="Blue", font=("Aero", 20), anchor="w",pady=20)
        self.labelDetails.grid(row=2, column=0, columnspan=3)

        self.labelEnterNumber = Label(self.frame,text="Numero",fg="Blue", font=("Aero", 20), anchor="w",pady=10)
        self.labelEnterNumber.grid(row=3, column=0, columnspan=1)

        self.labelBaseOrigin = Label(self.frame, text="Base Original", fg="Blue", font=("Aero", 20), anchor="w",pady=10)
        self.labelBaseOrigin.grid(row=3, column=1, columnspan=1)

        self.labelBaseOrigin = Label(self.frame, text="Base Destino", fg="Blue", font=("Aero", 20), anchor="w",pady=10)
        self.labelBaseOrigin.grid(row=3, column=2, columnspan=1)

        self.textNumber = StringVar()
        self.textFieldNumber = Entry(self.frame, textvariable=self.textNumber, font=("Aero", 20) , width=13)
        self.textFieldNumber.grid(row=4, column=0, columnspan=1)

        self.comboBaseOrigin = Combobox(self.frame, font=("Aero", 20), state="readonly", width=3)
        self.comboBaseOrigin["values"] = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
        self.comboBaseOrigin.current(0)
        #self.comboBaseOrigin.bind("<<ComboboxSelected>>", self.selection_changed)
        self.comboBaseOrigin.grid(row=4, column=1, columnspan=1,pady=10)

        self.comboBaseDestiny = Combobox(self.frame, font=("Aero", 20), state="readonly", width=3)
        self.comboBaseDestiny["values"] = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
                                          23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
        self.comboBaseDestiny.current(0)
        # self.comboBaseOrigin.bind("<<ComboboxSelected>>", self.selection_changed)
        self.comboBaseDestiny.grid(row=4, column=2, columnspan=1)


        self.buttonAccept = Button(self.frame, text="Calcular", bg="green",fg="white", font=("Aero",20),command = self.controllerApp.calculate, pady=1)
        self.buttonAccept.grid(row=5, column=1, columnspan=1)

        self.labelResult = Label(self.frame, textvariable=self.varResult, fg="Blue", font=("Aero", 20), anchor="w",pady=10)
        self.labelResult.grid(row=6, column=0, columnspan=3)

    def getNumber(self):
        return self.textNumber.get()

    def getBaseOrigin(self):
        return self.comboBaseOrigin.get()

    def getBaseDestiny(self):
        return self.comboBaseDestiny.get()

    def setResult(self, result):
        self.varResult.set("Resultado: "+result)