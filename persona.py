
from PySide6.QtWidgets import QMainWindow

from UI.interfaz import Ui_vtnPrincipal


class PersonaServicio(QMainWindow):
    '''
    Clase que genera la logica de la clase PersonaServicio
    '''
    def __init__(self):
        super(PersonaServicio, self).__init__()
        self.ui = Ui_vtnPrincipal()
        self.ui.setupUi(self)
