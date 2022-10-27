from Repositorios.RepositorioMesas import RepositorioMesas
from Modelos.Mesas import Mesas

class ControladorMesas():
    def __init__(self):
        self.repositorioMesas = RepositorioMesas()

    def index(self):
        return self.repositorioMesas.findAll()

    def create(self, infoMesas):
        mesas = Mesas(infoMesas)
        return self.repositorioMesas.save(mesas)

    def update(self, id, infoMesas):
        mesas = Mesas(self.repositorioMesas.findById(id))
        mesas.numero_mesa = infoMesas['numero_mesa']
        mesas.cantidad_inscritos = infoMesas['cantidad_inscritos']
        return self.repositorioMesas.save(mesas)

    def delete(self, id):
        return self.repositorioMesas.delete(id)

    def show(self, id):
        mesas = Mesas(self.repositorioMesas.findById(id))
        return mesas.__dict__
