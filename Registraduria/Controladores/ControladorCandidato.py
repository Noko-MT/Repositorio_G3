from Repositorios.RepositorioCandidato import RepositorioCandidato
from Modelos.Candidato import Candidato

class ControladorCandidato():
    def __init__(self):
        self.repositorioCandidato=RepositorioCandidato()

    def index(self):
        return self.repositorioCandidato.findAll()

    def create(self, infoCandidato):
        candidato=Candidato(infoCandidato)
        return self.repositorioCandidato.save(candidato)

    def update(self, id, infoCandidato):
        candidato=Candidato(self.repositorioCandidato.findById(id))
        candidato.cedula=infoCandidato['cedula']
        candidato.numero_resolucion=infoCandidato['numero_resolucion']
        candidato.nombre=infoCandidato['nombre']
        candidato.apellido=infoCandidato['apellido']
        return self.repositorioCandidato.save(candidato)

    def delete(self,id):
        return self.repositorioCandidato.delete(id)

    def show(self, id):
        candidato=Candidato(self.repositorioCandidato.findById(id))
        return candidato.__dict__


