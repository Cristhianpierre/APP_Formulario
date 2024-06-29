from PyQt5 import QtWidgets,uic

class CalculadoraController:

    def __init__(self):
        app=QtWidgets.QApplication([])
        self.ventana=uic.loadUi("view/frmcalculadora.ui")
        self.ventana.show()
        app.exec()
        