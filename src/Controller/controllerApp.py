from src.view.MainView import MainView
from src.Model.Conversor import Conversor
from tkinter import messagebox as MessageBox

class controllerApp():

    def __init__(self):
        self.conversor = Conversor()
        self.mainWindow = MainView(self)
        self.mainWindow.start()


    def calculate(self):
        result = self.conversor.baseTobase(self.mainWindow.getNumber().upper(), int(self.mainWindow.getBaseOrigin()), int(self.mainWindow.getBaseDestiny()))
        if type(result) == str:
            self.mainWindow.setResult(result)
        else:
            MessageBox.showerror("Pailas", result)
