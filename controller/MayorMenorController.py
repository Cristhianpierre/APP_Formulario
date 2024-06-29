from PyQt5 import QtWidgets,uic

class MayorMenoraController:

    def __init__(self):
        app=QtWidgets.QApplication([])
        self.ventana=uic.loadUi("view/frmMayorMenor.ui")
        self.ventana.show()
        app.exec()
        