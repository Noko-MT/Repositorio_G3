#CREACION DE CLASE ABSTRACTA QUE SIRVE COMO BASE PARA CREAR LOS MODELOS
from abc import ABCMeta

class AbstractModelo(metaclass=ABCMeta):
    def __init__(self, data):#CONSTRUCTOR DE LA CLASE
        for llave, valor in data.items():
            setattr(self, llave, valor)#AGREGAR LLAVES Y VALORES



