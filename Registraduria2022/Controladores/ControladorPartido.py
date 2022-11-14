from Repositorios.RepositorioPartido import RepositorioPartido
from Modelos.Partido import Partido

class ControladorPartido():
    def __init__(self):#CONSTRUCTOR
        self.repositorioPartido = RepositorioPartido()

    def index(self): #OPTENER TODOS LOS DATOS
        return self.repositorioPartido.findAll()

    def create(self, infoPartido):  #CREAR UN DOCUMENTO EN EL MODELO
        partido = Partido(infoPartido)
        return self.repositorioPartido.save(partido)

    def update(self, id, infoPartido):  #ACTUALIZAR DATOS DEL MODELO
        partido = Partido(self.repositorioPartido.findById(id))
        partido.nombre = infoPartido['nombre']
        partido.lema = infoPartido['lema']
        return self.repositorioPartido.save(partido)

    def delete(self, id):  # BORRAR DATOS DEL MODELO
        return self.repositorioPartido.delete(id)

    def show(self, id):  # CONSULTAR UN DATO ESPECIFICO DEL MODELO
        partido = Partido(self.repositorioPartido.findById(id))
        return partido.__dict__
