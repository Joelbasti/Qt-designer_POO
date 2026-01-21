

class Persona:
    '''clase que permite crear objetos de tipo persona
    '''
    def __init__(self,cedula:str, nombre:str, apellido:str, sexo:str
              ,email:str=None):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.email = email


    @property
    def nombre(self):
        return self._nombre