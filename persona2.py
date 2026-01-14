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
        self.ui.btnLimpiar.clicked.connect(self.limpiar)


    def guardar(self):
        nombre = self.ui.txtNombre.text()
        apellido = self.ui.txtApellido.text()
        cedula = self.ui.txtCedula.text()
        #validacion de los datos del formulario
        if nombre == "":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar el nombre")
        elif apellido == "":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar el apellido")
        elif cedula == "":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar la cedula")
        else:
            print(nombre)
            print(apellido)
            print(cedula)

            self.ui.statusbar.showMessage('Se guardo la información', 500)
            #borrar campos del formulario
            self.ui.txtNombre.setText('')
            self.ui.txtApellido.setText('')
            self.ui.txtCedula.setText('')

    def limpiar(self):
        nombre = self.ui.txtNombre.clear()
        apellido = self.ui.txtApellido.clear()
        cedula = self.ui.txtCedula.clear()

