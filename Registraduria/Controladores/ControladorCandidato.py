from Modelos.Candidato import Candidato
from Modelos.Partido import Partido
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioPartido import RepositorioPartido

class ControladorCandidato():
    def __init__(self):#CONSTRUCTOR
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioPartido = RepositorioPartido()

    def index(self): #OPTENER TODOS LOS DATOS
        return self.repositorioCandidato.findAll()

    def create(self, infoCandidato):  #CREAR UN DOCUMENTO EN EL MODELO
        candidato = Candidato(infoCandidato)
        return self.repositorioCandidato.save(candidato)

    def update(self, id, infoCandidato):  #ACTUALIZAR DATOS DEL MODELO
        candidato = Candidato(self.repositorioCandidato.findById(id))
        candidato.cedula = infoCandidato['cedula']
        candidato.numero_resolucion = infoCandidato['numero_resolucion']
        candidato.nombre = infoCandidato['nombre']
        candidato.apellido = infoCandidato['apellido']
        return self.repositorioCandidato.save(candidato)

    def delete(self, id):  # BORRAR DATOS DEL MODELO
        return self.repositorioCandidato.delete(id)

    def show(self, id):  # CONSULTAR UN DATO ESPECIFICO DEL MODELO
        candidato = Candidato(self.repositorioCandidato.findById(id))
        return candidato.__dict__

    def setPartido(self, id_candidato, id_partido):
        candidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        partido = Partido(self.repositorioPartido.findById(id_partido))
        candidato.partido = partido
        return self.repositorioCandidato.save(candidato)


