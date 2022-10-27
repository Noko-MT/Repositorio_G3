from Repositorios.RepositorioCandidato import RepositorioMateria
from Repositorios.RepositorioMesas import RepositorioDepartamento
from Modelos.Resultado import Materia
from Modelos.Mesas import Departamento

class ControladorMateria():
    def __init__(self):
        self.repositorioMateria = RepositorioMateria()
        self.repositorioDepartamento = RepositorioDepartamento()
    def index(self):
        return self.repositorioMateria.findAll()
    def create(self, infoMateria):
        materia = Materia(infoMateria)
        return self.repositorioMateria.save(materia)
    def update(self, id, infoMateria):
        materia = Materia(self.repositorioMateria.findById(id))
        materia.nombre = infoMateria['nombre']
        materia.creditos = infoMateria['creditos']
        return self.repositorioMateria.save(materia)
    def delete(self, id):
        return self.repositorioMateria.delete(id)
    def show(self, id):
        materia = Materia(self.repositorioMateria.findById(id))
        return materia.__dict__
    def setDepartamento(self, id_materia, id_departamento):
        materia = Materia(self.repositorioMateria.findById(id_materia))
        departamento = Departamento(self.repositorioDepartamento.findById(id_departamento))
        materia.departamento = departamento
        return self.repositorioMateria.save(materia)
