from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QMainWindow, QMessageBox

from UI.vtnPrincipal import Ui_vtnPrincipal

class PersonaServicio(QMainWindow):
    ''''
    Clase que genera la logica de los objetos persona
    '''
    def __init__(self):
        super(PersonaServicio,self).__init__()
        self.ui = Ui_vtnPrincipal()
        self.ui.setupUi(self)
        self.ui.btnGuardar.clicked.connect(self.guardar)
        self.ui.txtCedula.setValidator(QIntValidator())
        self.ui.btnLimpiar.clicked.connect(self.limpiar)


    def guardar(self):
        nombre = self.ui.txtNombre.text()
        apellido = self.ui.txtApellido.text()
        cedula = self.ui.txtCedula.text()
        sexo = self.ui.btnSexo.currentText()
        #validacion de los datos del formulario
        if nombre == "":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar el nombre")
        elif apellido == "":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar el apellido")
        elif len(cedula) < 10:
            QMessageBox.warning(self, "Advertencia", "Debe ingresar la cedula")
        elif sexo == "Seleccionar":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar el sexo")
        else:
            print(nombre)
            print(apellido)
            print(cedula)
            print(sexo)

            self.ui.statusbar.showMessage('Se guardo la información', 500)
            #borrar campos del formulario
            self.ui.txtNombre.setText('')
            self.ui.txtApellido.setText('')
            self.ui.txtCedula.setText('')
            self.ui.btnSexo.setCurrentText('')
    def limpiar(self):
        nombre = self.ui.txtNombre.clear()
        apellido = self.ui.txtApellido.clear()
        cedula = self.ui.txtCedula.clear()
        self.ui.statusbar.showMessage('informacion eliminada correctamente', 500)
